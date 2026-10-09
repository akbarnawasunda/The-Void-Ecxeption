"""Regression tests plus deliberately corrupt fixtures for the canon checker."""
from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_canon import validate_data,validate_documents,check_range_coverage
from render_canon import load_data,clock_totals,level_at,block,render_tables,replace_blocks


class DataTests(unittest.TestCase):
    def setUp(self):
        self.data=copy.deepcopy(load_data())

    def assert_invalid(self,needle=None):
        errors=validate_data(self.data)
        self.assertTrue(errors,'Corrupt fixture passed')
        if needle:
            self.assertTrue(any(needle in e for e in errors),errors)

    def test_current_canon(self):
        self.assertEqual(validate_data(self.data),[])

    def test_exact_clocks_include_home_visits(self):
        totals=clock_totals(self.data)
        self.assertEqual(totals[-1]['earth'],Fraction(39))
        self.assertEqual(totals[-1]['subjective'],Fraction(20083,5))
        self.assertEqual(totals[-1]['age'],Fraction(20138,5))
        self.assertEqual(totals[8]['local'],Fraction(2381,20))
        self.assertEqual(totals[10]['local'],Fraction(4781,20))
        self.assertEqual(totals[12]['local'],Fraction(2901,2))

    def test_costs_use_full_capacity(self):
        t={x['id']:x for x in self.data['techniques']}
        e=lambda id:Fraction(str(t[id]['energy']))
        spent=3*e('voidstep')+e('soul_pressure')+2*e('merah')
        self.assertEqual(100-spent,Fraction('70.5'))
        niskala=3*t['voidstep']['niskala']+t['soul_pressure']['niskala']+2*t['merah']['niskala']
        self.assertEqual(niskala,11)
        after_mode=100-spent-self.data['mode_stages'][3]['activation_energy']-5
        self.assertEqual(after_mode,Fraction('35.5'))
        self.assertLess(after_mode,e('domain'))
        # A 50%-of-full-capacity cost stays50 even when only50 is left.
        self.assertEqual(Fraction(50)-e('domain'),0)

    def test_recycling_cannot_generate_energy(self):
        yield_ratio=Fraction(self.data['mechanics']['primeval_yield_percent_max'],100)
        self.assertLess(100*yield_ratio*yield_ratio,100*yield_ratio)

    def test_reject_old_version(self):
        self.data['version']='4.0';self.assert_invalid('Version')

    def test_reject_changed_user_ending(self):
        self.data['constraints']['ending']='reset';self.assert_invalid('constraints')

    def test_reject_duplicate_level_range(self):
        self.data['levels'][3]['yazha_chapters'][0]=107;self.assert_invalid('Level states')

    def test_reject_volume_gap(self):
        self.data['volumes'][2]['chapters'][0]=122;self.assert_invalid('Volumes')

    def test_reject_wrong_final_chapter(self):
        self.data['volumes'][-1]['chapters'][1]=1531;self.assert_invalid('1530')

    def test_reject_blank_arc(self):
        self.data['volumes'][8]['arcs'][2]['choice']='';self.assert_invalid('empty arc')

    def test_reject_arc_overlap(self):
        self.data['volumes'][6]['arcs'][1]['chapters'][0]-=1;self.assert_invalid('arcs')

    def test_reject_old_timeless_outside_segment(self):
        self.data['volumes'][-1]['segments'][0]['place']='outside_time';self.assert_invalid('unclocked')

    def test_reject_missing_return_visit(self):
        self.data['volumes'][8]['segments'][1]['earth_years']='0';self.assert_invalid('nonpositive')

    def test_reject_incorrect_total(self):
        self.data['volumes'][5]['segments'][0]['earth_years']='3';self.assert_invalid('39 Earth')

    def test_reject_nonmonotonic_lifespan(self):
        self.data['levels'][4]['lifespan']=100;self.assert_invalid('monotonic')

    def test_reject_core_before_level1(self):
        self.data['milestones'][0]['chapter']=80;self.assert_invalid('core: needs Lv1')

    def test_reject_technique_before_core(self):
        self.data['techniques'][1]['chapter']=30;self.assert_invalid('before Core')

    def test_reject_vt2_in_volume3(self):
        self.data['mode_stages'][1]['chapter']=200;self.assert_invalid('VT2')

    def test_reject_vision_after_crossing(self):
        next(m for m in self.data['milestones'] if m['id']=='vision')['chapter']=1530
        self.assert_invalid('Vision precedes')

    def test_reject_cancelled_death(self):
        self.data['deaths'][5]['actual']=False;self.assert_invalid('actual death')

    def test_reject_wrong_death_volume(self):
        next(e for e in self.data['deaths'] if e['id']=='varin')['volume']=9
        self.assert_invalid('death in wrong volume')

    def test_reject_twelfth_lesh(self):
        self.data['lesh'].append({**self.data['lesh'][-1],'id':12,'name':'False node'})
        self.assert_invalid('Exactly 11')

    def test_reject_duplicate_lesh(self):
        self.data['lesh'][1]['id']=1;self.assert_invalid('Exactly 11')

    def test_reject_removing_civil_pump(self):
        self.data['lesh'][6]['physically_removed']=True;self.assert_invalid('remain installed')

    def test_reject_mortal_clock_change(self):
        self.data['character_clocks']['bhaskara']['residence_after_invasion']='bumi_fana'
        self.assert_invalid('mortal/clock')

    def test_reject_immortal_yuna(self):
        self.data['character_clocks']['ryuna']['max_level']=17;self.assert_invalid('mortal/clock')

    def test_reject_nala_wrong_stasis_age(self):
        self.data['character_clocks']['nala']['awake_years_in_captivity']='6'
        self.assert_invalid('age8')

    def test_reject_six_person_dewan(self):
        self.data['duty_cycle']['members'].pop();self.assert_invalid('seven people')

    def test_reject_stasis_training_freebie(self):
        self.data['duty_cycle']['active_fraction']='1';self.assert_invalid('duty-cycle')

    def test_reject_body_older_than_lifespan(self):
        self.data['duty_cycle']['members'][0]['biological_age']=590000000
        self.assert_invalid('biological age')

    def test_reject_wiadava_massacre_before_birth(self):
        self.data['wiadava']['massacre_years_before_epoch']=3000;self.assert_invalid('predates')

    def test_reject_wiadava_reserve_months_error(self):
        self.data['wiadava']['final_gate_reserve_cost']=5;self.assert_invalid('reserve arithmetic')

    def test_reject_payoff_without_setup(self):
        self.data['setup_payoffs'][0]['payoff']=[1];self.assert_invalid('without prior setup')

    def test_reject_missing_opening_card(self):
        self.data['volume1_cards'].pop();self.assert_invalid('35 V1')

    def test_reject_actual_vision_children(self):
        self.data['sequel']['actual_children']=['Akasa'];self.assert_invalid('vision children')

    def test_reject_resurrection_sequel(self):
        self.data['sequel']['ending']='resurrect';self.assert_invalid('resurrection')

    def test_reject_complete_memory_recovery(self):
        self.data['sequel']['memory']='everything';self.assert_invalid('complete memory')

    def test_reject_sequel_clock_drift(self):
        self.data['sequel']['arcs'][0]['earth_years']='2';self.assert_invalid('six Earth')

    def test_level_boundary_lookup(self):
        self.assertEqual(level_at(self.data,90),0)
        self.assertEqual(level_at(self.data,91),1)
        self.assertEqual(level_at(self.data,1009),10)
        self.assertEqual(level_at(self.data,1529),16)
        self.assertEqual(level_at(self.data,1530),17)
        with self.assertRaises(ValueError):level_at(self.data,1531)

    def test_range_gap_and_overlap(self):
        self.assertEqual(check_range_coverage([[1,5],[6,10]],1,10,'x'),[])
        self.assertTrue(check_range_coverage([[1,5],[5,10]],1,10,'x'))
        self.assertTrue(check_range_coverage([[1,5],[7,10]],1,10,'x'))


