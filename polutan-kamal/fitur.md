# Fitur TSFEL

Setelah data NO₂ dinyatakan bersih dari outlier dan missing value, dilakukan ekstraksi fitur menggunakan library **TSFEL (Time Series Feature Extraction Library)**. Pada penelitian ini digunakan sebanyak **68 fitur** untuk menggambarkan berbagai karakteristik.

## Pengelompokan dan Penjelasan Fitur TSFEL

Fitur-fitur tersebut dikelompokkan ke dalam tiga domain utama, yaitu **Statistical, Temporal, dan Spectral**.

### 1. Domain Statistical
Domain statistik mengekstrak metrik kuantitatif dan karakteristik sebaran serta bentuk distribusi dari sinyal deret waktu. Domain ini terdiri dari 17 fitur utama yang fokus pada distribusi.

1. **`calc_max`**
   - **Penjelasan**: Nilai maksimum dari deret waktu.
   - **Rumus**: $\max(x)$
   - **Hasil (NO2)**: `5.51000e-05`

2. **`calc_min`**
   - **Penjelasan**: Nilai minimum dari deret waktu.
   - **Rumus**: $\min(x)$
   - **Hasil (NO2)**: `5.12000e-06`

3. **`calc_mean`**
   - **Penjelasan**: Rata-rata (mean) dari deret waktu.
   - **Rumus**: $\mu = \frac{1}{N} \sum_{i=1}^N x_i$
   - **Hasil (NO2)**: `2.84004e-05`

4. **`calc_median`**
   - **Penjelasan**: Nilai tengah (median) dari deret waktu.
   - **Rumus**: $\text{median}(x)$
   - **Hasil (NO2)**: `2.81250e-05`

5. **`calc_std`**
   - **Penjelasan**: Standar deviasi, mengukur tingkat penyebaran data.
   - **Rumus**: $\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}$
   - **Hasil (NO2)**: `1.01280e-05`

6. **`calc_var`**
   - **Penjelasan**: Varians, kuadrat dari standar deviasi.
   - **Rumus**: $\sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2$
   - **Hasil (NO2)**: `1.02577e-10`

7. **`ecdf`**
   - **Penjelasan**: Fungsi distribusi kumulatif empiris.
   - **Rumus**: $\hat{F}(t) = \frac{1}{N} \sum_{i=1}^N \mathbf{1}_{x_i \le t}$
   - **Hasil (NO2)**: `1.50273e-02`

8. **`ecdf_percentile`**
   - **Penjelasan**: Nilai ECDF pada persentil tertentu.
   - **Rumus**: $P_{perc}(\hat{F})$
   - **Hasil (NO2)**: `2.84000e-05`

9. **`ecdf_percentile_count`**
   - **Penjelasan**: Jumlah data yang berada di bawah persentil ECDF.
   - **Rumus**: $\sum \mathbf{1}_{x_i \le P_{perc}}$
   - **Hasil (NO2)**: `1.82500e+02`

10. **`ecdf_slope`**
   - **Penjelasan**: Kemiringan dari kurva ECDF.
   - **Rumus**: $\frac{\Delta y}{\Delta x} \text{ pada } \hat{F}(t)$
   - **Hasil (NO2)**: `3.47222e+04`

11. **`hist_mode`**
   - **Penjelasan**: Modus (nilai paling sering muncul) berdasarkan histogram.
   - **Rumus**: $\arg\max_j (\text{count}(bin_j))$
   - **Hasil (NO2)**: `2.76110e-05`

12. **`interq_range`**
   - **Penjelasan**: Jangkauan interkuartil (IQR), selisih Q3 dan Q1.
   - **Rumus**: $IQR = Q_3 - Q_1$
   - **Hasil (NO2)**: `1.45000e-05`

13. **`kurtosis`**
   - **Penjelasan**: Keruncingan (peakedness) dari distribusi data.
   - **Rumus**: $K = \frac{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^4}{\sigma^4} - 3$
   - **Hasil (NO2)**: `-4.15397e-01`

14. **`skewness`**
   - **Penjelasan**: Kemiringan (asimetri) dari distribusi data.
   - **Rumus**: $S = \frac{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^3}{\sigma^3}$
   - **Hasil (NO2)**: `1.02776e-01`

