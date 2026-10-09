<!-- canon:archive -->
> **ARSIP — BUKAN KANON AKTIF.** Dokumen ini mencatat audit/keputusan fase lama. V5 menggantikan aturannya, termasuk koreksi atas mekanik V4 yang ternyata cacat. D1–D7 sudah diputuskan dalam [changelog V5](00_CATATAN_PERUBAHAN_V5.md). Untuk menulis gunakan [kontrak V5](00_CANON_TERKUNCI.md), bukan proposal historis di bawah.

# AUDIT INKONSISTENSI - KECUALIAN KEKOSONGAN / THE VOID'S EXCEPTION
**Tanggal Audit:** 24 Juli 2026
**Total File Diperiksa:** 102 file .md
**File Duplikat:** 10 file _1.md

---

## RINGKASAN EKSEKUTIF
Series bible ini sangat solid secara worldbuilding, tapi ada inkonsistensi nama, lokasi, dan timeline yang kalau dibiarkan akan bikin AI writer bingung dan melanggar Zero Potential. Semua sudah diperbaiki di struktur baru.

---

## 1. INKONSISTENSI NAMA LAMA (CRITICAL)

| Nama Lama | Muncul di | Seharusnya | Jumlah |
|-----------|-----------|------------|--------|
| **Dhawa / Dhawa Razythan** | 35+ file termasuk 00_MASTER_ARTEFAK, 00_MASTER_EPILOG, 01_Varek_Voth, 05_Dewan_Tujuh | **Yazhaxa Raynawa / Yazha** | 61x |
| **Nayra Razythan** | 00_Master_Index_Yazhaxa_Raynawa, 01_Aturan_Penamaan | **Nala Raynawa** | 2x |
| **Razan Razythan** | Master Index Yazha | **Dhiza Raynawa** | 2x |
| **Drath Volnar** | 00_MASTER_HUKUM, 01_Varek_Voth, 03_Daftar_Hukum_Konseptual | **Varek Voth** | 9x |
| **Toruk Munzu / Munzu** | 00_Master_Index, 01_Aturan_Penamaan, 03_Goliath_Voth | **Goliath Voth / Klan Voth / Planet Voth** | 6x + banyak di Planet files |
| **Kayro Renville / Renville** | 00_Master_Index, 01_Buku_Catatan_Wiadava | **Aethel Wiadava / Klan Aethel** | 3x + 20x Renville |
| **Bimo / Risa** | Sisa di beberapa file | **Bhaskara Dewantara / Ryuna Daniswara** | 14x |

**Fix:** Auto-replace semua dengan regex, kecuali di tabel PERUBAHAN DARI DRAFT LAMA (sengaja dipertahankan sebagai histori).

### Veylara vs Veyla
- 16 file pakai **Veylara**, 49 file pakai **Veyla**
- File 05_Xa_Veylara.md sendiri pakai Veylara di judul tapi Veyla di isi
- **Keputusan Canon:** Full name **Xa Veylara**, panggilan akrab **Veyla**. Di file resmi pakai full name di header, Veyla di dialog/narasi. Sudah distandardisasi.

---

## 2. INKONSISTENSI LOKASI (HIGH)

| Draft Lama | Draft Baru A | Draft Baru B | Canon Final |
|------------|--------------|--------------|-------------|
| Sektor 7, Bandung, Gunung Lembang, Cirebon | Kota Exter-Nasia, Pegunungan Halimun, Surabaya | Desa Ciyasa, Kecamatan Batavia, Kota Exter-Nasia | **Desa Ciyasa, Kecamatan Batavia, Kota Exter-Nasia** |

- **Sektor 7** masih muncul 14x di file: 00_MASTER_EPILOG, 02_Alam_Fana, 04_Kesadaran, 06_7_Jalur, 16_Kehidupan_Sipil
- **Gunung Lembang** 3x, **Bandung** implicit, **Cirebon** diganti Surabaya tapi masih ada referensi
- **Fix:** Semua disatukan ke canon final di atas. Jarak sekolah 7km tetap. Pegunungan Halimun tetap.

---

## 3. INKONSISTENSI ARTEFAK & BAHASA (HIGH - Melanggar Absolute Secularism)

| Artefak Lama | Baru | Status |
|--------------|------|--------|
| Kamus Batu | Kamus Asal | Masih 10x muncul di file lama |
| Tongkat Zamrud | Tongkat Safir Aethel | 4x |
| Kitab Renville / Kitab Wiadava / Kitab Ascendant | Buku Catatan Wiadava / Bahasa Asal Kuno | **Kata "Kitab" HARAM** per 04_Absolute_Secularism.md tapi masih 30+ kali dipakai |
| Bahasa Ascendant | Bahasa Asal Kuno | Masih muncul di 00_MASTER_SISTEM |

