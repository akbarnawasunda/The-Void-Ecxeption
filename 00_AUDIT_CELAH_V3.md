# AUDIT CELAH V3 — KECUALIAN KEKOSONGAN / THE VOID'S EXCEPTION

**Tanggal audit:** 9 Oktober 2026
**Yang diaudit:** 102 file `.md` / `.txt` (seluruh series bible)
**Status:** Audit ini **bukan** perbaikan. Ini daftar celah + rekomendasi keputusan.
**Catatan:** Audit V1 (`00_INKONSISTENSI_AUDIT.md`, 24 Juli 2026) berhasil beresin masalah **nama & lokasi**. Audit V3 ini nemuin masalah yang **lebih gawat**: timeline, skala kekuatan, dan slot plot.

---

## VERDIK

> **Worldbuilding-nya kuat. Tapi "pipa"-nya bocor.**
> Nama, lokasi, artefak, dan aturan gaya sudah rapi. Yang bermasalah adalah **angka-angka yang saling tabrak antar file** — dan karena `00_CANON_TERKUNCI.md` dinyatakan *single source of truth*, setiap file yang melenceng jadi bom waktu buat AI writer.

**Yang paling gawat bukan "ada yang beda", tapi "ada yang hilang":**
`Dewan Tujuh` disebut di **16 file**, muncul di peta alur **0 kali**.
`Moxi` punya file profil 8.700 karakter + arc moral 3 volume, muncul di peta alur **1 kali**.
`Goliath Voth` (pembantai Klan Aethel = motif utama Wiadava) **nggak punya adegan kematian**.
11 Lesh dikumpulin di Vol 7, **nggak pernah dipakai**.

---

# TIER 0 — FATAL
*Kalau ini nggak diberesin, novelnya kacau secara struktural. Nggak bisa ditambal saat nulis.*

---

## ❌ T0-1. Yazha tembus Level 17 dalam ~50 tahun, padahal setting-nya bilang butuh 10.000–20 miliar tahun

**Ini celah terbesar di seluruh bible.**

| Entitas | Waktu tempuh | Level akhir | Sumber |
|---|---|---|---|
| Aethel Wiadava (**jenius sejati**) | 10.000 tahun | Level 8 Puncak | `02_Aethel_Wiadava.md:9,112` |
| Varin Astralis | 100.000+ tahun | Level 9 (atau 10) | `02_Aethel_Wiadava.md:112` |
| Penguasa Hampa | berdiri di Dinding 3 **3 miliar tahun**, nggak pernah lompat | gagal di Level 16 | `10_Tiga_Dinding_Unbegotten.md` §3 |
| The First Exception | 20 miliar tahun | Level 17 | `11_Entitas_Step_4.md:52` |
| Dewan Tujuh | 590 juta tahun | ditekan jadi Level 4 Puncak | `00_CANON_TERKUNCI.md:121` |
| **Yazhaxa Raynawa (zero bakat)** | **~50 tahun** | **Level 17** | lihat bawah |

**Kenapa ~50 tahun? Karena 3 jangkar ini ngunci timescale-nya:**

1. `13_Kecepatan_Kultivasi_Per_Karakter.md` — Level 0→5 = 3 + 0,5 + 1 + 1,5 + 2 = **8 tahun**. Yazha (11 tahun di 2084) nyampe Level 5 di usia **~19 tahun (~2091)**.
2. `09_EPILOG/01_Akhir_Cerita.md` §4 — Dhiza & Vaniya diselamatkan tahun 2087, **meninggal alami di usia 90**. Berarti epilog maksimal **~2137**. Jarak 2087→2137 = **50 tahun**.
3. `03_Nala_Raynawa.md:29` — Nala 5–6 tahun saat diculik (2087), lalu **jadi antagonis Vol 3–5** dan diselamatkan Vol 6. Kalau Vol 3–5 itu ribuan tahun kemudian, Nala udah jadi debu.

**TAPI** `01_FONDASI_ATURAN/05_Struktur_Volume_Pacing.md:57` bilang:

> *"Sisanya: Tidak usah ditulis tahun spesifik. Cukup 'ribuan tahun' atau 'jutaan era' untuk perjalanan selanjutnya."*

→ **Dua timescale yang mutually exclusive, dua-duanya ada di bible.**
→ Kalau pilih "ribuan tahun": epilog, Nala, Bhaskara, Ryuna hancur.
→ Kalau pilih "50 tahun": power scale-nya pincang — anak miskin zero bakat ngalahin jenius 10.000 tahun dan entitas 20 miliar tahun, tanpa penjelasan.

### Rekomendasi
**Pilih salah satu, dan tulis aturannya:**

- **Opsi A (Recommended — "Lonceng Waktu"):** Pertahankan timescale pendek (~50–80 tahun), tapi **tambahkan aturan in-universe** yang bikin Yazha beda: Jalan Aseity + Hukum Kehilangan membuat *kemajuan Yazha diukur dari kedalaman kehilangan, bukan dari umur*. Semakin banyak yang ia renggut dari dirinya, semakin cepat naik. Wiadava/Varin lambat karena mereka **nggak pernah mau kehilangan apa pun**. Ini justru *menguatkan* tema dan Zero Potential.
- **Opsi B:** Naikin timescale jadi ribuan tahun, tapi ubah epilog: Dhiza & Vaniya harusnya ikut berkultivasi (batal "meninggal di usia 90"), Nala jadi antagonis dewasa, Bhaskara/Ryuna harus dijelasin umur panjangnya.
- **Opsi C:** Hapus kalimat "ribuan tahun / jutaan era" dari `05_Struktur_Volume_Pacing.md:57`.

**Yang wajib:** tulis **1 tabel "Usia Yazha & tahun per Volume"** di `00_CANON_TERKUNCI.md`. Sekarang nggak ada.

