# The Void’s Exception — Series Bible V5

<!-- canon:v5 -->
**Kanon aktif: V5.0 — 9 Oktober 2026.** [Kontrak utama](00_CANON_TERKUNCI.md).

Rewrite aktif V5: dunia dark cultivation dengan sebab-akibat yang dapat diperiksa dan tokoh yang mempunyai pilihan di luar ambisi protagonis. Semua pengembangan seri utama mengikuti 14 volume/1.530 slot bab. **Repository ini bible dan cetak biru, bukan naskah penuh 1.530 bab.**

## Jalur baca

1. [Ringkasan rewrite](00_RINGKASAN_REWRITE_V5.md)
2. [Kontrak kanon](00_CANON_TERKUNCI.md)
3. [Peta plot](07_PETA_ALUR_PLOT/07_Peta_Alur_Plot.md)
4. [Mesin emosi](01_FONDASI_ATURAN/06_Mesin_Emosi_Dan_Prosa.md) dan [tujuh adegan uji](11_NASKAH_UJI/01_Tujuh_Adegan_Kunci.md)
5. [Changelog dan veto](00_CATATAN_PERUBAHAN_V5.md)
6. [Indeks seluruh bible](00_MASTER_INDEX_FINAL.md)

## Kontrak ringkas

Yazha manusia biasa; bantuan/alat tidak berarti takdir khusus. Harga Hukum terukur, tidak menagih kematian keluarga acak. Lesh adalah infrastruktur yang tetap terpasang. Bhas/Yuna tetap fana. Ending keluarga lengkap adalah penglihatan; aktual Shell→amnesia. Tidak ada pemutaran sejarah atau kebangkitan sebagai hadiah.

Jam:39 tahun Bumi 2084→2123;4.016,6 tahun lokal Yazha; usia akhir 4.027,6. Data menghitung kunjungan kembali, bukan menebak dari rata-rata.

## Merawat sumber kebenaran

- `00_DATA_KANON.json`: angka, range, milestone, kartu arc,35 kartu V1, 18 setup, serta anggaran sekuel.
- `00_CANON_TERKUNCI.md`: makna dan batas; dokumen turunannya memberi contoh/kondisi.
- Blok `BEGIN CANON` **dihasilkan otomatis**. Edit data lalu render, jangan menambal salinan tabel/plot satu per satu.
- Perubahan peristiwa/aturan dicatat di changelog beserta dependensi. Prosa di luar blok dapat diedit langsung, tetapi harus dibaca ulang terhadap kontrak.
- Audit/changelog V1/V3/V4 bertanda **arsip**, bukan sumber aturan. Versi sebelum rewrite dapat dilihat di Git `c1de254`.

## Validasi lokal — tanpa dependency tambahan

```sh
python3 scripts/render_canon.py
python3 scripts/render_canon.py --check
python3 scripts/check_canon.py
python3 -m unittest discover -s tests -v
git diff --check
```

Pemeriksa mempunyai **52 regresi**, termasuk data/doc korup: salah jam, arc bertabrakan, node kedua belas, VT sebelum level, stasis tanpa hitungan, anak penglihatan dianggap aktual, tautan rusak, dan kondisi kematian. Workflow GitHub menjalankan pemeriksaan yang sama; belum berarti quality sastra telah “lulus mesin”.

**Batas pemeriksa:** struktur/angka/status dan konsistensi salinan. Ia tidak memahami seluruh semantik prosa atau menjamin setiap adegan menyentuh. Gunakan checklist pilihan, sumber pengetahuan, alternatif, harga, dan aftermath untuk review editorial.

## Arsip

[Audit V3](00_AUDIT_CELAH_V3.md), [changelog V4](00_CATATAN_PERUBAHAN_V4.md), [audit awal](00_INKONSISTENSI_AUDIT.md). Jangan menerapkan proposal lama sebagai mekanik aktif.