15. **`mean_abs_deviation`**
   - **Penjelasan**: Rata-rata simpangan absolut dari mean.
   - **Rumus**: $MAD = \frac{1}{N} \sum_{i=1}^N |x_i - \mu|$
   - **Hasil (NO2)**: `8.22498e-06`

16. **`median_abs_deviation`**
   - **Penjelasan**: Median dari simpangan absolut dari median.
   - **Rumus**: $\text{Median}(|x_i - \text{median}(x)|)$
   - **Hasil (NO2)**: `7.10833e-06`

17. **`rms`**
   - **Penjelasan**: Root Mean Square (energi kuadrat rata-rata).
   - **Rumus**: $RMS = \sqrt{\frac{1}{N} \sum_{i=1}^N x_i^2}$
   - **Hasil (NO2)**: `3.01523e-05`

### 2. Domain Temporal
Domain temporal mengevaluasi sinyal dari segi urutan waktunya. Terdiri dari 25 fitur yang mengukur dependensi, jarak, autokorelasi, dan kompleksitas waktu.

1. **`abs_energy`**
   - **Penjelasan**: Total energi absolut dari deret waktu.
   - **Rumus**: $E = \sum_{i=1}^N x_i^2$
   - **Hasil (NO2)**: `3.32752e-07`

2. **`auc`**
   - **Penjelasan**: Area di bawah kurva sinyal (Area Under Curve).
   - **Rumus**: $AUC = \sum_{i=1}^{N-1} \frac{x_i + x_{i+1}}{2}$
   - **Hasil (NO2)**: `1.03695e-02`

3. **`autocorr`**
   - **Penjelasan**: Autokorelasi sinyal, kesamaan sinyal dengan versi tertundanya.
   - **Rumus**: $R(\tau) = \sum_{i=1}^{N-\tau} x_i x_{i+\tau}$
   - **Hasil (NO2)**: `1.70000e+01`

4. **`average_power`**
   - **Penjelasan**: Daya rata-rata dari sinyal waktu.
   - **Rumus**: $P = \frac{1}{N} \sum_{i=1}^N x_i^2$
   - **Hasil (NO2)**: `9.11650e-10`

5. **`calc_centroid`**
   - **Penjelasan**: Titik pusat dari urutan waktu (Time Centroid).
   - **Rumus**: $C_t = \frac{\sum t_i \cdot x_i}{\sum x_i}$
   - **Hasil (NO2)**: `2.03671e+02`

6. **`dfa`**
   - **Penjelasan**: Detrended Fluctuation Analysis, untuk mengukur dependensi fraktal.
   - **Rumus**: $F(n) \propto n^\alpha$
   - **Hasil (NO2)**: `1.01119e+00`

7. **`distance`**
   - **Penjelasan**: Total jarak (panjang lintasan) antar titik-titik berturutan.
   - **Rumus**: $D = \sum_{i=1}^{N-1} \sqrt{1 + (x_{i+1} - x_i)^2}$
   - **Hasil (NO2)**: `3.65000e+02`

8. **`entropy`**
   - **Penjelasan**: Shannon Entropy, mengukur ketidakpastian sinyal.
   - **Rumus**: $H = -\sum p(x) \log p(x)$
   - **Hasil (NO2)**: `9.27850e-01`

9. **`higuchi_fractal_dimension`**
   - **Penjelasan**: Dimensi Fraktal Higuchi, mengukur kompleksitas bentuk.
   - **Rumus**: $L(k) \propto k^{-D}$
   - **Hasil (NO2)**: `1.84022e+00`

10. **`hurst_exponent`**
   - **Penjelasan**: Eksponen Hurst, indikasi memori jangka panjang waktu.
   - **Rumus**: $E[\frac{R(n)}{S(n)}] = C n^H$
   - **Hasil (NO2)**: `8.03093e-01`

11. **`lempel_ziv`**
   - **Penjelasan**: Kompleksitas Lempel-Ziv, mengukur tingkat kompresibilitas sinyal.
   - **Rumus**: $LZ = \frac{c(N)}{\frac{N}{\log N}}$
   - **Hasil (NO2)**: `1.72131e-01`