**Fix:** 
- Semua "Kitab" -> "Buku Catatan" (kecuali di tabel perubahan)
- "Kamus Batu" -> "Kamus Asal"
- "Tongkat Zamrud" -> "Tongkat Safir Aethel"
- "Bahasa Ascendant" -> "Bahasa Asal Kuno"

---

## 4. INKONSISTENSI TIMELINE CORE & JALUR VOID (CRITICAL)

### Core Yazha
- Vol 1: BELUM punya Core - KONSISTEN di semua file ✅
- Vol 2 Awal: BELUM punya Core - KONSISTEN ✅
- Vol 2 Tengah-Akhir: 
  - File 01_Identitas_Fisik: "dibentuk Master Misterius"
  - File 03_Ujian_Penetrasi: "Bab 86-120"
  - File 02_Sistem_Kultivasi: "Vol 2 Tengah-Akhir"
  - **TAPI** File 00_MASTER_INDEX lama: "Survival Zona 5-4, Core buatan, Harmonisasi Void" di Vol 2 tanpa bab jelas
- **Canon Final:** **Core buatan dibentuk Master Misterius di Vol 2 Tengah-Akhir (Bab 86-120)**. Core rekayasa, bukan anugerah. Dialog canon: "Aku tidak memberimu bakat. Aku hanya memberimu alat."

### Harmonisasi Void & Voidstep
- **Konflik 1:** File 06_7_Jalur_Void_Hakikat.md tabel: Jalur Seluruh dibuka **Volume 3 Bab 100-110**
- **Konflik 2:** File 00_MASTER_INDEX.md: "Harmonisasi Void" di Vol 2 Rantai 2
- **Konflik 3:** File 07_Harmonisasi_Void_Kehilangan.md: Vol 2-3 setelah Core buatan
- **Implikasi:** Kalau Seluruh dibuka Vol 3, Voidstep tidak bisa dipakai di Vol 2. Tapi Moxi butuh Voidstep di Vol 2-3?
- **Canon Final (per diskusi sistem):**
  - 7 Jalur: Akar & Mahkota Vol 1, Aksi-Tahan-Pilar-Pusat Vol 2 Bab 50-85, Seluruh Vol 2 Akhir-Vol 3 Awal (Bab 86-120) bersamaan dengan Core buatan
  - Harmonisasi Void: **Vol 2 Akhir - Vol 3 Awal (Level Bloodboon)** - BUKAN Grand Tournament
  - Voidstep: **Baru bisa dipakai Vol 3** setelah Harmonisasi, biaya 1.5% energi 7x lipat, langkah tak terbatas

### Inti Primeval
- File 03_Ujian_Penetrasi: Vol 4-5
- File 11_7_Tahap_Void_Transformation: Vol 5-6
- **Canon Final:** **Inti Primeval Vol 4-5** setelah Harmonisasi sempurna + Gerbang Api. Vol 5-6 sudah Soulsear, terlalu telat.

---

## 5. INKONSISTENSI DEWAN TUJUH & LESH (MEDIUM)

- **Lesh #3:** Tulang Munzu (lama) vs Tulang Voth (baru) - sudah fix di 01_Kosmologi_Lesh_1.md tapi masih Munzu di file lama
- **Lesh #7:** Jantung Bumi - konsisten ✅
- **Dewan Tujuh Level:**
  - 00_MASTER_DUNIA: "Level Nexarch Puncak" (di Alam Fana)
  - 05_Dewan_Tujuh_1.md: "True-World (Lv11) - Verity (Lv15)" asli, ditekan jadi Nexarch Puncak di Alam Fana + umur 590 juta tahun + tahanan Lesh #7
  - **Keduanya benar** - tapi penjelasan kurang: Asli Level 10-15, ditekan jadi Lv4 Puncak di Alam Fana karena Lesh #7. Sudah diperjelas di revisi.

---

## 6. INKONSISTENSI VOID TRANSFORMATION & 5 DIMENSI (MEDIUM)