---

## ❌ T0-2. Varin Astralis mati di Volume 7 atau Volume 9? (Dan Goliath Voth nggak punya slot mati)

| Sumber | Varin mati | Goliath mati |
|---|---|---|
| `00_CANON_TERKUNCI.md:70-71` | **Volume 9** (Yazha Lv 9 Puncak) | **Volume 7** (Yazha Lv 7 Puncak) |
| `07_Peta_Alur_Plot.md:144` (7.5) | **Volume 7** | ❌ **tidak ada** |
| `07_Peta_Alur_Plot.md:113` (5.6) | — | Goliath cuma muncul, Yazha "hampir mati tapi lolos" |
| `01_Yazha/10_Arc_Karakter_per_Volume.md` | **Volume 7** — *"Bunuh Varin. Tapi tidak merasa apa-apa."* | ❌ tidak ada |
| `04_SISTEM_KULTIVASI/02_17_Level_Detail.md:112` | Level 8 dicapai *"Volume 7 — setelah perang melawan Varin"* → **Vol 7** | — |
| `01_Yazha/08_Progresi_Kekuatan_Timeline.md` | Vol 7 = Lv 7-8, Vol 8 = Lv 9-10 → Varin (Lv 9–10) mati **Vol 7–8** | — |

**Dampak:**
- **CANON adalah outlier.** 3 file bilang Vol 7, 1 file (CANON) bilang Vol 9. Karena CANON dinyatakan *single source of truth*, AI yang nurut CANON akan nulis Varin masih hidup di Vol 7–8 — padahal plot Rantai 7 klimaksnya adalah pembunuhan Varin.
- **Goliath Voth nggak punya adegan kematian di mana pun.** Padahal dia pembantai Klan Aethel (`02_Aethel_Wiadava.md:222`), dendam utama Wiadava, dan CANON nge-lock kematiannya di Vol 7. **Motif Wiadava nggak pernah lunas.**
- Vol 9 di peta alur udah penuh: Gerbang Kesepian + Gerbang Nameless + masuk Alam Keabadian. Nggak ada ruang buat Varin.

### Rekomendasi
1. **Ubah `00_CANON_TERKUNCI.md:71`** → Varin mati **Volume 7**, Yazha **Level 8 Puncak**, di Alam Bintang/Kekosongan (sesuai plot + arc + level file).
2. **Bikin arc kematian Goliath di Vol 7** (sebelum Varin). Dia "tangan kanan", jadi dia harus mati duluan. Ini juga jadi **pembayaran motif Wiadava** yang selama ini menggantung.
3. Atau, kalau mau Varin tetap Vol 9: **rombak Rantai 7 & 8** jadi bukan tentang Varin.

---

## ❌ T0-3. Tabel level di `02_17_Level_Detail.md` butuh 1800+ bab, plot cuma 1530

`04_SISTEM_KULTIVASI/02_17_Level_Detail.md` punya **TIGA** versi progresi yang saling tabrak:

**A. Tabel akhir (baris 286–310):**

| Baris | Bab | Level |
|---|---|---|
| 298 | 1321-1360 | **13 Awal** (Nameless) |
| 303 | 1521-1560 | **14 Puncak** |
| 310 | **1801+** | **17 Unbegotten** |

**B. "Waktu Dicapai" di tiap level (baris 24–232):** Level 16 dicapai Vol 12-13, Level 17 dicapai **Vol 14 (1441-1530)** ✓ sesuai plot.

**C. Label volume-nya geser mulai Level 10:**

| Level | Yang tertulis | Bab yang tertulis | Volume asli bab itu |
|---|---|---|---|
| 10 | "Volume 8" | **841-960** | Vol **9** ❌ |
| 11 | "Volume 9" | **841-960** | Vol **9** — **range bentrok dgn Level 10** ❌ |
| 12 | "Volume 9" | **961-1080** | Vol **10** ❌ |
| 13 | "Volume 10" | **961-1080** | Vol **10** — **range bentrok dgn Level 12** ❌ |

**Dampak:** Di **bab terakhir cerita (1530)**, Yazha adalah:
- Level **17 Unbegotten** menurut `08_Progresi` + `10_Tiga_Dinding` + plot map ✅
- Level **14 Puncak** menurut `02_17_Level_Detail.md:303` ❌

Dan tabel A butuh **1801+ bab**, artinya ceritanya kurang **~270 bab / ~2,5 volume**.

**Ini tabel yang paling sering dibaca AI buat nentuin "Yazha lagi Level berapa di bab ini". Kalau ini salah, seluruh cerita ngaco dari Vol 13.**

### Rekomendasi
- **Hapus atau tulis ulang total tabel baris 286–310.** Ganti dengan tabel yang bab-nya mentok di 1530 dan Level 17 dicapai di 1441-1480 (sesuai `10_Tiga_Dinding_Unbegotten.md` §3).
- **Perbaiki range bab yang dobel** (841-960 dipakai Level 10 & 11; 961-1080 dipakai Level 12 & 13).

---

## ❌ T0-4. Urutan Alam & Gerbang Transisi geser 1–2 volume

| Sumber | Kapan Yazha masuk Alam Kekosongan (Lv 9–12) | Kapan Gerbang Kesepian (8→9) |
|---|---|---|
| `00_CANON_TERKUNCI.md:99` | — | **Vol 9, bab 841-880** |
| `07_Peta_Alur_Plot.md:140` (7.1) | **Vol 7 (601-720)**: *"Yazha masuk Alam Kekosongan"* | — |
| `07_Peta_Alur_Plot.md:150` (Rantai 8) | **Vol 8 (721-840)**: judulnya *"ALAM KEKOSONGAN — Ordo Primordium"* | — |
| `07_Peta_Alur_Plot.md:167` (9.1) | — | **Vol 9** |
| `01_Yazha/08_Progresi` | Vol 8 = Lv 9-10 → **Vol 8** | Vol 8 ❌ |
| `02_17_Level_Detail.md:128` | Level 9 dicapai **Vol 8 (721-840)** → **Vol 8** | Vol 8 ❌ |

