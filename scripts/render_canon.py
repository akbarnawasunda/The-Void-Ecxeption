#!/usr/bin/env python3
"""Render numeric canon tables. Standard library only; use --check in CI."""
from __future__ import annotations

import argparse
import difflib
import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "00_DATA_KANON.json"
MARKER = re.compile(r"(<!-- BEGIN CANON:([a-z_]+) -->\n)(.*?)(<!-- END CANON:\2 -->)", re.S)


def load_data(path: Path = DATA) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def number(value: int | Fraction) -> str:
    value = Fraction(value)
    if value.denominator == 1:
        return f"{value.numerator:,}".replace(",", ".")
    # Exact rational values are kept in JSON; display rounds to two decimals.
    return f"{float(value):,.2f}".replace(",", "_").replace(".", ",").replace("_", ".").rstrip("0").rstrip(",")


def table(headers: list[str], rows: list[list[object]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines.extend("| " + " | ".join(str(cell) for cell in row) + " |" for row in rows)
    return "\n".join(lines) + "\n"


def level_at(data: dict, chapter: int) -> int:
    matches = [level["id"] for level in data["levels"] if level["yazha_chapters"][0] <= chapter <= level["yazha_chapters"][1]]
    if len(matches) != 1:
        raise ValueError(f"Chapter {chapter}: expected one level, got {matches}")
    return matches[0]


def clock_totals(data: dict) -> list[dict]:
    earth = Fraction(0)
    subjective = Fraction(0)
    out = []
    for volume in data["volumes"]:
        local = sum((Fraction(s["earth_years"]) * data["clock_rates"][s["place"]] for s in volume["segments"]), Fraction(0))
        delta_earth = sum((Fraction(s["earth_years"]) for s in volume["segments"]), Fraction(0))
        earth += delta_earth
        subjective += local
        out.append({"volume": volume["id"], "earth_delta": delta_earth, "earth": earth, "local": local, "subjective": subjective, "age": subjective + data["epoch_yazha_age"]})
    return out


def render_plot(data: dict) -> str:
    body = ""
    for v in data["volumes"]:
        body += f"## V{v['id']}. {v['title']} — bab {v['chapters'][0]}–{v['chapters'][1]}\n\n"
        body += f"**Keinginan:** {v['premise']} **Pilihan inti:** {v['choice']} **Sisa:** {v['aftermath']}\n\n"
        for a in v["arcs"]:
            body += f"### {a['chapters'][0]}–{a['chapters'][1]} · {a['title']}\n\n"
            body += f"**Gerak:** {a['action']}\n\n**Pilihan:** {a['choice']}\n\n**Akibat:** {a['aftermath']}\n\n"
    return body


def render_setup_payoffs(data: dict) -> str:
    body = ""
    for s in data["setup_payoffs"]:
        body += f"### {s['id']} · {s['title']}\n\n"
        body += f"- **Tanam:** bab {', '.join(map(str, s['setup']))}.\n"
        body += f"- **Panen:** bab {', '.join(map(str, s['payoff']))}.\n"
        body += f"- **Yang berubah:** {s['result']}\n\n"
    return body


def render_opening_cards(data: dict) -> str:
    body = ""
    for c in data["volume1_cards"]:
        body += f"### {c['chapter']}. {c['title']} · {c['time']}\n\n"
        body += f"**Keinginan/hambatan:** {c['want_obstacle']}\n\n"
        body += f"**Pilihan/akibat:** {c['choice_result']}\n\n"
    return body


def render_tables(data: dict) -> dict[str, str]:
    totals = clock_totals(data)
    volume_rows = []
    for v, t in zip(data["volumes"], totals):
        a, b = v["chapters"]
        locations = " → ".join(data["place_names"][s["place"]] for s in v["segments"])
        if v["id"] == 14:
            locations += "; Luar Shell hanya bab 1530"
        volume_rows.append([v["id"], f"{a}–{b}", locations, f"{level_at(data,a)}→{level_at(data,b)}", number(t["local"]), number(t["earth_delta"]), number(t["earth"]), number(t["age"])])
    level_rows = [[l["id"], l["name"], "Tidak menua; tetap dapat tewas" if l["lifespan"] is None else number(l["lifespan"]), f"{l['yazha_chapters'][0]}–{l['yazha_chapters'][1]}"] for l in data["levels"]]
    return {
        "plot_arcs": render_plot(data),
        "setup_payoffs": render_setup_payoffs(data),
        "opening_cards": render_opening_cards(data),
        "consequences": table(["Bab", "Jenis", "Sisa yang dibawa"], [[s["chapter"], s["type"], s["entry"]] for s in data["state_ledgers"]]),
        "volumes": table(["Vol", "Bab", "Lokasi Yazha", "Level", "Tahun lokal", "Δ tahun Bumi", "Σ tahun Bumi", "Usia Yazha"], volume_rows),
        "levels": table(["Lv", "Nama", "Batas hayat lokal", "Bab Yazha pada level ini"], level_rows),
        "lesh": table(["#", "Lesh Putih", "Fungsi", "Lokasi", "Mandat disahkan"], [[l["id"], l["name"], l["function"], l["location"], f"V{l['mandate_volume']} · bab {l['mandate_chapter']}"] for l in data["lesh"]]),
        "techniques": table(["Teknik", "Pertama", "Energi dari kapasitas penuh", "Niskala", "Batas paket dasar"], [[t["name"], f"Bab {t['chapter']}", f"{t['energy']:g}%", t["niskala"], t["scope"]] for t in data["techniques"]]),
        "milestones": table(["Peristiwa", "Volume", "Bab", "Arti"], [[e["id"], e["volume"], e["chapter"], e["label"]] for e in data["milestones"]]),
        "deaths": table(["Nama", "Volume", "Bab", "Kejadian aktual"], [[e["name"], e["volume"], e["chapter"], e["cause"]] for e in data["deaths"]]),
        "clock_rates": table(["Tempat", "Tahun lokal per tahun Bumi"], [[data["place_names"][p], rate] for p, rate in data["clock_rates"].items()]),
        "friends": table(["Akhir volume", "Σ tahun Bumi", "Bhas/Yuna jika masih hidup", "Nala: usia biologis", "Catatan"], [[t["volume"], number(t["earth"]), number(Fraction(11)+t["earth"]) if t["volume"] == 1 else number(Fraction(14)+3*(t["earth"]-3)), "6" if t["volume"] == 1 else "6→8: sesi bangun total 2 tahun" if t["volume"] < 5 else number(Fraction(8)+3*(t["earth"]-totals[4]["earth"])), "Bhas telah mati" if t["volume"] in (11,12) else "Keduanya telah mati" if t["volume"] >= 13 else "Bumi Abadi sejak invasi" if t["volume"] >= 2 else "Invasi"] for t in totals]),
    }


def block(name: str, data: dict | None = None) -> str:
    tables = render_tables(data or load_data())
    return f"<!-- BEGIN CANON:{name} -->\n{tables[name]}<!-- END CANON:{name} -->\n"


def replace_blocks(text: str, tables: dict[str, str]) -> str:
    def replacement(match: re.Match[str]) -> str:
        name = match.group(2)
        if name not in tables:
            raise ValueError(f"Unknown canon table: {name}")
        return match.group(1) + tables[name] + match.group(4)
    return MARKER.sub(replacement, text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail instead of writing stale tables")
    args = parser.parse_args()
    tables = render_tables(load_data())
    stale = []
    count = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(p in {".git", ".arena", "node_modules", ".cache", ".venv"} for p in path.parts):
            continue
        original = path.read_text(encoding="utf-8")
        if "<!-- BEGIN CANON:" not in original:
            continue
        count += len(MARKER.findall(original))
        rendered = replace_blocks(original, tables)
        if rendered != original:
            stale.append(path.relative_to(ROOT))
            if args.check:
                print("".join(difflib.unified_diff(original.splitlines(True), rendered.splitlines(True), fromfile=str(path), tofile="expected")))
            else:
                path.write_text(rendered, encoding="utf-8")
    if args.check and stale:
        print(f"FAIL: {len(stale)} stale documents. Run python3 scripts/render_canon.py")
        return 1
    print(f"OK: {count} canon tables; {'checked' if args.check else 'rendered'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