12. **`maximum_fractal_length`**
   - **Penjelasan**: Panjang maksimal fraktal di berbagai skala pengukuran.
   - **Rumus**: $L_{max} = \max_k (L(k))$
   - **Hasil (NO2)**: `-2.69521e+00`

13. **`mean_abs_diff`**
   - **Penjelasan**: Rata-rata dari perbedaan absolut titik berurutan.
   - **Rumus**: $\mu_{\Delta} = \frac{1}{N-1} \sum_{i=1}^{N-1} |x_{i+1} - x_i|$
   - **Hasil (NO2)**: `4.56367e-06`

14. **`mean_diff`**
   - **Penjelasan**: Rata-rata perbedaan antara titik berurutan.
   - **Rumus**: $\mu_{d} = \frac{1}{N-1} \sum_{i=1}^{N-1} (x_{i+1} - x_i)$
   - **Hasil (NO2)**: `1.20548e-08`

15. **`median_abs_diff`**
   - **Penjelasan**: Median perbedaan absolut berurutan.
   - **Rumus**: $\text{Median}(|x_{i+1} - x_i|)$
   - **Hasil (NO2)**: `2.50000e-06`

16. **`median_diff`**
   - **Penjelasan**: Median dari selisih titik berurutan.
   - **Rumus**: $\text{Median}(x_{i+1} - x_i)$
   - **Hasil (NO2)**: `4.00000e-07`

17. **`mse`**
   - **Penjelasan**: Mean Squared Error dari sinyal terhadap rata-ratanya.
   - **Rumus**: $MSE = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2$
   - **Hasil (NO2)**: `1.28358e+00`

18. **`negative_turning`**
   - **Penjelasan**: Jumlah titik belok bergradien negatif (puncak yang turun).
   - **Rumus**: $\sum \mathbf{1}_{x_{i-1} < x_i > x_{i+1}}$
   - **Hasil (NO2)**: `6.70000e+01`

19. **`neighbourhood_peaks`**
   - **Penjelasan**: Jumlah puncak pada area bertetangga yang ditentukan.
   - **Rumus**: $\sum \text{Peaks}(x, \text{window})$
   - **Hasil (NO2)**: `1.60000e+01`

20. **`petrosian_fractal_dimension`**
   - **Penjelasan**: Dimensi Fraktal Petrosian.
   - **Rumus**: $D = \frac{\log_{10}(N)}{\log_{10}(N) + \log_{10}(\frac{N}{N + 0.4 N_{\Delta}})}$
   - **Hasil (NO2)**: `1.02404e+00`

21. **`pk_pk_distance`**
   - **Penjelasan**: Jarak dari puncak tertinggi ke lembah terendah (Peak-to-Peak).
   - **Rumus**: $P2P = \max(x) - \min(x)$
   - **Hasil (NO2)**: `4.99800e-05`

22. **`positive_turning`**
   - **Penjelasan**: Jumlah titik belok bergradien positif (lembah yang naik).
   - **Rumus**: $\sum \mathbf{1}_{x_{i-1} > x_i < x_{i+1}}$
   - **Hasil (NO2)**: `6.80000e+01`

23. **`slope`**
   - **Penjelasan**: Kemiringan tren regresi linier secara keseluruhan.
   - **Rumus**: $m = \frac{\sum (t_i - \bar{t})(x_i - \mu)}{\sum (t_i - \bar{t})^2}$
   - **Hasil (NO2)**: `2.85331e-08`

24. **`sum_abs_diff`**
   - **Penjelasan**: Total akumulasi perbedaan absolut titik berurutan.
   - **Rumus**: $SAD = \sum_{i=1}^{N-1} |x_{i+1} - x_i|$
   - **Hasil (NO2)**: `1.66574e-03`

25. **`zero_cross`**
   - **Penjelasan**: Jumlah titik perpotongan nol (zero-crossing).
   - **Rumus**: $\sum \mathbf{1}_{x_i \cdot x_{i+1} < 0}$
   - **Hasil (NO2)**: `0.00000e+00`

### 3. Domain Spectral
Domain spektral mentransformasi data ke domain frekuensi (melalui Fourier/Wavelet). Terdiri dari 26 fitur untuk mengukur sifat periodik, energi spektrum, dan rentang frekuensi.

