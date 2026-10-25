# Business Understanding

Business Understanding merupakan tahap awal dalam proses analisis data yang bertujuan untuk memahami permasalahan yang akan dikaji sebelum masuk ke tahap pengolahan data. Pada tahap ini ditentukan masalah utama, tujuan analisis, kebutuhan yang ingin dicapai, serta pendekatan analitik yang dapat digunakan untuk membantu menjawab permasalahan tersebut.

Dalam proyek ini, Business Understanding digunakan untuk membangun dasar analisis terhadap kondisi polutan udara di **Kecamatan Kamal, Kabupaten Bangkalan, Jawa Timur**.

## Mendefinisikan Masalah

### Problem

Kecamatan Kamal menjadi wilayah pengamatan dalam proyek ini. Permasalahan utama yang ingin dikaji adalah:

> **Bagaimana karakteristik data polutan udara di Kecamatan Kamal berdasarkan hasil pengamatan satelit?**

Analisis difokuskan pada tiga jenis polutan, yaitu **karbon monoksida (CO)**, **nitrogen dioksida (NO₂)**, dan **sulfur dioksida (SO₂)**. Pengamatan terhadap ketiga polutan tersebut digunakan untuk memperoleh gambaran mengenai karakteristik dan variasi polutan pada wilayah serta periode yang dianalisis.

1. **Karbon monoksida (CO)** merupakan gas yang tidak berwarna, tidak berbau, dan tidak berasa. Gas ini umumnya terbentuk akibat proses pembakaran bahan bakar atau biomassa yang tidak berlangsung secara sempurna. Sumber emisi CO dapat berasal dari kendaraan bermotor, kegiatan industri, pembakaran biomassa, serta berbagai aktivitas pembakaran lainnya. Pada konsentrasi tinggi, paparan CO dapat menghambat kemampuan darah dalam membawa oksigen sehingga dapat menimbulkan gangguan kesehatan seperti sakit kepala, pusing, gangguan kardiovaskular, hingga kondisi yang lebih serius.

2. **Nitrogen dioksida (NO₂)** merupakan gas berwarna cokelat kemerahan dengan bau yang cukup tajam dan umumnya terbentuk dari proses pembakaran bersuhu tinggi. Sumber NO₂ banyak berkaitan dengan emisi kendaraan bermotor, pembangkit listrik berbahan bakar fosil, serta aktivitas industri. Selain berperan dalam pembentukan kabut asap dan hujan asam, paparan NO₂ juga dapat mengganggu sistem pernapasan, memperburuk asma, dan meningkatkan kerentanan terhadap gangguan pernapasan.

3. **Sulfur dioksida (SO₂)** merupakan gas tidak berwarna dengan bau menyengat yang terutama dihasilkan dari pembakaran bahan bakar yang mengandung sulfur, seperti batu bara dan minyak bumi. Emisi SO₂ dapat berasal dari pembangkit listrik, kegiatan industri, maupun sumber alami seperti aktivitas vulkanik. Di atmosfer, SO₂ dapat berkontribusi terhadap pembentukan hujan asam yang berdampak pada lingkungan dan infrastruktur. Paparan dalam konsentrasi tinggi juga dapat menyebabkan iritasi saluran pernapasan serta memperburuk kondisi kesehatan tertentu, terutama pada sistem pernapasan.

### Goal

Tujuan proyek adalah memperoleh **gambaran berbasis data mengenai karakteristik polutan udara di Kecamatan Kamal** dengan memanfaatkan data pengamatan satelit.

Hasil analisis diharapkan dapat membuat data atmosfer yang semula berupa data pengamatan satelit menjadi informasi yang lebih mudah dibaca, dibandingkan, dan dipahami.

### Objectives

Untuk mencapai tujuan tersebut, proyek ini memiliki beberapa objective:

1. Mengumpulkan data pengamatan **NO₂, SO₂, dan CO** pada wilayah Kecamatan Kamal.
2. Mengolah data pengamatan menjadi bentuk yang sesuai untuk proses analisis.
3. Mengidentifikasi nilai dan variasi masing-masing polutan selama periode pengamatan.
4. Menyajikan hasil analisis dalam bentuk yang dapat membantu memahami karakteristik polutan pada wilayah penelitian.
5. Menyusun proses analisis secara sistematis sehingga tahapan pengambilan dan pengolahan data dapat direproduksi.

## Analytics Approach

Setelah masalah dan tujuan ditentukan, tahap berikutnya adalah menentukan bagaimana data dapat digunakan untuk membantu menjawab permasalahan tersebut.

### Descriptive Analytics

Pendekatan utama pada proyek ini adalah **descriptive analytics**, yaitu menggunakan data untuk menjelaskan kondisi yang telah diamati.

Pertanyaan yang ingin dijawab antara lain:

- Bagaimana nilai pengamatan NO₂, SO₂, dan CO pada wilayah penelitian?
- Bagaimana variasi nilai setiap polutan selama periode pengamatan?
- Apakah terdapat perubahan atau pola tertentu pada data polutan?
- Bagaimana perbedaan karakteristik antara ketiga jenis polutan yang diamati?

### Diagnostic Analytics

Analisis juga dapat memberikan indikasi awal ketika ditemukan nilai atau pola yang berbeda pada periode tertentu. Namun, untuk menyatakan penyebab suatu perubahan polutan diperlukan data tambahan, seperti kondisi meteorologi, aktivitas transportasi, kegiatan industri, penggunaan lahan, atau sumber emisi lainnya.

Oleh karena itu, proyek ini tidak secara langsung menyimpulkan bahwa suatu perubahan nilai polutan disebabkan oleh aktivitas tertentu hanya berdasarkan data satelit.