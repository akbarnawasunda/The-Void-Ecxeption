"""Structural/copy regression tests; they are not literary-quality tests."""
from __future__ import annotations

import copy
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_canon import load_data
from render_manuscript import extract_prose,render_edition,validate_manuscript,workspace_path,calendar_age
from datetime import date


class ManuscriptTests(unittest.TestCase):
    def setUp(self):
        self.data=copy.deepcopy(load_data())
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        m=self.data['manuscript']
        first=m['chapters'][0]
        m['chapters']=[first]
        m['latest_drafted_chapter']=1
        m['next_chapter']=2
        m['next_chapter_year']=2084
        m['new_minor_characters']=[]
        m['reading_editions']=[{**m['reading_editions'][0],'end':1}]
        self.path=self.root/first['file']
        self.path.parent.mkdir(parents=True)
        self.path.write_text((ROOT/first['file']).read_text(),encoding='utf-8')

    def tearDown(self):
        self.temp.cleanup()

    def invalid(self,needle):
        errors=validate_manuscript(self.data,self.root)
        self.assertTrue(any(needle in e for e in errors),errors)

    def test_actual_eight_chapters(self):
        self.assertEqual(validate_manuscript(load_data()),[])

    def test_valid_single_chapter_fixture(self):
        self.assertEqual(validate_manuscript(self.data,self.root),[])

    def test_extract_only_prose(self):
        body=extract_prose(self.path.read_text())
        self.assertTrue(body.startswith('Nala sudah'))
        self.assertNotIn('manuscript:chapter',body)
        self.assertGreaterEqual(len(body.split()),1000)

    def test_missing_prose_marker(self):
        self.path.write_text(self.path.read_text().replace('<!-- END PROSE -->',''))
        self.invalid('PROSE markers')

    def test_duplicated_prose_marker(self):
        self.path.write_text(self.path.read_text()+'\n<!-- BEGIN PROSE -->\n')
        self.invalid('PROSE markers')

    def test_summary_cannot_pass_as_chapter(self):
        text=self.path.read_text()
        body=extract_prose(text)
        self.path.write_text(text.replace(body,'Satu anak menemukan orang koma. Ia pulang.'))
        self.invalid('below draft length')

    def test_outline_table_not_chapter_prose(self):
        text=self.path.read_text().replace('<!-- END PROSE -->','| Bab | Tujuan |\n<!-- END PROSE -->')
        self.path.write_text(text)
        self.invalid('outline/table')

    def test_level_cannot_advance_in_opening(self):
        self.data['manuscript']['chapters'][0]['yazha_level']=1
        self.invalid('level differs')

    def test_no_core_energy_before_installation(self):
        c=self.data['manuscript']['chapters'][0]
        c['core_state']='artificial';c['energy_percent']=100
        self.invalid('Core/energy')

    def test_no_active_technique_for_level0(self):
        self.data['manuscript']['chapters'][0]['active_techniques']=['voidstep']
        self.invalid('active technique')

    def test_date_before_epoch_is_rejected(self):
        self.data['manuscript']['chapters'][0]['date_start']='2084-08-16'
        self.invalid('chronology moves backward')

    def test_year_must_match_opening_card(self):
        c=self.data['manuscript']['chapters'][0]
        c['date_start']=c['date_end']='2085-08-17'
        self.invalid('year differs')

    def test_date_end_before_start(self):
        self.data['manuscript']['chapters'][0]['date_end']='2084-08-16'
        self.invalid('chronology moves backward')

    def test_age_must_match_date_label(self):
        self.data['manuscript']['chapters'][0]['yazha_age']=14
        self.invalid('age mismatches')

    def test_wrong_pov_tag(self):
        self.path.write_text(self.path.read_text().replace('pov=yazha','pov=wiadava'))
        self.invalid('wrong chapter/revision/POV tag')

    def test_undeclared_pov_change(self):
        self.data['manuscript']['chapters'][0]['pov']='maera'
        self.invalid('undeclared POV')

    def test_withheld_identity_is_not_revealed(self):
        self.path.write_text(self.path.read_text().replace('<!-- END PROSE -->','Nama orang itu Aethel Wiadava.\n<!-- END PROSE -->'))
        self.invalid('withheld identity')

    def test_title_mismatch(self):
        self.path.write_text(self.path.read_text().replace('Bab 001 — Porsi','Bab 001 — Ramalan'))
        self.invalid('heading/title mismatch')

    def test_missing_file(self):
        self.path.unlink()
        self.invalid('missing chapter file')

    def test_source_cannot_escape_workspace(self):
        self.data['manuscript']['chapters'][0]['file']='../outside.md'
        self.invalid('Unsafe manuscript path')

    def test_source_must_live_in_manuscript_folder(self):
        with self.assertRaises(ValueError):workspace_path(self.root,'00_CANON_TERKUNCI.md')

    def test_latest_pointer_not_future_claim(self):
        self.data['manuscript']['latest_drafted_chapter']=35
        self.invalid('Latest drafted chapter')

    def test_next_pointer_stays_sequential(self):
        self.data['manuscript']['next_chapter']=9
        self.invalid('Next chapter pointer')

    def test_edition_cannot_contain_unwritten_chapters(self):
        self.data['manuscript']['reading_editions'][0]['end']=35
        self.invalid('undrafted chapters')

    def test_edition_cannot_overwrite_source(self):
        self.data['manuscript']['reading_editions'][0]['file']=self.data['manuscript']['chapters'][0]['file']
        self.invalid('overwrite chapter source')

    def test_next_year_checked(self):
        self.data['manuscript']['next_chapter_year']=2085
        self.invalid('Next chapter year')

    def test_reader_copy_is_deterministic(self):
        e=self.data['manuscript']['reading_editions'][0]
        self.assertEqual(render_edition(self.data,e,self.root),render_edition(self.data,e,self.root))

    def test_story_edit_changes_reader_copy(self):
        e=self.data['manuscript']['reading_editions'][0]
        old=render_edition(self.data,e,self.root)
        self.path.write_text(self.path.read_text().replace('Nala sudah','Nala pagi itu sudah',1))
        self.assertNotEqual(render_edition(self.data,e,self.root),old)

    def test_epoch_age_labels(self):
        ep=date(2084,8,17)
        self.assertEqual(calendar_age(date(2084,8,26),ep,11),11)
        self.assertEqual(calendar_age(date(2085,8,17),ep,11),12)


if __name__=='__main__':unittest.main()