**Peta alur sendiri tabrak:** Rantai 7 & 8 bilang Yazha **sudah di Alam Kekosongan**, tapi Rantai 9 baru bilang dia **lewat gerbang masuk Alam Kekosongan**. Kalau Alam Kekosongan = Level 9–12 dan dia baru Lv 8 di Vol 7 (`08_Progresi`: Vol 7 = Lv 7-8), dia nggak mungkin udah di sana.

**Dampak berantai:**
- Kapan Yazha pindah alam → ngambang
- Di alam mana Varin mati → ngambang
- Kapan ketemu Ordo Primordium → ngambang
- Vol 8 judulnya "Alam Kekosongan" tapi isinya bisa jadi masih Alam Bintang

### Rekomendasi
Tulis **1 tabel "Alam per Volume"** di CANON, misal:

| Volume | Alam | Level |
|---|---|---|
| 1-2 | Fana | 0-2 |
| 3-4 | Fana | 2-4 |
| 5-7 | **Bintang** | 5-8 |
| 8-9 | **Kekosongan** | 9-12 |
| 10-12 | **Keabadian** | 13-16 |
| 13-14 | — (Tiga Dinding) | 16→17 |

Lalu samakan: **Gerbang Kesepian = Vol 8 bab 721-780** (bukan Vol 9), dan **Rantai 7.1 diubah** jadi *"Yazha menyeberang ke wilayah terluar Alam Bintang"* bukan *"masuk Alam Kekosongan"*.

---

# TIER 1 — BESAR
*Nggak bikin cerita runtuh, tapi bikin pembaca berhenti baca atau nanya "kok bisa?"*

---

## ⚠️ T1-1. Paradoks epilog: Yazha nggak pernah ketemu Veyla di timeline baru

`09_EPILOG/01_Akhir_Cerita.md` §2 — setelah waktu diputar ke 17 Agustus 2087:
> *"Yazha menghentikan invasi Varin Astralis di masa depan sebelum Veyla tersentuh ancaman. **Veyla selamat dan hidup bersama Yazha.**"*

Terus mereka **menikah, punya Akasa & Kanavi**.

**Masalah:** Veyla ketemu Yazha di `05_Xa_Veylara.md:180` —
> *"Bumi Abadi, Zona 3 (Kota Arus), **pelelangan bawah tanah**."*

Yazha ada di Bumi Abadi **karena invasi 2087** (`07_Peta_Alur_Plot.md:46`). Kalau invasi dicegah → Yazha nggak pernah lari ke portal → nggak pernah ke Bumi Abadi → **nggak pernah ketemu Veyla**.

Ini **ending utama novel**. Belum ada penjelasannya di file mana pun.

### Rekomendasi di `01_Akhir_Cerita.md`
Tambahkan 1 paragraf: Yazha **memilih untuk tidak mencegah pertemuan itu** — karena dia sadar kalau dia hapus perjalanannya, dia hapus juga alasan dia mencintai mereka. Atau: dia yang *mencari* Veyla secara sadar di timeline baru, karena itu satu-satunya hal yang ia minta dari keabadian.

---

## ⚠️ T1-2. Epilog seri utama TABRAKAN LANGSUNG dengan Sekuel

| | Seri Utama (`09_EPILOG`) | Sekuel (`08_CETAK_BIRU_SEKUEL`) |
|---|---|---|
| Kapan nembus The Shell | Sudah di luar The Shell di Vol 14 | **Baru** nembus setelah Unbegotten |
| Kondisi Yazha | Pengamat Multiverse, damai, lihat keluarganya | **Amnesia total**, lupa keluarga, sendiri |
| Ingatan | Cuma memori sensori masa kecil yang pudar | Lupa **semua**: Dhiza, Vaniya, Nala, Veyla, anak-anak, Wiadava, Bhas, Yuna |
| Level | 17 (puncak) | 17–48+ (Step 5-12) |
| **Kata terakhir** | *"Aku... pulang."* | *"Aku... pulang."* ❗ |

**Dua ending, kalimat penutup yang sama persis.** Salah satu harus dinyatakan non-canon atau dibingkai ulang.

### Rekomendasi
- **Paling bersih:** nyatakan `09_EPILOG/01_Akhir_Cerita.md` §7 ("Pengawas Multiverse") sebagai **visi/proyeksi yang Yazha lihat saat lompat**, bukan kejadian nyata. Jadi epilog = "*apa yang ia perjuangkan*", dan Sekuel = kenyataannya. Ini malah bikin Sekuel lebih berat.
- Atau: **Sekuel dimulai ratusan tahun setelah epilog**, dan amnesia-nya bukan karena nembus The Shell tapi karena hal lain.

---

## ⚠️ T1-3. "Hanya ada SATU Unbegotten" — udah dilanggar di seri utamanya sendiri

`09_EPILOG/01_Akhir_Cerita.md` §4:
> *"Nala tidak bisa menjadi Level 17 (Unbegotten) karena aturan alam semesta: **Hanya ada SATU Unbegotten di multiverse.**"*

Tapi:
- The First Exception udah Unbegotten **20 miliar tahun** lalu (`11_Entitas_Step_4.md:52`)
- Yazha jadi **yang kedua** — `07_Peta_Alur_Plot.md` 14.2: *"Akhirnya... ada yang kedua."*
- Gelar Yazha: **"The Second Exception"** (`06_Reputasi_Gelar.md:94`)
- `10_Tiga_Dinding_Unbegotten.md`: *"Hanya ada DUA ENTITAS ... yang berhasil melewatinya"*

