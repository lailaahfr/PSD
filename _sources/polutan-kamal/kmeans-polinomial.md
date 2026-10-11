# K-Means Clustering pada Data Polutan Versi Polinomial

![Workflow K-Means untuk data polinomial](../img/kmenas-polinomial.png)

## 1. Gambaran Umum

Pada tahap ini dilakukan proses **clustering menggunakan algoritma K-Means** terhadap data polutan Kertosono. Data yang dianalisis terdiri atas tiga jenis polutan, yaitu **karbon monoksida (CO), nitrogen dioksida (NO₂), dan sulfur dioksida (SO₂)**.

Sebelum dilakukan proses clustering, data terlebih dahulu melalui tahap preprocessing. Pada tahap ini, nilai yang hilang atau **missing value** diisi menggunakan **interpolasi polinomial**. Interpolasi dilakukan untuk memperkirakan nilai yang hilang berdasarkan pola nilai di sekitar data tersebut sehingga deret waktu menjadi lebih lengkap dan dapat digunakan pada tahap berikutnya.

Setelah missing value ditangani, data kemudian melalui proses **ekstraksi fitur menggunakan TSFEL (Time Series Feature Extraction Library)**. Hasil ekstraksi fitur tersebut selanjutnya digunakan sebagai masukan dalam proses K-Means Clustering.

Pada eksperimen ini digunakan tiga variasi jumlah cluster, yaitu:

- **k = 3**
- **k = 5**
- **k = 7**

Selain clustering menggunakan seluruh fitur, dilakukan juga eksperimen menggunakan **Principal Component Analysis (PCA)** untuk melihat pengaruh reduksi dimensi terhadap kualitas cluster.

Secara umum tahapan analisis yang dilakukan adalah:

**Data Polutan → Penanganan Missing Value dengan Interpolasi Polinomial → Ekstraksi Fitur TSFEL → Standardisasi → PCA → K-Means → Evaluasi Silhouette Coefficient**

## 2. Preprocessing Missing Value dengan Interpolasi Polinomial

Data deret waktu polutan dapat memiliki nilai kosong atau **missing value** pada beberapa periode pengamatan. Nilai kosong tersebut perlu ditangani sebelum dilakukan proses ekstraksi fitur karena missing value dapat memengaruhi perhitungan karakteristik sinyal.

Pada penelitian ini, missing value ditangani menggunakan **interpolasi polinomial**.

Interpolasi polinomial memperkirakan nilai yang hilang dengan membentuk fungsi polinomial berdasarkan beberapa titik data yang tersedia di sekitar nilai yang hilang. Nilai hasil interpolasi kemudian digunakan untuk menggantikan nilai kosong pada data.

Secara umum, proses interpolasi polinomial dapat dituliskan sebagai:

