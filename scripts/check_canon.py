#!/usr/bin/env python3
"""Check the parts of the fiction contract that can actually be checked.

This is not a semantic proof of every sentence or a literary-quality metric.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from fractions import Fraction
from pathlib import Path
from urllib.parse import unquote

from render_canon import ROOT, MARKER, clock_totals, level_at, load_data, render_tables, replace_blocks


def containing_volume(data: dict, chapter: int) -> int | None:
    for v in data['volumes']:
        if v['chapters'][0] <= chapter <= v['chapters'][1]:
            return v['id']
    return None


def check_range_coverage(ranges: list[list[int]], start: int, end: int, label: str) -> list[str]:
    errors = []
    cursor = start
    for a, b in ranges:
        if type(a) is not int or type(b) is not int or a != cursor or b < a:
            errors.append(f'{label}: gap/overlap/invalid range {a}–{b}, expected start {cursor}')
        cursor = b + 1
    if cursor != end + 1:
        errors.append(f'{label}: final chapter {cursor-1}, expected {end}')
    return errors


def validate_data(data: dict) -> list[str]:
    errors: list[str] = []
    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)
    try:
        require(data['version'] == '5.0', 'Version must be 5.0')
        require(data['epoch_earth'] == '2084-08-17', 'Epoch must be 17 August 2084')
        date.fromisoformat(data['epoch_earth'])
        require(data['epoch_yazha_age'] == 11, 'Yazha starts at 11')
        require(data['constraints'] == {
            'ending':'vision_then_shell_then_amnesia', 'friends':'mortal',
            'time':'inter_realm_dilation','protagonist':'ordinary_human_no_hidden_lineage'}, 'Locked user constraints changed')
        require(data['clock_rates'] == {'bumi_fana':1,'bumi_abadi':3,'bintang':12,'kekosongan':60,'keabadian':300}, 'Clock ratios changed without contract migration')
        levels = data['levels']
        require([l['id'] for l in levels] == list(range(18)), 'Levels must cover 0–17 exactly once')
        require(len({l['name'] for l in levels}) == 18, 'Duplicate level name')
        errors += check_range_coverage([l['yazha_chapters'] for l in levels],1,1530,'Level states')
        for previous,current in zip(levels[:16], levels[1:17]):
            require(current['lifespan'] > previous['lifespan'], f'Lifespan not monotonic at {current["name"]}')
        require(levels[17]['lifespan'] is None,'Lv17 has no biological aging cap, not invulnerability')
        volumes=data['volumes']
        require([v['id'] for v in volumes]==list(range(1,15)), 'Volumes must cover 1–14')
        errors += check_range_coverage([v['chapters'] for v in volumes],1,1530,'Volumes')
        arc_count=0
        for v in volumes:
            arcs=v['arcs']; arc_count+=len(arcs)
            require(bool(arcs),f'V{v["id"]}: empty arcs')
            errors += check_range_coverage([a['chapters'] for a in arcs],*v['chapters'],f'V{v["id"]} arcs')
            for a in arcs:
                require(all(isinstance(a[k],str) and a[k].strip() for k in ('title','action','choice','aftermath')), f'V{v["id"]}: empty arc card')
            require(all(s['place'] in data['clock_rates'] for s in v['segments']),f'V{v["id"]}: unclocked place, including outside Shell')
            if errors and any(s['place'] not in data['clock_rates'] for s in v['segments']):
                return errors
            require(all(Fraction(s['earth_years']) > 0 for s in v['segments']), f'V{v["id"]}: nonpositive duration')
            segment_end=v['chapters'][1] - (1 if v['id']==14 else 0)
            errors += check_range_coverage([s['chapters'] for s in v['segments']],v['chapters'][0],segment_end,f'V{v["id"]} clock segments')
        require(arc_count==74,'Expected 74 explicit arc cards')
        totals=clock_totals(data)
        require(totals[-1]['earth']==39, 'Main timeline must total 39 Earth years')
        require(totals[-1]['subjective']==Fraction('4016.6'), 'Main timeline must total 4016.6 local years')
        require(totals[-1]['age']==Fraction('4027.6'),'Final Yazha age must be 4027.6')
        require(2084 + totals[-1]['earth']==2123,'Main Earth endpoint is 2123')
        expected={'core':1,'harmonisasi':2,'voidstep':2,'primeval':4,'gerbang_api':5,'gerbang_kesepian':9,'gerbang_nameless':13,'dinding_1':16,'dinding_2':16,'vision':16,'shell':17}
        milestones={m['id']:m for m in data['milestones']}
        require(len(milestones)==len(data['milestones']) and set(milestones)==set(expected),'Milestone IDs missing/duplicated')
        for id,lv in expected.items():
            m=milestones[id]
            require(containing_volume(data,m['chapter'])==m['volume'],f'{id}: wrong volume')
            require(level_at(data,m['chapter'])==lv,f'{id}: needs Lv{lv} at its chapter')
        require(milestones['shell']['chapter']==1530 and milestones['vision']['chapter']<1530,'Vision precedes actual crossing on final chapter')
        require(milestones['core']['chapter']<milestones['harmonisasi']['chapter']<milestones['voidstep']['chapter'],'Core → harmonization → Voidstep order')
        deaths={e['id']:e for e in data['deaths']}
        required_deaths={'preman','dhiza','wiadava','moxi_victim','varek','veyla','goliath','varin','pemburu','vaniya','bhas','hampa','yuna'}
        require(set(deaths)==required_deaths and len(deaths)==len(data['deaths']), 'Critical death IDs missing/duplicated')
        for e in data['deaths']:
            require(e['actual'] is True,f'{e["id"]}: actual death changed to vision')
            require(containing_volume(data,e['chapter'])==e['volume'],f'{e["id"]}: death in wrong volume')
            require(e['chapter']<milestones['vision']['chapter'],f'{e["id"]}: actual death after vision')
        require(level_at(data,deaths['preman']['chapter'])==0,'Preman incident is physical Level0, not energy')
        require(level_at(data,deaths['vaniya']['chapter'])==10,'Vaniya rescue attempts after tested Realmwarp')
        for c in data['critical_antagonists']:
            require(c['death'] in deaths and c['level']>0,f'{c["name"]}: invalid antagonist/death reference')
        for s in data['lesh']:
            require(s['physically_removed'] is False,f'Lesh #{s["id"]}: infrastructure must remain installed')
            require(containing_volume(data,s['mandate_chapter'])==s['mandate_volume'],f'Lesh #{s["id"]}: wrong mandate volume')
        require(sorted(s['id'] for s in data['lesh'])==list(range(1,12)),'Exactly 11 Lesh, IDs 1–11')
        require(len({s['name'] for s in data['lesh']})==11,'Duplicate Lesh name')
        mins={'voidstep':2,'soul_pressure':1,'merah':3,'ungu':6,'merah_ungu':7,'domain':9}
        require({t['id'] for t in data['techniques']}==set(mins),'Technique roster changed')
        for t in data['techniques']:
            require(level_at(data,t['chapter'])>=mins[t['id']],f'{t["id"]}: technique available before minimum level')
            require(0<t['energy']<=100 and t['niskala']>=0,f'{t["id"]}: invalid cost')
            require(t['chapter']>=milestones['core']['chapter'],f'{t["id"]}: active technique before Core')
        require([s['stage'] for s in data['mode_stages']]==list(range(1,8)), 'Seven mode stages required')
        for s in data['mode_stages']:
            require(level_at(data,s['chapter'])>=s['min_level'],f'VT{s["stage"]}: before minimum level')
            require(0<s['activation_energy']<=100 and s['niskala']>0,f'VT{s["stage"]}: no free mode')
        require([t['at'] for t in data['niskala_thresholds']]==[10,25,50,100],'Niskala thresholds must include collapse at 100')
        m=data['mechanics']
        require(m['max_direct_level_gap']==2 and m['primeval_yield_percent_max']<100,'No unlimited counter or perpetual recycling')
        require(m['voidstep_cooldown_heartbeats']>=2 and m['niskala_recovery_per_hour']>0,'Invalid cooldown/recovery')
        require(m['voidmaw_rebind_seconds']==180,'Voidmaw operator phase must be seeded before fatal choice')
        require(data['clamp_limits']=={'bumi_fana':4,'bumi_abadi':4,'bintang':8,'kekosongan':12,'keabadian':16},'Clamp limits changed')
        for id in ('bhaskara','ryuna'):
            c=data['character_clocks'][id]
            require(c['max_level']==4 and c['residence_after_invasion']=='bumi_abadi',f'{id}: mortal/clock changed')
            elapsed=Fraction(c['death_earth_elapsed'])
            age=Fraction(c['age_at_invasion'])+3*(elapsed-3)
            v=deaths[c['death']]['volume']
            prior=totals[v-2]['earth']
            require(prior<=elapsed<=totals[v-1]['earth'],f'{id}: death clock not within its volume')
            require(age<levels[4]['lifespan'],f'{id}: biological age exceeds ceiling')
        n=data['character_clocks']['nala']
        require(Fraction(n['age_at_invasion'])+Fraction(n['awake_years_in_captivity'])==8,'Nala must leave captivity at biological age8')
        require(n['rescued_at_volume_end']==5 and n['residence_after_rescue']=='bumi_abadi' and n['final_level']==6,'Nala rescue/life path changed')
        nala_age=8+3*(totals[-1]['earth']-totals[4]['earth'])
        require(nala_age==92,'Nala final age must be92')
        w=data['wiadava']; reserve=levels[w['original_level']]['lifespan']-w['age_at_epoch']
        require(w['massacre_years_before_epoch']<w['age_at_epoch'],'Aethel massacre predates Wiadava birth')
        require(reserve-w['damaged_reserve_multiplier']*w['earth_years_until_death']==w['final_gate_reserve_cost'],'Wiadava final reserve arithmetic fails')
        dc=data['duty_cycle']
        require(Fraction(dc['prison_local_years'])*Fraction(dc['active_fraction'])==dc['total_awake_years'],'Dewan stasis duty-cycle arithmetic fails')
        require(len(dc['members'])==7 and len({e['name'] for e in dc['members']})==7,'Dewan must contain seven people')
        for c in dc['members']:
            require(dc['total_awake_years']<=c['biological_age']<levels[c['level']]['lifespan'],f'{c["name"]}: invalid biological age')
        setups=data['setup_payoffs']
        require(len(setups)==18 and len({s['id'] for s in setups})==18,'18 setup/payoff IDs required')
        for s in setups:
            require(all(1<=ch<=1530 for ch in s['setup']+s['payoff']),f'{s["id"]}: chapter outside main story')
            require(all(any(a<b for a in s['setup']) for b in s['payoff']),f'{s["id"]}: payoff without prior setup')
        require([c['chapter'] for c in data['volume1_cards']]==list(range(1,36)),'35 V1 cards required')
        for c in data['volume1_cards']:
            require(all(c[k].strip() for k in ('title','time','want_obstacle','choice_result')),f'V1 card{c["chapter"]}: empty')
        sequel=data['sequel']
        require(sequel['status']=='blueprint' and sequel['actual_children']==[],'Sequel is blueprint; vision children not actual')
        errors += check_range_coverage([a['chapters'] for a in sequel['arcs']],1,600,'Sequel arcs')
        require(sequel['chapter_total']==600 and len(sequel['fields'])==8,'Sequel600chapters/eight horizontal fields')
        require(sum(Fraction(a['earth_years']) for a in sequel['arcs'])==6,'Sequel must total six Earth years')
        require(sum(Fraction(a['personal_years']) for a in sequel['arcs'])==300,'Sequel must total300 personal years')
        require(sequel['memory']=='facts_and_fragments_not_full_recovery' and sequel['ending']=='return_without_resurrection','No complete memory/reset/resurrection ending')
        require(nala_age+3*6==110,'Nala final sequel age110')
    except (KeyError,TypeError,ValueError,IndexError) as exc:
        errors.append(f'Invalid/missing data structure: {exc}')
    return errors


LINK=re.compile(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)')
EXCLUDED={'.git','.arena','.cache','.venv','node_modules','__pycache__'}


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob('*.md') if not any(part in EXCLUDED for part in p.relative_to(root).parts))


def validate_documents(data: dict,root: Path=ROOT) -> list[str]:
    errors=[]; tables=render_tables(data)
    legacy=set(data['legacy_documents'])
    expected=set(data.get('active_documents',[]))
    actual=set()
    for path in markdown_files(root):
        relative=path.relative_to(root).as_posix(); text=path.read_text(encoding='utf-8')
        if relative in legacy:
            if '<!-- canon:archive -->' not in text:
                errors.append(f'{relative}: missing archive marker')
            continue
        actual.add(relative)
        if '<!-- canon:v5 -->' not in text:
            errors.append(f'{relative}: missing active V5 marker')
        if re.search(r'\b(TODO|TBD|FIXME)\b',text):
            errors.append(f'{relative}: unfinished placeholder')
        # A changelog may quote old rules; it is not a source of active mechanics.
        if relative != '00_CATATAN_PERUBAHAN_V5.md':
            for phrase in data['forbidden_active_phrases']:
                if phrase.casefold() in text.casefold():
                    errors.append(f'{relative}: stale absolute phrase: {phrase}')
        try:
            if replace_blocks(text,tables)!=text:
                errors.append(f'{relative}: stale generated table/block; run render_canon.py')
        except ValueError as exc:
            errors.append(f'{relative}: {exc}')
        names=[m[1] for m in MARKER.findall(text)]
        for key in data.get('required_blocks',{}).get(relative,[]):
            if key not in names:
                errors.append(f'{relative}: required canon block missing: {key}')
        begins=text.count('<!-- BEGIN CANON:'); ends=text.count('<!-- END CANON:')
        if begins!=ends or begins!=len(MARKER.findall(text)):
            errors.append(f'{relative}: malformed canon block markers')
        for href in LINK.findall(text):
            href=href.strip()
            if href.startswith('<') and href.endswith('>'):
                href=href[1:-1]
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',href) or href.startswith('#'):
                continue
            target=unquote(href.split('#',1)[0].split('?',1)[0])
            if target and not (path.parent/target).is_file():
                errors.append(f'{relative}: broken local link {href}')
    for name in data.get('active_text_documents',[]):
        path=root/name
        if not path.is_file():
            errors.append(f'Missing active text document: {name}')
        elif not path.read_text(encoding='utf-8').startswith('CANON V5'):
            errors.append(f'{name}: missing V5 text marker')
    if expected:
        for p in sorted(expected-actual): errors.append(f'Missing active document: {p}')
        for p in sorted(actual-expected): errors.append(f'Unregistered active document: {p}')
    return errors


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-only',action='store_true')
    args=parser.parse_args()
    try:
        data=load_data()
    except (OSError,json.JSONDecodeError) as exc:
        print(f'FAIL: {exc}'); return 1
    errors=validate_data(data)
    if not errors and not args.data_only:
        errors+=validate_documents(data)
    if errors:
        for error in errors: print('FAIL:',error)
        return 1
    total=clock_totals(data)[-1]
    print(f"OK: 14 volumes / 1530 chapters / 74 arcs / 35 opening cards / 18 setup chains")
    print(f"OK: Earth {total['earth']} years; subjective {total['subjective']} = 4016.6; final age4027.6")
    print('OK: 11 installed Lesh; 7 living prisoners; Core/gates/techniques; irreversible critical deaths')
    print('OK: sequel blueprint600chapters /300personal /6Earth; Nala92→110; no actual vision children')
    if not args.data_only:
        print(f"OK: {len(data.get('active_documents',[]))} active documents, archive markers, canon blocks, local links")
    print('Scope: structural/mechanical checks, NOT a proof of all prose or literary quality.')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
