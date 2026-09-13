# 1. Business Understanding

## 1.1 Latar Belakang

- Kabupaten **Bangkalan**, sebagai bagian dari wilayah **Madura** dan kawasan sekitar **Surabaya**, menghadapi tekanan aktivitas antropogenik seperti:
  - transportasi,
  - industri kecil,
  - pembakaran biomassa,
  - pertumbuhan permukiman,  
  yang berpotensi memengaruhi **kualitas udara**.

- Cakupan **stasiun pemantau kualitas udara darat** (ground station) di wilayah ini masih **terbatas**, sehingga sulit mendapatkan gambaran **spasial** yang lengkap dan konsisten dari waktu ke waktu.

- Data pengamatan satelit **Sentinel‑5P** menyediakan alternatif penting karena:
  - cakupan **global**,
  - resolusi spasial yang relatif **tinggi**,
  - konsistensi temporal sejak **2018**.  

- Produk **Level‑2 Sentinel‑5P** mencakup kolom total berbagai polutan (**NO₂, SO₂, CO, O₃, HCHO**, dll.) yang dapat digunakan untuk memetakan sebaran polusi udara secara **spasial** dan **temporal**.

- Dengan memanfaatkan layanan **openEO**, data ini dapat:
  - diakses,
  - diproses,
  - dianalisis secara komputasional di lingkungan **cloud**,  
  sehingga cocok untuk proyek data sains yang memerlukan **skalabilitas** dan **reproduktibilitas**.

---

## 1.2 Tujuan Proyek

Secara umum, proyek ini bertujuan untuk:

1. Membangun **pipeline data kualitas udara** berbasis satelit untuk wilayah **Bangkalan** menggunakan **Sentinel‑5P** dan **openEO**.  
2. Menggambarkan **pola spasial** dan **temporal** konsentrasi polutan utama (**NO₂, SO₂, CO**) di Bangkalan dalam periode tertentu.  
3. Menyediakan dasar analitis yang dapat digunakan untuk:
   - pemantauan kualitas udara,
   - identifikasi area rawan polusi,
   - dukungan keputusan terkait **lingkungan** dan **kesehatan masyarakat**.

---

## 1.3 Rumusan Masalah

Berdasarkan latar belakang tersebut, rumusan masalah dalam proyek ini adalah:

1. Bagaimana **karakteristik sebaran spasial** dan **temporal** konsentrasi polutan **NO₂, SO₂, dan CO** di wilayah Bangkalan berdasarkan data **Sentinel‑5P**?  
2. Apakah terdapat **pola musiman** atau **tren tertentu** pada konsentrasi polutan tersebut selama periode pengamatan?  
3. Area mana di Bangkalan yang secara konsisten menunjukkan **tingkat polutan lebih tinggi**, dan faktor apa (misalnya dekat jalur transportasi, kawasan permukiman padat, atau aktivitas industri) yang mungkin berkontribusi?

---

## 1.4 Target / Sasaran Analisis

Target teknis dari proyek ini meliputi:

1. Mengakses dan mengekstrak data **Sentinel‑5P** (**NO₂, SO₂, CO**) untuk *bounding box* wilayah Bangkalan melalui **openEO/Copernicus Data Space**.  
2. Melakukan **pra-pemrosesan data**, meliputi:
   - filtering,
   - agregasi temporal,
   - handling missing value,  
   sehingga siap untuk analisis lebih lanjut.  
3. Menghasilkan:
   - visualisasi **peta sebaran polutan**,
   - **deret waktu (time series)**,
   - ringkasan **statistik per wilayah/kabupaten**.  
4. Menyusun **interpretasi awal** terkait potensi sumber polusi dan implikasinya bagi kualitas udara lokal.

---

## 1.5 Manfaat Proyek

Proyek ini diharapkan memberikan manfaat, antara lain:

### a. Bagi akademisi / mahasiswa

- Contoh nyata penerapan **data sains** dan **remote sensing** untuk isu lingkungan di Indonesia.  
- Latihan **end‑to‑end pipeline data**:
  - akses data cloud,
  - ekstraksi fitur,
  - visualisasi,
  - interpretasi.

### b. Bagi pemangku kepentingan lokal  
(pemerintah daerah, dinas lingkungan)

- Informasi tambahan tentang **sebaran polutan udara** yang dapat melengkapi data stasiun darat.  
- Dasar awal untuk:
  - identifikasi area prioritas pemantauan,
  - intervensi pengendalian pencemaran udara.

### c. Bagi masyarakat

- Peningkatan **kesadaran** tentang kondisi kualitas udara di wilayah mereka.  
- Informasi yang dapat dikaitkan dengan isu **kesehatan** (misalnya paparan **NO₂** dan **SO₂**) dalam konteks edukasi.

---

## 1.6 Ruang Lingkup dan Batasan

Agar proyek tetap terfokus, beberapa batasan diterapkan:

1. Wilayah studi dibatasi pada **Kabupaten Bangkalan, Jawa Timur** (dengan *bounding box* tertentu).  
2. Data utama yang digunakan adalah produk **Level‑2 Sentinel‑5P** (**NO₂, SO₂, CO**) yang tersedia di **Copernicus Data Space**.  
3. Analisis bersifat **deskriptif** dan **eksploratif**; pemodelan prediktif atau kausalitas mendalam **bukan target utama** pada tahap ini.  
4. Validasi dengan data stasiun darat (jika ada) bersifat **opsional** dan **terbatas**, mengingat ketersediaan data *ground truth* di Bangkalan mungkin minim.