→ Jadi minimal **dua**, dan aturan "satu" itu bohong.
→ Sekuel malah bikin **Level 17–48+** (Step 5-12), jadi 17 bukan puncak lagi. Nala "cuma" Lv 16 jadi nggak ada artinya.

### Rekomendasi
Ubah jadi: *"Hanya ada SATU Unbegotten **per alam semesta** — dan satu lagi cuma bisa lahir kalau yang pertama mengizinkannya."* Atau: *"Nala bisa saja, tapi ia menolak — karena harganya adalah melepaskan semua yang ia cintai, dan ia sudah kehilangan cukup banyak."*

---

## ⚠️ T1-4. Moxi (identitas pembunuh bayaran) nggak punya slot di peta alur

`07_Profil_Pembunuh_Bayaran.md` (8.700 karakter) + `06_Reputasi_Gelar.md` menjabarkan:

| Arc Moxi | Volume |
|---|---|
| Konflik moral: target nggak bersalah | **Vol 3-4** |
| Klien nyuruh bunuh anak kecil | **Vol 5** |
| Target = mantan teman; titik balik ninggalin profesi | **Vol 6-7** |

Tapi di `07_Peta_Alur_Plot.md`, kata **"Moxi"** cuma muncul **1 kali** — baris 82: *"Moxi mulai terbentuk."*

Vol 3 isinya: jadi asisten apoteker → universitas.
Vol 4 isinya: Grand Tournament.
Vol 5 isinya: buru Nala.
Vol 6 isinya: Veyla mati.

**Nggak ada satu pun bab buat karier pembunuh bayaran.**

**Dan ada masalah logika yang lebih parah:**

`06_Reputasi_Gelar.md` §11: **"Moxi = Rahasia Total."**
`07_Peta_Alur_Plot.md` 4.6: Vol 4 Yazha **menang Grand Tournament**, dapat **Kursi Kosmos ke-7**, dan `06_Reputasi_Gelar.md` nyebut dia *"orang termuda yang pernah memegang kursi ini"* + gelar **"Sang Penakluk Void"**.

→ **Juara Grand Tournament antar planet yang wajahnya dikenal se-dunia nggak mungkin punya identitas pembunuh bayaran rahasia.** Nggak ada penjelasan gimana ini jalan bareng.

**Plus:** `06_Reputasi_Gelar.md:292` bilang Moxi muncul **"Volume 2-3"** — tapi Voidstep (fondasi Moxi) baru bisa dipakai **Vol 3** (`00_CANON_TERKUNCI.md:95`), dan Vol 2 Yazha masih di hutan belantara Zona 5/4, nggak ada klien.

### Rekomendasi
- **Tambahkan Rantai khusus Moxi** di Vol 3–5 (sub-plot yang jalan paralel sama universitas), ATAU
- **Turunkan status Moxi** jadi "nama yang dipakai sesekali buat cari uang" (bukan arc besar), dan hapus 3 arc moralnya, ATAU
- **Pindahin Moxi ke Vol 5-7** (setelah GT selesai, saat Yazha jadi buronan/brutal) — ini justru lebih cocok sama arc "Yazha kehilangan sisi manusianya".

---

## ⚠️ T1-5. Bhaskara & Ryuna hilang setelah Vol 3 (dan premis "kontras bakat" runtuh)

**Masalah 1 — Level mereka ketinggalan jauh:**
`06_Tim_Pendukung.md:30-31, 82-83` — Level Akhir mereka (Vol 2-3) = **Voidskin Puncak (Level 1 Puncak)**.
Tapi `01_Yazha/08_Progresi` — Yazha di Vol 3 = **Level 2-3**.
→ **"Si zero bakat" ngalahin "si berbakat" di Vol 3.**

**Masalah 2 — premis Zero Potential runtuh:**
`01_FONDASI_ATURAN/01_Zero_Potential_Absolut.md:33`:
> *"Bhaskara & Ryuna adalah pengingat: 'Ini yang seharusnya terjadi jika kau punya bakat.'"*

Tapi `13_Kecepatan_Kultivasi_Per_Karakter.md` bilang Bhas/Ryuna: 0→1 = 3 bulan, 1→2 = 6 bulan, 2→3 = 1 tahun. Di Vol 3 harusnya mereka udah **Level 2-3**, bukan 1 Puncak.

**Masalah 3 — nggak ada data Vol 4-14.**
Mereka breakup di Vol 8, reuni di Vol 9, "akrab" di Vol 12-13. Tapi nggak ada file yang nyebut level mereka setelah Vol 3. Secara logika mereka bakal jadi **Level ~5** saat Yazha **Level 16** — nggak relevan, dan reuni emosional di Vol 9-13 jadi nggak bermakna.

### Rekomendasi
- Naikin level Bhas/Ryuna di Vol 2-3 jadi **Level 3 Awal** (biar tetap di depan Yazha).
- Tulis **tabel level Bhas/Ryuna per volume** di `06_Tim_Pendukung.md`, minimal sampai Vol 14. Kalau mereka memang tertinggal, **jadiin itu arc** — mereka memilih hidup fana, menua, dan Yazha harus menyaksikan mereka mati. Itu jauh lebih menyakitkan dan jauh lebih cocok sama tema Kehilangan.

---

## ⚠️ T1-6. Nala jadi "Antagonis / Penguasa Boneka Vol 3-5" — nggak ada di peta alur

`03_Nala_Raynawa.md:29`:
> *"Diculik (Vol 1) → **Eksperimen & Antagonis (Vol 3–5)** → Diselamatkan (Vol 6)"*

Ada deskripsi fisik lengkap buat fase ini (`03_Nala_Raynawa.md` §2.2): *"Jubah hitam panjang dengan sulaman Astralis — pakaian seorang penguasa boneka."*