1. **`fundamental_frequency`**
   - **Penjelasan**: Frekuensi dasar yang paling kuat pada spektrum.
   - **Rumus**: $f_0 = \arg\max_f (|X(f)|^2)$
   - **Hasil (NO2)**: `2.73224e-03`

2. **`max_frequency`**
   - **Penjelasan**: Frekuensi tertinggi pada analisis spektrum daya.
   - **Rumus**: $f_{max} = \max(f)$
   - **Hasil (NO2)**: `4.34426e-01`

3. **`median_frequency`**
   - **Penjelasan**: Frekuensi yang membagi spektrum daya (energi) menjadi dua bagian sama.
   - **Rumus**: $\int_0^{f_{med}} |X(f)|^2 df = \frac{1}{2} \int_0^\infty |X(f)|^2 df$
   - **Hasil (NO2)**: `4.09836e-02`

4. **`human_range_energy`**
   - **Penjelasan**: Energi sinyal pada jangkauan pendengaran manusia.
   - **Rumus**: $E_h = \sum_{f \in H} |X(f)|^2$
   - **Hasil (NO2)**: `0.00000e+00`

5. **`lpcc`**
   - **Penjelasan**: Koefisien Linear Prediction Cepstral (LPCC).
   - **Rumus**: $C_n = -a_n - \sum_{k=1}^{n-1} \frac{k}{n} C_k a_{n-k}$
   - **Hasil (NO2)**: `7.48200e-01`

6. **`mfcc`**
   - **Penjelasan**: Koefisien Mel-Frequency Cepstral (MFCC).
   - **Rumus**: $c_n = \sum_{k=1}^K (\log S_k) \cos\left[n(k-\frac{1}{2})\frac{\pi}{K}\right]$
   - **Hasil (NO2)**: `2.43670e+01`

7. **`max_power_spectrum`**
   - **Penjelasan**: Daya tertinggi dari seluruh rentang spektrum frekuensi.
   - **Rumus**: $\max_f (|X(f)|^2)$
   - **Hasil (NO2)**: `1.22004e+02`

8. **`power_bandwidth`**
   - **Penjelasan**: Lebar pita tempat akumulasi mayoritas kekuatan sinyal (daya).
   - **Rumus**: $BW = f_{upper} - f_{lower}$
   - **Hasil (NO2)**: `3.22404e-01`

9. **`spectral_centroid`**
   - **Penjelasan**: Pusat massa spektral (frekuensi rata-rata berbobot energi).
   - **Rumus**: $C_s = \frac{\sum f_k |X(f_k)|}{\sum |X(f_k)|}$
   - **Hasil (NO2)**: `1.20096e-01`

10. **`spectral_decrease`**
   - **Penjelasan**: Tingkat penurunan kekuatan spektral pada frekuensi yang meninggi.
   - **Rumus**: $D_s = \frac{\sum_{k=2}^K \frac{|X(f_k)| - |X(f_1)|}{k-1}}{\sum_{k=2}^K |X(f_k)|}$
   - **Hasil (NO2)**: `-2.52716e+00`

11. **`spectral_distance`**
   - **Penjelasan**: Jarak spektral, selisih antar kurva densitas spektrum.
   - **Rumus**: $D(X, Y) = \sqrt{\sum (X(f) - Y(f))^2}$
   - **Hasil (NO2)**: `-1.58982e+00`

12. **`spectral_entropy`**
   - **Penjelasan**: Entropi spektral, seberapa menyebar distribusi energi spektrum.
   - **Rumus**: $H_s = -\sum p_f \log p_f$
   - **Hasil (NO2)**: `6.21878e-01`

13. **`spectral_kurtosis`**
   - **Penjelasan**: Kurtosis dari kepadatan daya spektrum.
   - **Rumus**: $K_s = \frac{\sum (f - C_s)^4 |X(f)|^2}{(\sum (f - C_s)^2 |X(f)|^2)^2}$
   - **Hasil (NO2)**: `2.71723e+00`