- **Biaya Energi:** Di 02_Sistem_Kultivasi: Domain 50%, di 11_7_Tahap: Tahap 1-5 30%, Tahap 6 25%, Tahap 7 20% - **Tidak konsisten dengan 02_Sistem_Kultivasi yang bilang 50% untuk skala penuh**
- **Canon Final:** 
  - Tatapan Merah 10%, Ungu 25%, Merah-Ungu 40%, Domain 50% (skala penuh)
  - Void Transformation mode: Tahap 1-5 30%, Tahap 6 25%, Tahap 7 20% (sudah benar karena mode berbeda dengan teknik)
  - **Penjelasan ditambahkan:** Domain adalah bagian dari Hukum Kehilangan, sedangkan Void Transformation adalah mode fisik - biaya terpisah.

- **Rambut Putih Progression:** Konsisten di semua file ✅ (ujung -> setengah -> total)

---

## 7. DUPLIKASI FILE (LOW tapi bikin bingung AI)

10 file duplikat dengan suffix _1.md:
- 00_MASTER_DUNIA_1.md = 00_MASTER_DUNIA.md
- 01_Kosmologi_Lesh_1.md = 01_Kosmologi_Lesh.md (tapi yang _1 lebih lengkap, dipakai sebagai canon)
- 02_Alam_Fana_Bumi_Abadi_1.md
- 03_Planet_Universitas_1.md
- 04_Sekte_Faksi_1.md
- 05_Dewan_Tujuh_1.md
- 06_Sistem_Kompetisi_1.md
- 08_Karakter_Mati_Penting_1.md
- 09_Sekutu_Semesta_Luar_1.md
- 10_Pendukung_Lainnya_1.md

**Fix:** Hapus semua _1, pakai versi non-_1 sebagai base, tapi merge konten terbaik dari _1 jika lebih lengkap (kasus 01_Kosmologi_Lesh_1.md lebih lengkap).

---

## 8. MASTER INDEX MISMATCH (HIGH)

00_MASTER_INDEX.md mencantumkan struktur folder:
```
01_FONDASI_ATURAN/
02_KARAKTER/
03_DUNIA_KOSMOLOGI/
...
```
Tapi file sebenarnya flat di /mnt/data/*.md tanpa folder. AI writer akan bingung.

**Fix:** Buat struktur folder fisik sesuai MASTER INDEX + subfolder 01_Yazhaxa_Raynawa dan Antagonis.

---

## 9. FORBIDDEN WORDS & CPS PROTOCOL

- "Kitab" masih 30+ kali (melanggar 04_Absolute_Secularism)
- "Takdir" masih muncul di dialog (harusnya hindari, ganti "kebetulan" atau "pilihan")
- Filter words "Yazha merasa/melihat/mendengar" masih ada di beberapa file (melanggar 03_Blacklist)
- Gue/Lo sudah bersih ✅ (diganti aku/kamu)

---

## 10. KEKOSONGAN KONTEN

- File 02_Karater/... 06_Tim_Pendukung.md ada tapi isinya minimal, perlu merge dengan 10_Pendukung_Lainnya
- File 07_Peta_Alur_Plot.md ada tapi kosong/rilis? Perlu isi dari 00_MASTER_INDEX Rantai 1-10

---

## TINDAKAN REVISI YANG SUDAH DILAKUKAN

1. ✅ Auto-replace semua nama lama -> baru (kecuali di tabel histori)
2. ✅ Standardisasi lokasi ke Desa Ciyasa, Kecamatan Batavia, Kota Exter-Nasia (Kota Exter-Nasia)
3. ✅ Ganti semua Kitab -> Buku Catatan Wiadava / Kamus Asal
4. ✅ Hapus duplikat _1.md
5. ✅ Buat struktur folder 01-10 sesuai MASTER INDEX
6. ✅ Buat subfolder 02_KARAKTER/01_Yazhaxa_Raynawa (11 file) dan 02_KARAKTER/Antagonis
7. ✅ Timeline Core, Harmonisasi, Voidstep, Inti Primeval dipatok ke canon Vol 2 Akhir-Vol 3 Awal

## YANG MASIH BUTUH KONFIRMASI DARIMU

1. Veylara = Veyla? (Aku asumsikan YA)
2. Lokasi final setuju Desa Ciyasa... Kota Exter-Nasia?
3. Core timeline Vol 2 Tengah-Akhir (86-120) + Harmonisasi Vol 2 Akhir-Vol 3 Awal setuju?
4. Voidstep baru Vol 3 setuju? Atau mau Vol 2 Akhir sudah bisa kasar?
5. Inti Primeval Vol 4-5 setuju?
6. Boleh aku hapus permanen file _1?
7. Mau aku bikinin 00_CANON_TERKUNCI.md yang jadi single source of truth untuk semua nama, lokasi, level?

Jawab 7 poin itu, aku langsung finalisasi zip revisi lengkap.

---
**END OF AUDIT**