Tapi di `07_Peta_Alur_Plot.md`:
- Nala pertama kali ketemu di **Vol 5 (5.7)** — *"Nala udah dikendalikan"*
- Vol 5.8: Varek mati, **"Nala mulai sadar"**
- `01_Yazha/10_Arc_Karakter`: Vol 6 = *"Mulai sadar"*, Vol 7 = *"Mulai pulih"*
- `08_Progresi`: Vol 6 = penyelamatan? Nggak ada. Vol 6 = Veyla mati.

→ **Arc "Yazha harus menghadapi adiknya yang jadi musuh" nggak punya satu bab pun.** Padahal ini beats emosional terbesar kedua setelah kematian Veyla.

### Rekomendasi
Tambahkan arc di Vol 6: **Nala yang dikendalikan disuruh membunuh Yazha.** Ini jauh lebih kuat dari "Yazha bunuh Xa Doran & Xa Aran" dan bikin Vol 6 (yang sekarang cuma 6 arc) lebih padat.

---

## ⚠️ T1-7. Wiadava ada di 3 tempat sekaligus antara 2084–2087

| Periode | Lokasi | Sumber |
|---|---|---|
| 2084–2087 | **Koma di reruntuhan Pegunungan Halimun**, Yazha jenguk tiap Sabtu | `02_Aethel_Wiadava.md` §3.3 |
| 2086–2087 | Menulis Buku Catatan *"selama dirawat di **Pusat Rehab Surabaya**"* | `02_Aethel_Wiadava.md:196` |
| 17 Agustus 2087 | **Tewas di Pluto**, satu lawan ratusan | `02_Aethel_Wiadava.md:230` |

Dan `01_Yazha/04_Hubungan_Koneksi.md:87`:
> *"Rasa bersalahnya besar karena dia merasa **gagal menolong Wiadava di Pluto**."*

**Yang nggak dijelaskan di mana pun:**
1. Gimana Wiadava pindah dari Halimun → Surabaya → Pluto? Siapa yang mindahin?
2. Yazha umur 14, **Level 0**, tanpa Core — **naik apa ke Pluto?**
3. Kalau Wiadava di Surabaya, gimana Yazha "jenguk tiap Sabtu" ke Halimun?

### Rekomendasi
Pilih satu rantai yang masuk akal, misal: Yazha nemuin Wiadava di Halimun (2084) → Wiadava sadar dan minta dipindah (dibantu Yazha lewat Kamus Asal) ke fasilitas di Surabaya supaya nggak ketahuan sensor Astralis → Wiadava **sengaja pergi ke Pluto** sendirian buat jadi umpan, tanpa ngasih tahu Yazha (ini yang bikin rasa bersalah Yazha). Yazha **nggak ke Pluto** — dia cuma nerima getaran terakhir lewat Tongkat Safir. Kalau gitu, ubah `04_Hubungan_Koneksi.md:87` jadi *"gagal menyadari bahwa Wiadava sengaja pergi"*.

---

# TIER 2 — SEDANG
*Bikin AI writer nyimpang dari kanon tanpa lu sadar.*

---

## 🔸 T2-1. Master Misterius muncul 3 kali setelah dinyatakan "tidak pernah muncul lagi"

`07_Master_Misterius.md`:
> *"Perpisahan: Setelah membentuk Core, ia pergi. Yazha tidak pernah melihatnya lagi — sampai mungkin di sekuel."*
> *"Konsistensi: Ia tidak pernah muncul lagi setelah Volume 3 — kecuali di sekuel."*

Tapi:
| Sumber | Kemunculan |
|---|---|
| `01_Yazha/08_Progresi` | **Vol 5 (421-480)** — "Tusukan Hampa — **Diajarkan Master Misterius**" |
| `01_Yazha/08_Progresi` | **Vol 8-9 (721-960)** — "Tungku Air Guntur Kosmik — **Diberikan Master Misterius**" |
| `07_Peta_Alur_Plot.md:157` (8.4) | **Vol 8** — *"Pemimpin Ordo [Primordium] adalah Master Misterius"* |

**Dan masalah tambahan:**
- Di `07_Master_Misterius.md` dia **bekas anggota yang kabur**; di plot 8.4 dia **pemimpin Ordo**. Dua peran beda.
- `07_Master_Misterius.md:33`: Level True-World (**Lv 11**) *"tapi ditekan di Alam Fana"* — tapi dia ketemu Yazha di **Zona 4 Hutan Pola, Bumi Abadi** (`02_Alam_Fana_Bumi_Abadi.md` Zona 4), bukan Alam Fana. Alam Fana = Bumi Fana.

---

## 🔸 T2-2. Level Varin Astralis: 4 angka berbeda

| Sumber | Level |
|---|---|
| `00_CANON_TERKUNCI.md:71` + `02_Varin_Astralis.md:133` | **Level 10 Tengah (Realmwarp)** ← canon |
| `02_Aethel_Wiadava.md:112` | **Level 9 Tengah** |
| `05_Xa_Veylara.md:149` | **"kultivator Level 9"** |
| `01_Yazha/04_Hubungan_Koneksi.md:57` | **Rune-Willed Tengah (Lv 9)** ❌ nilai lama |
| `03_DUNIA_KOSMOLOGI/04_Sekte_Faksi.md:34` | **Rune-Willed Tengah (Level 9)** ❌ nilai lama |

→ Audit 24 Juli bilang *"sudah diperbaiki"*, tapi **2 file belum ke-update**: `04_Hubungan_Koneksi.md` dan `04_Sekte_Faksi.md`.

---

## 🔸 T2-3. Rambut putih & Tatapan Merah/Ungu bentrok 2 volume