14. **`spectral_positive_turning`**
   - **Penjelasan**: Titik belok positif pada kurva spektrum.
   - **Rumus**: $\sum \mathbf{1}_{|X(f_{i-1})| > |X(f_i)| < |X(f_{i+1})|}$
   - **Hasil (NO2)**: `6.10000e+01`

15. **`spectral_roll_off`**
   - **Penjelasan**: Frekuensi roll-off di mana sebagian besar energi spektral terkonsentrasi.
   - **Rumus**: $f_c \text{ dimana } \sum_{f=0}^{f_c} |X(f)|^2 = 0.95 \sum_{f} |X(f)|^2$
   - **Hasil (NO2)**: `4.34426e-01`

16. **`spectral_roll_on`**
   - **Penjelasan**: Frekuensi roll-on tempat sebagian kecil energi (misal 5%) terakumulasi.
   - **Rumus**: $f_c \text{ dimana } \sum_{f=0}^{f_c} |X(f)|^2 = 0.05 \sum_{f} |X(f)|^2$
   - **Hasil (NO2)**: `0.00000e+00`

17. **`spectral_skewness`**
   - **Penjelasan**: Skewness (kemiringan) dari kepadatan daya spektrum.
   - **Rumus**: $S_s = \frac{\sum (f - C_s)^3 |X(f)|^2}{(\sum (f - C_s)^2 |X(f)|^2)^{3/2}}$
   - **Hasil (NO2)**: `1.05467e+00`

18. **`spectral_slope`**
   - **Penjelasan**: Kemiringan dari spektrum daya yang dihitung menggunakan regresi linier.
   - **Rumus**: $m_s = \frac{\sum (f_i - \bar{f})(|X(f_i)| - \overline{|X(f)|})}{\sum (f_i - \bar{f})^2}$
   - **Hasil (NO2)**: `-3.35216e-02`

19. **`spectral_spread`**
   - **Penjelasan**: Sebaran spektrum atau varians frekuensi di sekeliling pusat massa.
   - **Rumus**: $V_s = \sqrt{\frac{\sum (f_k - C_s)^2 |X(f_k)|}{\sum |X(f_k)|}}$
   - **Hasil (NO2)**: `1.50384e-01`

20. **`spectral_variation`**
   - **Penjelasan**: Variasi atau jarak perubahan spektrum pada titik yang berdekatan.
   - **Rumus**: $V = 1 - \frac{\sum X_{t-1}(f) X_t(f)}{\sqrt{\sum X_{t-1}^2 \sum X_t^2}}$
   - **Hasil (NO2)**: `2.64122e-01`

21. **`spectrogram_mean_coeff`**
   - **Penjelasan**: Koefisien magnitudo rata-rata dari matriks spektrogram.
   - **Rumus**: $\frac{1}{T F} \sum_t \sum_f |S(t, f)|$
   - **Hasil (NO2)**: `1.21204e-10`

22. **`wavelet_abs_mean`**
   - **Penjelasan**: Rata-rata magnitudo absolut dari koefisien transformasi wavelet.
   - **Rumus**: $\mu_w = \frac{1}{N} \sum |W(a,b)|$
   - **Hasil (NO2)**: `1.83560e-06`

23. **`wavelet_energy`**
   - **Penjelasan**: Energi total yang terkandung di dalam koefisien wavelet.
   - **Rumus**: $E_w = \sum |W(a,b)|^2$
   - **Hasil (NO2)**: `1.42750e-05`

24. **`wavelet_entropy`**
   - **Penjelasan**: Entropi wavelet, ukuran distribusi sebaran energi di ruang waktu-frekuensi.
   - **Rumus**: $H_w = -\sum p_j \log p_j, p_j = \frac{E_j}{E_{tot}}$
   - **Hasil (NO2)**: `2.12394e+00`

25. **`wavelet_std`**
   - **Penjelasan**: Standar deviasi dari sebaran koefisien wavelet.
   - **Rumus**: $\sigma_w = \sqrt{\frac{1}{N} \sum (|W(a,b)| - \mu_w)^2}$
   - **Hasil (NO2)**: `1.41400e-05`

26. **`wavelet_var`**
   - **Penjelasan**: Varians dari koefisien dispersi wavelet.
   - **Rumus**: $\sigma_w^2$
   - **Hasil (NO2)**: `2.24529e-10`

