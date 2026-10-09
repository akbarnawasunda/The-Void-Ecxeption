#!/usr/bin/env python3
"""Check drafted chapter metadata and assemble reproducible reader copies.

This checks declarations, files, basic prose structure, and copy freshness.
It cannot prove POV quality, medical plausibility, or every narrative statement.
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re

from render_canon import ROOT, load_data, level_at

BEGIN = '<!-- BEGIN PROSE -->'
END = '<!-- END PROSE -->'


def extract_prose(text: str) -> str:
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError('Expected exactly one pair of PROSE markers')
    if text.index(BEGIN) >= text.index(END):
        raise ValueError('PROSE markers are reversed')
    prose = text.split(BEGIN, 1)[1].split(END, 1)[0].strip()
    if not prose:
        raise ValueError('Empty chapter prose')
    return prose


def workspace_path(root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts or rel.suffix != '.md':
        raise ValueError(f'Unsafe manuscript path: {relative}')
    if not rel.parts or rel.parts[0] != '12_NASKAH_UTAMA':
        raise ValueError(f'Outside manuscript section: {relative}')
    target = root / rel
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes repository: {relative}')
    return target


def calendar_age(day: date, epoch: date, age_at_epoch: int) -> int:
    return age_at_epoch + day.year - epoch.year - ((day.month, day.day) < (epoch.month, epoch.day))


def validate_manuscript(data: dict, root: Path = ROOT) -> list[str]:
    errors = []
    def require(ok: bool, message: str) -> None:
        if not ok:
            errors.append(message)
    try:
        m = data['manuscript']
        require(m['schema_version'] == 1 and m['status'] == 'draft', 'Manuscript schema/status invalid')
        require(m['revision'] >= 1, 'Revision must be positive')
        volume = data['volumes'][m['volume']-1]
        require(m['target_chapters'] == volume['chapters'][1] - volume['chapters'][0] + 1, 'Volume target differs from canon')
        chapters = m['chapters']
        ids = [c['chapter'] for c in chapters]
        require(bool(ids) and ids == list(range(volume['chapters'][0], max(ids)+1)), 'Drafted chapters must be sequential without gaps/duplicates')
        require(len({c['file'] for c in chapters}) == len(chapters), 'Duplicate chapter file')
        require(m['latest_drafted_chapter'] == max(ids), 'Latest drafted chapter is stale')
        require(m['next_chapter'] == max(ids)+1, 'Next chapter pointer is stale')
        require(m['minimum_prose_words'] >= 100, 'Minimum prose length policy invalid')
        epoch = date.fromisoformat(data['epoch_earth'])
        previous_end = epoch
        for c in chapters:
            n = c['chapter']
            prefix = f'Chapter{n}'
            start, end = date.fromisoformat(c['date_start']), date.fromisoformat(c['date_end'])
            require(previous_end <= start <= end, f'{prefix}: chronology moves backward')
            previous_end = end
            require(c['volume'] == m['volume'] and volume['chapters'][0] <= n <= volume['chapters'][1], f'{prefix}: wrong volume')
            require(c['pov'] == m.get('pov_overrides',{}).get(str(n),'yazha'), f'{prefix}: undeclared POV change')
            require(c['yazha_level'] == level_at(data,n), f'{prefix}: level differs from canon')
            # This edition covers BumiFana before its three-year invasion boundary.
            if m['volume'] == 1:
                require(epoch <= start <= end <= date(2087,8,17), f'{prefix}: outside V1 calendar')
                require(c['yazha_age'] == calendar_age(start,epoch,11), f'{prefix}: Yazha age mismatches date')
                require(c['nala_age'] == calendar_age(start,epoch,3), f'{prefix}: Nala age mismatches date')
                core_chapter = next(x['chapter'] for x in data['milestones'] if x['id']=='core')
                if n < core_chapter:
                    require(c['core_state']=='absent' and c['energy_percent'] is None, f'{prefix}: Core/energy assigned before installation')
                    require(c['niskala']==0 and c['active_techniques']==[], f'{prefix}: active technique assigned to Level0')
                require(start.year == int(data['volume1_cards'][n-1]['time'][-4:]), f'{prefix}: year differs from opening card')
            require(c['state_after'].strip() and c['known_after'].strip(), f'{prefix}: missing continuity state')
            path = workspace_path(root,c['file'])
            if not path.is_file():
                errors.append(f'{prefix}: missing chapter file {c["file"]}')
                continue
            text = path.read_text(encoding='utf-8')
            require('<!-- canon:v5 -->' in text, f'{prefix}: missing V5 marker')
            require(text.startswith(f'# Bab {n:03d} — {c["title"]}\n'), f'{prefix}: heading/title mismatch')
            tag = f'<!-- manuscript:chapter={n}; revision={m["revision"]}; pov={c["pov"]} -->'
            require(tag in text, f'{prefix}: wrong chapter/revision/POV tag')
            try:
                prose = extract_prose(text)
            except ValueError as exc:
                errors.append(f'{prefix}: {exc}')
                continue
            require(len(prose.split()) >= m['minimum_prose_words'], f'{prefix}: prose below draft length policy')
            require(not re.search(r'^\s*\|.*\|\s*$',prose,re.M), f'{prefix}: outline/table inside chapter prose')
            require(not re.search(r'\b(TODO|TBD|FIXME)\b',prose), f'{prefix}: unfinished placeholder')
            for literal in c.get('blocked_prose_literals',[]):
                require(literal.casefold() not in prose.casefold(), f'{prefix}: withheld identity/ability appears in prose: {literal}')
        require(chapters[0]['date_start'] == data['epoch_earth'], 'First draft must start on canon epoch')
        if m['next_chapter'] <= volume['chapters'][1]:
            require(m['next_chapter_year'] == int(data['volume1_cards'][m['next_chapter']-1]['time'][-4:]), 'Next chapter year differs from opening card')
        edition_ids=set()
        edition_paths=set()
        source_paths={c['file'] for c in chapters}
        for e in m['reading_editions']:
            require(e['id'] not in edition_ids and e['file'] not in edition_paths, 'Duplicate reading edition')
            edition_ids.add(e['id']);edition_paths.add(e['file'])
            workspace_path(root,e['file'])
            require(e['file'] not in source_paths, 'Reading copy would overwrite chapter source')
            require(e['volume']==m['volume'] and e['revision']==m['revision'], 'Edition volume/revision mismatch')
            require(e['start'] <= e['end'] and all(n in ids for n in range(e['start'],e['end']+1)), 'Reading edition contains undrafted chapters')
        for c in m.get('new_minor_characters',[]):
            require(c['first_chapter'] in ids and c['place'] in data['clock_rates'], f'{c["name"]}: invalid debut/place')
            require(0<=c['level']<=16 and 0<c['age_at_epoch']<data['levels'][c['level']]['lifespan'], f'{c["name"]}: age/level invalid')
    except (KeyError,TypeError,ValueError,IndexError) as exc:
        errors.append(f'Invalid manuscript data: {exc}')
    return errors


def render_edition(data: dict, edition: dict, root: Path = ROOT) -> str:
    m = data['manuscript']
    chapters = [c for c in m['chapters'] if edition['start']<=c['chapter']<=edition['end']]
    bodies = [(c,extract_prose(workspace_path(root,c['file']).read_text(encoding='utf-8'))) for c in chapters]
    words = sum(len(body.split()) for _,body in bodies)
    out = f'# The Void’s Exception\n\n## Volume {edition["volume"]} — {edition["title"]}\n\n'
    out += '<!-- canon:v5 -->\n<!-- manuscript:reading-copy; generated -->\n\n'
    out += f'*Draf {m["revision"]} · Bab {edition["start"]}–{edition["end"]} · {words:,} kata berdasarkan pemisah spasi.*\n\n'.replace(',', '.')
    out += 'Berkas baca ini memuat bab utuh, bukan kartu alur. Sumber bab dan catatan kesinambungan tersedia di [indeks naskah](00_INDEKS_NASKAH.md).\n\n'
    out += '## Daftar bab\n\n'
    for c,_ in bodies:
        out += f'- [Bab {c["chapter"]:03d} — {c["title"]}](#bab-{c["chapter"]:03d})\n'
    for c,body in bodies:
        out += f'\n---\n\n<a id="bab-{c["chapter"]:03d}"></a>\n\n## Bab {c["chapter"]:03d} — {c["title"]}\n\n'
        out += body+'\n'
    out += f'\n---\n\n*Berkas baca ini berhenti pada bab {edition["end"]}. Volume {edition["volume"]} masih dalam penulisan; kelanjutannya mengikuti kartu alur dan kalender kanon.*\n'
    return out


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Validate without writing reader copies')
    args=parser.parse_args()
    data=load_data()
    errors=validate_manuscript(data)
    if errors:
        for error in errors:print('FAIL:',error)
        return 1
    for edition in data['manuscript']['reading_editions']:
        path=workspace_path(ROOT,edition['file'])
        expected=render_edition(data,edition)
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8')!=expected:
                errors.append(f'Stale/missing reading copy: {edition["file"]}; run render_manuscript.py')
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(expected,encoding='utf-8')
    if errors:
        for error in errors:print('FAIL:',error)
        return 1
    chapters=data['manuscript']['chapters']
    total=0
    for c in chapters:
        count=len(extract_prose(workspace_path(ROOT,c['file']).read_text(encoding='utf-8')).split());total+=count
        print(f'OK: chapter{c["chapter"]:03d} · {count} words · {c["date_start"]} · Lv{c["yazha_level"]}')
    print(f'OK: {len(chapters)} complete chapter drafts; {total} whitespace-separated prose words; reader copies {"checked" if args.check else "rendered"}')
    print('Scope: declared continuity/copy checks, NOT automatic literary or full semantic validation.')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