| Tanda | `08_5_Dimensi_Kehilangan.md` | `01_Yazha/08_Progresi_Kekuatan_Timeline.md` |
|---|---|---|
| Ujung rambut putih | **Vol 5** (Dimensi 2) | Vol 4 udah "setengah putih" |
| Rambut putih total | **Vol 8-9** (Dimensi 4) | **Vol 5** |
| **Tatapan Merah** | **Vol 5** (Dimensi 2) | **Vol 3** (bab 181-240) |
| **Tatapan Ungu** | **Vol 6-7** (Dimensi 3) | **Vol 4** (bab 301-360) |

→ Ini **tanda visual utama** Yazha. Pembaca paling gampang nangkep ini.

---

## 🔸 T2-4. Blacklist dilanggar oleh bible-nya sendiri

CANON §8 (`00_CANON_TERKUNCI.md:135-136`) ngelarang kata-kata ini. Tapi:

| Kata terlarang | Ada di | Baris |
|---|---|---|
| **`Dewa`** | `06_Reputasi_Gelar.md` — gelar *"**Dewa** Tanpa Nama"* | §7 |
| **`Pewaris`** | `06_Reputasi_Gelar.md` — *"**Pewaris** Pengetahuan Sekte Tulis"* | §5 |
| **`mustahil`** | `05_Xa_Veylara.md` — *"lintasan **mustahil**"* | 119 |
| **`mustahil`** | `04_SISTEM_KULTIVASI/10_Tiga_Dinding_Unbegotten.md` — *"transisi paling **mustahil**"* | 10 |
| **`selamat`** | `01_Identitas_Fisik.md` | 66 |
| **`selamat`** | `01_Yazha/02_Sistem_Kultivasi.md` | 65, 66 |
| **`jenius`** (positif) | `02_Aethel_Wiadava.md` — *"**jenius sejati**"* | 9, 107 |
| **`jenius`** | `05_Jiwa_Primordial_7_Lapis.md` — *"5 lapis = **jenius**"* | 19, 29 |
| **`takdir`** | `08_CETAK_BIRU_SEKUEL/*` — "menulis takdir", "Sang Pemutus Takdir", "Penghancur Takdir" | banyak |

**Kenapa ini bahaya:** AI writer **nyontek contoh kalimat dari bible**. Contoh yang melanggar = pelanggaran yang di-copy ke novel.

---

## 🔸 T2-5. Self-audit checklist nyuruh ngehapus nama artefak kanonik

`01_FONDASI_ATURAN/05_Struktur_Volume_Pacing.md:86`:
> *"Ada kata 'Buku Catatan'? → **GANTI** dengan 'buku', 'catatan', 'prasasti'."*

Padahal **"Buku Catatan Wiadava"** adalah nama artefak terkunci di `00_CANON_TERKUNCI.md:58`.

→ **Instruksi ini aktif merusak kanon.** Setiap kali AI jalanin self-audit, dia bakal ngehapus nama artefak utama.

### Rekomendasi
Ubah jadi: *"Ada frasa 'buku catatan' dalam arti **umum**? → GANTI. Tapi '**Buku Catatan Wiadava**' sebagai nama diri WAJIB dipertahankan utuh."*

---

## 🔸 T2-6. Dewan Tujuh: 16 file, **0 kemunculan di peta alur**

`Dewan Tujuh` muncul di 16 file. Tapi `grep -c "Dewan Tujuh" 07_Peta_Alur_Plot.md` = **0**.

Mereka dideskripsikan sebagai (`00_CANON_TERKUNCI.md:121`):
> *"7 tahanan Lesh #7, umur 590 juta tahun, level asli Lv 10-15, ditekan jadi Nexarch Puncak di Alam Fana, **tidak bisa keluar Zona 1**."*

Dan mereka yang **ngasih gelar** ke Yazha (`06_Reputasi_Gelar.md` §5):
- **Pemegang Kursi Kosmos Ke-7**
- **Penjaga Gerbang Bintang**

**Masalah:**
1. Faksi sepenting ini nggak punya satu adegan pun di 14 volume.
2. **Nama "Dewan Tujuh" vs "Dewan Sumber"** (antagonis Vol 10, di Alam Keabadian) — dua nama nyaris identik, dua organisasi beda. Pembaca pasti ketuker.
3. Kenapa tahanan yang nggak bisa keluar Zona 1 bisa ngasih gelar ke juara Grand Tournament di Zona 2?

### Rekomendasi
- **Ganti nama "Dewan Sumber"** jadi nama yang jelas beda (misal: **"Sidang Takhta Emas"** / **"Majelis Sumber"**).
- **Atau** — lebih bagus: **jadikan Dewan Sumber itu rupa lain dari Dewan Tujuh** (mereka akhirnya bebas, atau mereka punya cabang di Alam Keabadian). Ini langsung nutup 2 lubang sekaligus dan bikin Vol 10 punya bobot sejarah.
- **Atau**: kasih Dewan Tujuh 1 arc penampilan di Vol 4 (Grand Tournament) atau Vol 10.

---

## 🔸 T2-7. 11 Lesh dikumpulin di Vol 7, nggak pernah dipakai

`07_Peta_Alur_Plot.md:142` (7.3):
> *"Yazha kumpulin 11 Lesh Putih | Butuh kekuatan buat lawan Varin | Berhasil dapet 10 — Lesh #7 di Bumi Abadi"*

Terus... selesai. **Nggak pernah disebut lagi.**

Padahal:
- `02_Alam_Fana_Bumi_Abadi.md` Zona 1: *"**Klimaks akhir** — Yazha harus menembus Zona 1 untuk mencapai Lesh #7."* Tapi klimaks akhirnya ternyata **Tiga Dinding**, bukan Zona 1.
- `03_Kosmologi_Lesh.md`: Lesh #7 = Jantung Bumi, dijaga **Dragon Garu** — `grep "Dragon Garu" 07_Peta_Alur_Plot.md` = **0**.
- CANON bilang Dewan Tujuh itu **tahanan** Lesh #7. Kalau Yazha ngambil Lesh #7, Dewan Tujuh harusnya bebas atau mati.