class DocumentTests(unittest.TestCase):
    def setUp(self):
        self.data=load_data()
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        self.data['legacy_documents']=[]
        self.data['active_text_documents']=[]
        self.data['active_documents']=['sample.md']
        self.path=self.root/'sample.md'
        self.path.write_text('# Sample\n<!-- canon:v5 -->\n'+block('clock_rates',self.data))

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_fixture(self):
        self.assertEqual(validate_documents(self.data,self.root),[])

    def test_stale_generated_table(self):
        self.path.write_text(self.path.read_text().replace('| 300 |','| 301 |'))
        self.assertTrue(any('stale' in e for e in validate_documents(self.data,self.root)))

    def test_broken_local_link(self):
        self.path.write_text(self.path.read_text()+'\n[Missing](not-there.md)\n')
        self.assertTrue(any('broken local link' in e for e in validate_documents(self.data,self.root)))

    def test_unmigrated_document(self):
        self.path.write_text('# Old\n')
        self.assertTrue(any('missing active' in e for e in validate_documents(self.data,self.root)))

    def test_stale_absolute_mechanic(self):
        self.path.write_text(self.path.read_text()+'\n'+self.data['forbidden_active_phrases'][0])
        self.assertTrue(any('stale absolute' in e for e in validate_documents(self.data,self.root)))

    def test_bad_markers(self):
        self.path.write_text(self.path.read_text().replace('END CANON:clock_rates','END CANON:levels'))
        self.assertTrue(any('malformed' in e for e in validate_documents(self.data,self.root)))

    def test_renderer_is_idempotent(self):
        text=self.path.read_text();tables=render_tables(self.data)
        self.assertEqual(replace_blocks(replace_blocks(text,tables),tables),text)

    def test_plot_change_requires_regeneration(self):
        original=block('plot_arcs',self.data)
        changed=copy.deepcopy(self.data)
        changed['volumes'][0]['arcs'][0]['choice']='Changed choice.'
        self.assertNotEqual(replace_blocks(original,render_tables(changed)),original)

    def test_required_block_cannot_be_removed(self):
        self.data['required_blocks']={'sample.md':['clock_rates']}
        self.path.write_text('# Sample\n<!-- canon:v5 -->\n')
        self.assertTrue(any('required canon block missing' in e for e in validate_documents(self.data,self.root)))

    def test_missing_text_prompt(self):
        self.data['active_text_documents']=['prompt.txt']
        self.assertTrue(any('Missing active text' in e for e in validate_documents(self.data,self.root)))
        (self.root/'prompt.txt').write_text('CANON V5 — text prompt\n')
        self.assertEqual(validate_documents(self.data,self.root),[])

    def test_unknown_marker_is_rejected(self):
        text='<!-- BEGIN CANON:unknown -->\nx\n<!-- END CANON:unknown -->'
        with self.assertRaises(ValueError):replace_blocks(text,render_tables(self.data))

    def test_archive_cannot_be_silently_active(self):
        self.data['legacy_documents']=['sample.md'];self.data['active_documents']=[]
        self.assertTrue(any('archive marker' in e for e in validate_documents(self.data,self.root)))
        self.path.write_text('<!-- canon:archive -->\nOld reference\n')
        self.assertEqual(validate_documents(self.data,self.root),[])


if __name__=='__main__':
    unittest.main()