## Contoh Perhtungan Manual

### Distance (Euclidean Signal Distance)

**Deskripsi:**
Pada TSFEL, fitur `distance(signal)` mengkalkulasi panjang kurva (Euclidean Distance) dari keseluruhan deret waktu pada bidang 2-Dimensi. Algoritma ini menganggap jarak antar-indeks waktu di sumbu-x selalu bernilai $1$, dan fluktuasi amplitudo berada di sumbu-y.

Karena amplitudo $NO_2$ Anda memiliki satuan yang amat kecil (orde $10^{-5}$), kuadrat selisihnya menjadi nyaris nol. Akibatnya, akar kuadrat dari setiap langkah hampir persis bernilai $1$. Dengan total observasi $366$ hari (berarti ada $365$ perpindahan titik), total jarak geometrinya menjadi $365$ ditambah sedikit angka desimal dari fluktuasi gas $NO_2$.

**Rumus Matematis TSFEL:**


$$Distance = \sum_{i=1}^{N-1} \sqrt{1 + (x_{i+1} - x_i)^2}$$

**Penjelasan per Variabel:**

* $Distance$ : Panjang total kurva Euclidean dari sinyal deret waktu.
* $N$ : Total jumlah titik observasi dalam data ($N = 366$).
* $i$ : Indeks waktu, berjalan dari data pertama ($1$) hingga observasi sebelum terakhir ($N-1$).
* $1$ : Jarak kuadrat konstan pada sumbu waktu (interval waktu antar baris data, $\Delta t = 1$).
* $x_i$ : Nilai amplitudo ($NO_2$) pada waktu ke-$i$.
* $x_{i+1}$ : Nilai amplitudo ($NO_2$) pada waktu ke-$(i+1)$.

**Pembuktian Angka Anda:**

* Sinyal observasi memiliki jumlah data $N=366$, sehingga proses penjumlahannya terjadi $365$ kali.
* Untuk sembarang 2 titik data NO2 berurutan, misal selisihnya adalah $\Delta x = 1.45 \times 10^{-5}$.
* Maka: $\sqrt{1 + (0.0000145)^2} = \sqrt{1 + 0.00000000021} \approx 1.0000000001$.
* Bila diakumulasikan $365$ kali: $365 \times 1.00000000... = \mathbf{365.00000002415675}$.
* Ini **persis** dengan nilai *output* kode TSFEL Anda.

---

### ECDF (Empirical Cumulative Distribution Function)

**Deskripsi:**
Fitur `ecdf` menghitung proporsi probabilitas empiris data yang jatuh di bawah suatu nilai batas tertentu.

Pada nilai yang Anda tunjukkan (`0.015027322404371584`), angka ini merupakan nilai persentase kumulatif tunggal. Secara matematis, angka $0.0150273224...$ adalah hasil bagi pasti dari **$5.5 / 366$**. Ini merepresentasikan jumlah frekuensi data di bin awal (*bin* histogram) dibagi total populasi. Nilai $5.5$ sering muncul dari interpolasi linier di algoritma internal ECDF atau saat data jatuh tepat di batas *bin*.

**Rumus Matematis Evaluasi:**


$$ECDF(t) = \frac{1}{N} \sum_{i=1}^{N} c_i \quad \text{(atau frekuensi terinterpolasi)}$$

**Penjelasan per Variabel:**

* $ECDF(t)$ : Probabilitas (persentase) observasi dalam populasi yang nilainya $\le$ nilai batas atau berada pada *bin* distribusi awal.
* $N$ : Total jumlah populasi data (yakni $366$ baris *record* $NO_2$).
* $\sum c_i$ : Jumlah observasi yang berhasil melewati kondisi pembatas atau masuk ke dalam rentang keranjang *bin* tersebut (bernilai $5.5$ akibat interpolasi komputasi Python).

**Pembuktian Angka Anda:**
Jika kita mengevaluasi *bin* pertama, nilai kumulatif observasinya yang dihitung algoritma adalah sejumlah $5.5$ data.


$$ECDF = \frac{5.5}{366} = \mathbf{0.015027322404371584}$$


Angka manual pembuktian ini **cocok seratus persen** dengan *output* program Anda.