**Dan ada kontradiksi yang lebih dalam:**
`04_SISTEM_KULTIVASI/03_Ujian_Penetrasi_Core_Clarity.md:31,44` — **Inti Primeval** (udah dicapai Yazha di Vol 4-5) = *"Bisa **menghasilkan Lesh sendiri**."*

→ Kalau Yazha udah bisa bikin Lesh sendiri dari Vol 5, **ngapain dia buru 11 Lesh di Vol 7?**

### Rekomendasi
Pilih satu:
- **Hapus arc 7.3**, atau
- **Kasih payoff:** Yazha butuh **Lesh asli** (bukan bikinan) karena cuma Lesh asli yang bisa nembus Tiga Dinding / The Shell. Jadiin ini **pencarian utama Vol 7-9** dengan Lesh #7 (Jantung Bumi + Dragon Garu + Dewan Tujuh) sebagai **klimaks Vol 9 atau 10**, sebelum Alam Keabadian.

---

## 🔸 T2-8. Nama lama masih nyisa di file canon

| Temuan | File | Baris |
|---|---|---|
| **"Penggal Ken Volnar"** (Volnar = nama lama) | `07_PETA_ALUR_PLOT/07_Peta_Alur_Plot.md` | 111 |
| Varin masih **Lv 9** (nilai lama) | `01_Yazha/04_Hubungan_Koneksi.md` | 57 |
| Varin masih **Lv 9** (nilai lama) | `03_DUNIA_KOSMOLOGI/04_Sekte_Faksi.md` | 34 |

---

## 🔸 T2-9. Alias & gelar Yazha nggak pernah divalidasi

`07_Profil_Pembunuh_Bayaran.md` + `06_Reputasi_Gelar.md` nyebut alias: **Y.R., Ray, Dava, Yaz, Nawa, Moxi**.

Tapi `00_CANON_TERKUNCI.md` §1 (tabel nama kanonik) cuma punya **"Yazha"**. Nggak ada aturan:
- Alias mana dipakai di situasi apa
- Siapa yang tahu alias yang mana
- Apakah Bhaskara/Ryuna tahu

---

# TIER 3 — KECIL / CATATAN

---

## 🔹 T3-1. Pembunuhan pertama di Vol 1 = Level 0
`07_Peta_Alur_Plot.md:44` (1.5): Yazha **Level 0, belum punya Core**, "pake energi pertama kali — **preman mati**".
Tapi `00_CANON_TERKUNCI.md:141` (skala kekuatan): Level 1-2 baru "skala bangunan". Level 0 = manusia biasa.
Dan `02_17_Level_Detail.md` naruh contoh adegan preman di **Level 1 Tengah (Vol 2)**, bukan Vol 1.
→ Fix: bikin preman mati **karena jatuh / kepalanya ke batu**, bukan karena energi Yazha. Lebih cocok sama Zero Potential dan lebih traumatis.

## 🔹 T3-2. Tiga antagonis bullying Vol 1 yang beda
- Plot 1.2: **"Guru SD"** hina Yazha
- Plot 1.4: **"Kurnia"** (teman sekolah) khianati Yazha
- Plot (catatan kaki Bhas/Ryuna): **"Adit dan teman-temannya"** mengejek Yazha
→ Tiga nama, nggak ada yang dikonfirmasi canon.

## 🔹 T3-3. Bhaskara & Ryuna ketemu Yazha di mana?
- Plot 1.6: *"Yazha kabur ke Halimun — **ketemu Bhaskara & Ryuna di jalur**"* (kesannya baru kenal)
- Plot (catatan kaki): *"Mereka BUKAN sahabat dari kecil. **Baru kenal beberapa tahun terakhir**... mereka membela Yazha [dari Adit]"*
→ "Ketemu di jalur saat kabur" ≠ "udah kenal & pernah membela".

## 🔹 T3-4. Nala tembus Level 16 Puncak di epilog
`03_Nala_Raynawa.md`: *"**manusia biasa 100%**, tidak ada darah khusus."* Dicuil umur 5-6 tahun.
Epilog: dia capai **Primordial Puncak (Level 16)**.
Banding: Wiadava (jenius) 10.000 tahun baru Lv 8. Varin 100.000+ tahun baru Lv 9.
→ Perlu dijelasin, atau nurunin jadi Level 8-10.

## 🔹 T3-5. Anak Yazha levelnya rendah banget
Epilog: **Akasa** (19-20 tahun) = Nexarch Puncak (**Level 4**). **Kanavi** (16-17) = Starborn Tengah (**Level 3**).
Ayah mereka = Level 17, Sebab Pertama, Pengamat Multiverse. Bibi mereka = Level 16.
→ Perlu alasan in-universe (misal: Yazha sengaja nggak bantu — *"Aku nggak mau mereka jadi monster kayak aku"*). Ini malah bisa jadi momen bagus.

## 🔹 T3-6. Akasa "mirip gaya bicara Wiadava (yang diceritakan oleh Yazha)"
Epilog §5.A. Tapi `02_Aethel_Wiadava.md` §3.3: Wiadava **koma total 2084-2086**, cuma bisa kirim **getaran energi** — nggak pernah ngomong. Dan Wiadava bilang filosofinya: *"Kau harus mengalami dulu, baru menamai."*
→ Gimana Yazha tahu "gaya bicara" Wiadava kalau mereka nggak pernah ngobrol?

