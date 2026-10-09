# Naskah Utama — Volume 1

<!-- canon:v5 -->
**Status: draf 1.** Kontrak tetap [V5](../00_CANON_TERKUNCI.md); tanggal/bab yang sudah ditulis tercatat pada `manuscript` dalam [data kanon](../00_DATA_KANON.json).

## Baca ceritanya

**[Bab 001–008 dalam satu berkas](01_Baca_Volume_01_Bab_001_008.md)** — satu arc pembuka utuh: rumah, teman, gempa Halimun, pertolongan pasien, dan prasasti yang belum dapat diterjemahkan.

Ini prosa bab lengkap, bukan kartu adegan. Volume 1 baru **8 dari 35 bab**; seri utama baru **8 dari 1.530 bab**. Jangan menganggap folder yang belum dibuat sebagai naskah yang sudah selesai.

## Sumber per bab

| Bab | Judul | Tanggal cerita | Sumber |
| --- | --- | --- | --- |
| 001 | Porsi | 17 Agustus 2084 | [Bab 001](V01_Rumah_Yang_Belum_Hilang/001_Porsi.md) |
| 002 | Baut | 18 Agustus 2084 | [Bab 002](V01_Rumah_Yang_Belum_Hilang/002_Baut.md) |
| 003 | Gempa | 19 Agustus 2084 | [Bab 003](V01_Rumah_Yang_Belum_Hilang/003_Gempa.md) |
| 004 | Orang Terlalu Berat | 19 Agustus 2084 | [Bab 004](V01_Rumah_Yang_Belum_Hilang/004_Orang_Terlalu_Berat.md) |
| 005 | Perawatan di Tempat | 20 Agustus 2084 | [Bab 005](V01_Rumah_Yang_Belum_Hilang/005_Perawatan_Di_Tempat.md) |
| 006 | Harga Bantuan | 21 Agustus 2084 | [Bab 006](V01_Rumah_Yang_Belum_Hilang/006_Harga_Bantuan.md) |
| 007 | Nomor yang Tidak Cocok | 23 Agustus 2084 | [Bab 007](V01_Rumah_Yang_Belum_Hilang/007_Nomor_Yang_Tidak_Cocok.md) |
| 008 | Batu | 26 Agustus 2084 | [Bab 008](V01_Rumah_Yang_Belum_Hilang/008_Batu.md) |

[Catatan editor/kesinambungan](02_Catatan_Arc_Pembuka.md) terpisah dari berkas baca; berisi rincian yang dapat mengganggu pembacaan pertama.

## Cara mengedit

Edit sumber per bab, di dalam penanda `BEGIN PROSE` dan `END PROSE`. Ubah tanggal, kondisi, atau pengetahuan pada data bila adegan berubah. Berkas baca adalah salinan terbitan yang dapat dibuat ulang, **bukan sumber kedua untuk ditambal**.

```sh
python3 scripts/render_manuscript.py
python3 scripts/render_manuscript.py --check
python3 scripts/render_canon.py --check
python3 scripts/check_canon.py
python3 -m unittest discover -s tests -v
```

Pemeriksa menguji deklarasi kondisi, tanggal, urutan, identitas yang belum diungkap, kelengkapan berkas, panjang minimum draf, dan kesamaan salinan. Ia tidak memahami seluruh semantik prosa atau menjamin kualitas sastra. Pemeriksaan POV, motivasi, ritme, dan plausibilitas tetap kerja editor.

## Titik sambung berikutnya

Bab **009 — Jalan sekolah** memasuki **2085**, sesuai kartu V1. Bukan pagi setelah bab 008. Rawat perkembangan keluarga, perawatan Wiadava, sekolah, serta biaya waktu di antara dua tahun; jangan menggunakan time-skip untuk memberi Core atau menambah keahlian mendadak.