\[
P(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n
\]

dengan:

- \(P(x)\) merupakan nilai hasil interpolasi,
- \(x\) merupakan posisi atau waktu pengamatan,
- \(a_0,a_1,\ldots,a_n\) merupakan koefisien polinomial.

Penggunaan interpolasi bertujuan untuk menjaga kontinuitas deret waktu sehingga proses ekstraksi fitur dapat dilakukan pada data yang lebih lengkap.

Tahapan preprocessing yang dilakukan meliputi:

1. membaca data polutan CO, NO₂, dan SO₂;
2. memeriksa keberadaan missing value;
3. mengisi missing value menggunakan interpolasi polinomial;
4. memeriksa kembali apakah masih terdapat nilai kosong; dan
5. menggunakan data hasil interpolasi untuk proses ekstraksi fitur.

Dengan demikian, istilah **data versi polinomial** pada analisis ini mengacu pada data yang missing value-nya telah ditangani menggunakan metode interpolasi polinomial.

## 3. Ekstraksi Fitur TSFEL

Setelah proses interpolasi selesai, data CO, NO₂, dan SO₂ digunakan dalam proses ekstraksi fitur menggunakan **TSFEL**.

TSFEL digunakan untuk mengubah data deret waktu menjadi sejumlah fitur numerik yang menggambarkan karakteristik sinyal.

Dataset hasil ekstraksi fitur terdiri atas:

| Polutan | Jumlah Fitur |
|---|---:|
| NO₂ | 68 |
| SO₂ | 68 |
| CO | 68 |
| **Total** | **204** |

Masing-masing polutan menghasilkan **68 fitur**, sehingga secara keseluruhan diperoleh **204 fitur**.

Fitur-fitur tersebut mencakup berbagai karakteristik sinyal, seperti statistik, energi, korelasi, distribusi, karakteristik temporal, frekuensi, dan karakteristik lainnya.

Hasil ekstraksi kemudian disimpan dalam dataset:

`Polynomial-Kertosono-TSFEL.csv`

Dataset tersebut selanjutnya digunakan sebagai data masukan pada proses clustering.

## 4. Persiapan Data untuk K-Means

Sebelum K-Means dijalankan, data hasil ekstraksi fitur terlebih dahulu dipersiapkan agar sesuai untuk proses clustering.

### 4.1 Membaca Dataset

Dataset `Polynomial-Kertosono-TSFEL.csv` dibaca menggunakan **CSV Reader**.

Pada tahap ini dilakukan pemeriksaan terhadap struktur dataset untuk memastikan bahwa fitur yang akan digunakan memiliki tipe data numerik dan dapat diproses oleh algoritma K-Means.

### 4.2 Pemilihan Fitur

Fitur numerik hasil ekstraksi TSFEL digunakan sebagai variabel masukan K-Means.

Kolom yang hanya berfungsi sebagai identitas atau informasi tambahan tidak digunakan dalam perhitungan jarak.

### 4.3 Standardisasi Data

Sebelum clustering, data dilakukan **standardisasi**.

Standardisasi diperlukan karena setiap fitur hasil TSFEL dapat memiliki skala nilai yang berbeda. Sementara itu, K-Means menggunakan jarak Euclidean dalam menentukan kedekatan antarobservasi.

Standardisasi membantu mencegah fitur dengan rentang nilai besar mendominasi proses pembentukan cluster.

## 5. Reduksi Dimensi Menggunakan PCA

Selain menggunakan seluruh fitur, dilakukan juga eksperimen menggunakan **Principal Component Analysis (PCA)**.

PCA digunakan untuk mereduksi jumlah dimensi data dengan mentransformasikan fitur asli menjadi sejumlah komponen utama yang dapat mempertahankan sebagian besar variasi data.

Eksperimen dilakukan menggunakan empat skenario:

- **Tanpa PCA**
- **PCA 203 komponen**
- **PCA 74 komponen**
- **PCA 37 komponen**

Setiap skenario kemudian diuji menggunakan K-Means dengan:

- `k = 3`
- `k = 5`
- `k = 7`

Tujuan penggunaan beberapa jumlah komponen PCA adalah untuk membandingkan apakah pengurangan jumlah dimensi memberikan perubahan terhadap kualitas cluster yang terbentuk.

## 6. K-Means Clustering

K-Means merupakan algoritma **unsupervised learning** yang digunakan untuk membagi data ke dalam sejumlah kelompok atau cluster berdasarkan tingkat kemiripan antarobservasi.

K-Means bekerja dengan menentukan pusat cluster atau **centroid**, kemudian setiap data ditempatkan ke cluster dengan centroid terdekat.

Pada penelitian ini digunakan tiga nilai jumlah cluster.

### 6.1 K-Means k = 3

Pada eksperimen pertama, jumlah cluster ditentukan sebanyak:

\[
k=3
\]

Data dibagi menjadi tiga kelompok berdasarkan kedekatan karakteristik fiturnya.

### 6.2 K-Means k = 5

Pada eksperimen berikutnya digunakan:

\[
k=5
\]

Penggunaan lima cluster bertujuan untuk melihat apakah data memiliki pola kelompok yang lebih rinci dibandingkan dengan penggunaan tiga cluster.

### 6.3 K-Means k = 7

Eksperimen terakhir menggunakan:

\[
k=7
\]

Penggunaan tujuh cluster menghasilkan pembagian kelompok yang lebih banyak sehingga pola data dapat dikelompokkan secara lebih detail.

Namun, jumlah cluster yang lebih banyak tidak selalu menghasilkan clustering yang lebih baik. Oleh karena itu, setiap konfigurasi perlu dievaluasi menggunakan Silhouette Coefficient.

## 7. Evaluasi Silhouette Coefficient

Hasil K-Means dievaluasi menggunakan **Silhouette Coefficient**.

Silhouette Coefficient digunakan untuk mengukur seberapa baik suatu observasi berada pada cluster-nya dibandingkan dengan cluster lainnya.

Nilai Silhouette Coefficient berada pada rentang:

\[
-1 \leq s \leq 1
\]

Interpretasinya secara umum adalah:

- nilai mendekati **1** menunjukkan cluster memiliki pemisahan yang baik;
- nilai mendekati **0** menunjukkan data berada di sekitar batas dua cluster;
- nilai negatif menunjukkan terdapat kemungkinan data ditempatkan pada cluster yang kurang sesuai.

Oleh karena itu, konfigurasi dengan nilai silhouette yang lebih tinggi menunjukkan struktur cluster yang relatif lebih baik.

## 8. Hasil K-Means Tanpa Reduksi Dimensi

Pada skenario pertama, K-Means diterapkan langsung pada data tanpa melakukan reduksi dimensi menggunakan PCA.

### k = 3

![Tabel Silhouette k=3 tanpa reduksi](../../img/kp_tp_3.png)

![Scatter plot k=3 tanpa reduksi](../../img/kp_s_3.png)

Pada konfigurasi `k = 3`, data dibagi menjadi tiga cluster. Hasil clustering kemudian dievaluasi menggunakan Silhouette Coefficient untuk mengetahui tingkat pemisahan antarcluster.

### k = 5

![Tabel Silhouette k=5 tanpa reduksi](../../img/kp_tp_5.png)

![Scatter plot k=5 tanpa reduksi](../../img/kp_s_5.png)

Pada konfigurasi `k = 5`, data dibagi menjadi lima cluster. Hasil ini digunakan sebagai pembanding terhadap konfigurasi `k = 3`.

### k = 7

![Tabel Silhouette k=7 tanpa reduksi](../../img/kp_tp_7.png)

![Scatter plot k=7 tanpa reduksi](../../img/kp_s_7.png)

Pada konfigurasi `k = 7`, data dibagi menjadi tujuh cluster untuk melihat apakah penambahan jumlah kelompok menghasilkan struktur cluster yang lebih baik.

## 9. Hasil K-Means dengan PCA 203 Komponen

Eksperimen berikutnya dilakukan menggunakan hasil PCA sebanyak **203 komponen utama**.

### k = 3

![Tabel Silhouette PCA 203 k=3](../../img/kp_203_3.png)

![Scatter plot PCA 203 k=3](../../img/kp_203_s_3.png)

### k = 5

![Tabel Silhouette PCA 203 k=5](../../img/kp_203_5.png)

![Scatter plot PCA 203 k=5](../../img/kp_203_s_5.png)

### k = 7

![Tabel Silhouette PCA 203 k=7](../../img/kp_203_7.png)

![Scatter plot PCA 203 k=7](../../img/kp_203_s_7.png)

Ketiga konfigurasi tersebut dibandingkan berdasarkan nilai Silhouette Coefficient untuk melihat jumlah cluster yang memberikan struktur kelompok terbaik.

## 10. Hasil K-Means dengan PCA 74 Komponen

Pada skenario berikutnya, data direduksi menjadi **74 komponen utama** menggunakan PCA.

### k = 3

![Tabel Silhouette PCA 74 k=3](../../img/kp_74_3.png)

![Scatter plot PCA 74 k=3](../../img/kp_74_s_3.png)

### k = 5

![Tabel Silhouette PCA 74 k=5](../../img/kp_74_5.png)

![Scatter plot PCA 74 k=5](../../img/kp_74_s_5.png)

### k = 7

![Tabel Silhouette PCA 74 k=7](../../img/kp_74_7.png)

![Scatter plot PCA 74 k=7](../../img/kp_74_s_7.png)

Hasil ketiga konfigurasi digunakan untuk mengetahui pengaruh reduksi menjadi 74 komponen terhadap kualitas cluster.

## 11. Hasil K-Means dengan PCA 37 Komponen

Skenario terakhir menggunakan PCA sebanyak **37 komponen utama**.

### k = 3

![Tabel Silhouette PCA 37 k=3](../../img/kp_37_3.png)

![Scatter plot PCA 37 k=3](../../img/kp_37_s_3.png)

### k = 5

![Tabel Silhouette PCA 37 k=5](../../img/kp_37_5.png)

![Scatter plot PCA 37 k=5](../../img/kp_37_s_5.png)

### k = 7

![Tabel Silhouette PCA 37 k=7](../../img/kp_37_7.png)

![Scatter plot PCA 37 k=7](../../img/kp_37_s_7.png)

Ketiga konfigurasi tersebut selanjutnya dibandingkan dengan hasil tanpa PCA, PCA 203, dan PCA 74.

## 12. Perbandingan Hasil

Secara keseluruhan terdapat **12 konfigurasi eksperimen**, yaitu kombinasi antara empat skenario jumlah fitur dan tiga nilai `k`.

| Skenario | k = 3 | k = 5 | k = 7 |
|---|---|---|---|
| Tanpa PCA | Nilai Silhouette | Nilai Silhouette | Nilai Silhouette |
| PCA 203 | Nilai Silhouette | Nilai Silhouette | Nilai Silhouette |
| PCA 74 | Nilai Silhouette | Nilai Silhouette | Nilai Silhouette |
| PCA 37 | Nilai Silhouette | Nilai Silhouette | Nilai Silhouette |

Nilai Silhouette Coefficient dari setiap konfigurasi kemudian dibandingkan.

Konfigurasi dengan nilai silhouette tertinggi menunjukkan struktur cluster yang memiliki tingkat kedekatan dalam cluster dan pemisahan antarcluster yang relatif lebih baik dibandingkan konfigurasi lainnya.

Namun, penentuan konfigurasi terbaik juga perlu mempertimbangkan jumlah anggota pada setiap cluster dan visualisasi distribusi cluster.

## 13. Interpretasi

Penggunaan `k = 3`, `k = 5`, dan `k = 7` menghasilkan tingkat pembagian kelompok yang berbeda.

Pada `k = 3`, data dibagi menjadi tiga kelompok utama sehingga struktur cluster lebih sederhana dan relatif mudah diinterpretasikan.

Pada `k = 5`, pembagian kelompok menjadi lebih rinci sehingga karakteristik data yang sebelumnya tergabung dalam satu cluster dapat dipisahkan menjadi kelompok yang lebih spesifik.

Pada `k = 7`, pembentukan cluster menjadi lebih detail. Namun, jumlah cluster yang lebih banyak tidak selalu menunjukkan hasil yang lebih baik karena terdapat kemungkinan terbentuk cluster dengan anggota yang sedikit atau jarak antarcluster yang kurang jelas.

Oleh karena itu, jumlah cluster terbaik ditentukan dengan membandingkan nilai Silhouette Coefficient dari `k = 3`, `k = 5`, dan `k = 7`.

## 14. Kesimpulan

Analisis data polutan Kertosono dilakukan melalui beberapa tahapan yang dimulai dari preprocessing data.

Missing value pada data CO, NO₂, dan SO₂ terlebih dahulu ditangani menggunakan **interpolasi polinomial**. Data hasil interpolasi kemudian digunakan dalam proses ekstraksi fitur menggunakan **TSFEL**.

Masing-masing polutan menghasilkan 68 fitur sehingga diperoleh **204 fitur** secara keseluruhan.

Data hasil ekstraksi fitur kemudian distandardisasi sebelum digunakan dalam proses clustering. Selain menggunakan seluruh fitur, dilakukan pula eksperimen reduksi dimensi menggunakan PCA dengan 203, 74, dan 37 komponen.

K-Means dijalankan menggunakan tiga variasi jumlah cluster, yaitu **k = 3, k = 5, dan k = 7**.

Kualitas setiap hasil clustering dievaluasi menggunakan **Silhouette Coefficient**. Konfigurasi dengan nilai silhouette tertinggi digunakan sebagai acuan dalam menentukan struktur cluster yang memberikan pemisahan terbaik pada data polutan.

## 15. Kesimpulan Singkat untuk Laporan

Data polutan CO, NO₂, dan SO₂ terlebih dahulu melalui tahap preprocessing untuk menangani missing value menggunakan interpolasi polinomial. Data yang telah lengkap kemudian diekstraksi menggunakan TSFEL sehingga diperoleh 68 fitur untuk masing-masing polutan atau 204 fitur secara keseluruhan. Selanjutnya dilakukan standardisasi dan reduksi dimensi menggunakan PCA dengan beberapa skenario, yaitu tanpa PCA, PCA 203, PCA 74, dan PCA 37. K-Means kemudian diterapkan menggunakan `k = 3`, `k = 5`, dan `k = 7`. Hasil setiap konfigurasi dievaluasi menggunakan Silhouette Coefficient untuk menentukan jumlah cluster dan skenario reduksi dimensi yang memberikan kualitas clustering terbaik.