## 🔹 T3-7. Volume 1 = 35 bab buat 3 tahun
2084 (Yazha 11) → 17 Agustus 2087 (Yazha 14). 35 bab.
`05_Struktur_Volume_Pacing.md`: *"Yazha butuh berbulan-bulan untuk satu kata pertama."*
Muat sih, tapi sangat padat: guru SD + latihan Sabtu + Kurnia + preman + polisi + kabur + invasi, semuanya di 35 bab yang temponya "lambat dan detail untuk sakit".

## 🔹 T3-8. Moxi muncul "Volume 2-3" vs Voidstep baru Vol 3
`06_Reputasi_Gelar.md:292`: Moxi muncul **Vol 2-3**.
Tapi Voidstep = fondasi Moxi, baru bisa dipakai **Vol 3** (`00_CANON_TERKUNCI.md:95`).
Dan CANON §5 nyebut Voidstep *"Vol 3 | 100-110+"* — padahal **bab 100-110 itu Vol 2**, bukan Vol 3 (Vol 3 = 121-240).

## 🔹 T3-9. Inti Primeval nggak pernah muncul di peta alur
`grep -c "Inti Primeval" 07_Peta_Alur_Plot.md` = **0**.
Padahal ini milestone yang dikunci di `00_CANON_TERKUNCI.md:97` (Vol 4-5) dan punya file sendiri (`03_Ujian_Penetrasi_Core_Clarity.md`) dengan kutipan:
> *"Inti Primeval... hanya satu orang yang pernah mencapainya dalam sejarah modern. Dan dia tidak berbakat."*

---

# 7 KEPUTUSAN YANG HARUS LU AMBIL

Ini nggak bisa gue tentuin buat lu. Tapi **semuanya harus dijawab** sebelum novelnya ditulis:

| # | Pertanyaan | Opsi yang tersedia |
|---|---|---|
| **1** | **Timescale:** berapa tahun total perjalanan Vol 1→14? | A) ~50-80 tahun (perlu aturan "kemajuan = kedalaman kehilangan") · B) Ribuan tahun (perlu rombak epilog, Nala, Bhas/Yuna) |
| **2** | **Varin mati Vol 7 atau Vol 9?** | A) Vol 7 (sesuai plot + arc + level file; CANON salah) · B) Vol 9 (perlu rombak Rantai 7 & 8) |
| **3** | **Kapan masuk Alam Kekosongan?** | A) Vol 8 (sesuai judul Rantai 8, Gerbang Kesepian Vol 8) · B) Vol 9 (sesuai CANON; judul Rantai 7 & 8 harus diganti) |
| **4** | **Moxi: arc besar atau cuma nama?** | A) Arc besar → butuh slot bab Vol 3-7 · B) Cuma nama → hapus 3 arc moral · C) Pindah ke Vol 5-7 |
| **5** | **Epilog vs Sekuel, mana yang canon?** | A) Epilog = visi saat lompat, Sekuel = nyata · B) Sekuel = lanjutan ratusan tahun kemudian · C) Pilih salah satu, hapus yang lain |
| **6** | **Dewan Tujuh vs Dewan Sumber** | A) Ganti nama salah satu · B) Jadikan organisasi yang sama (Vol 10 jadi jauh lebih berat) · C) Kasih Dewan Tujuh arc sendiri |
| **7** | **11 Lesh: dipakai atau dibuang?** | A) Dibuang (hapus arc 7.3) · B) Jadiin pencarian utama Vol 7-10, klimaks = Lesh #7 + Dragon Garu + Zona 1 |

---

# URUTAN PENAMBALAN (yang paling hemat tenaga)

**Hari 1 — Beresin yang bikin AI salah nulis (2-3 jam):**
1. Tulis ulang tabel `02_17_Level_Detail.md` baris 286-310 → mentok 1530 bab, Lv 17 di 1441-1480
2. Perbaiki range bab yang dobel di "Waktu Dicapai" (Level 10/11 & 12/13)
3. Update `04_Hubungan_Koneksi.md:57` + `04_Sekte_Faksi.md:34` → Varin Lv 10 Tengah
4. Ganti "Penggal Ken Volnar" → "Penggal Ken Voth" (plot:111)
5. Fix `05_Struktur_Volume_Pacing.md:86` (instruksi "Buku Catatan")

**Hari 2 — Beresin yang bikin plot ngaco:**
6. Tabel "Alam per Volume" di CANON
7. Tabel "Usia Yazha & tahun per Volume" di CANON
8. Tabel "Level Bhas/Ryuna per volume" di `06_Tim_Pendukung.md`
9. Fix kematian Varin + bikin arc kematian Goliath
10. Fix lokasi Wiadava (Halimun → Surabaya → Pluto)

**Hari 3 — Beresin yang bikin ending bermasalah:**
11. T1-1 (paradoks Veyla)
12. T1-2 (Epilog vs Sekuel)
13. T1-3 (aturan "satu Unbegotten")
14. T2-6 (Dewan Tujuh vs Dewan Sumber)
15. T2-7 (payoff 11 Lesh)

---

# PENUTUP

Audit 24 Juli (`00_INKONSISTENSI_AUDIT.md`) udah beresin **kulitnya**: nama, lokasi, artefak, gaya bahasa. Itu kerjaan yang kelihatan dan hasilnya bagus.

Audit V3 ini nemuin masalah di **tulangnya**: tiga tabel progresi level yang saling tabrak, dua timescale yang nggak bisa keduanya benar, empat arc besar yang di-setup tapi nggak pernah punya bab (Moxi, Nala antagonis, Lesh, Dewan Tujuh), dan ending yang tabrakan sama sekuel.

**Kabar baiknya:** nggak ada satu pun dari ini yang minta lu nulis ulang idenya. Semuanya minta **keputusan + satu tabel**. Bible lu nggak kurang imajinasi — dia kurang **satu angka yang disepakati**.

---

**— END OF AUDIT V3 —**
