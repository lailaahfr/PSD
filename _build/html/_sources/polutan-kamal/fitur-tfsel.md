# Pengelompokan dan Penjelasan Fitur TSFEL

Setelah data NO₂ dinyatakan bersih dari outlier dan missing value, dilakukan ekstraksi fitur menggunakan library **TSFEL (Time Series Feature Extraction Library)**. Pada penelitian ini digunakan sebanyak **68 fitur** untuk menggambarkan berbagai karakteristik deret waktu konsentrasi NO₂.

Fitur-fitur tersebut dikelompokkan ke dalam tiga domain utama, yaitu **Statistical, Temporal, dan Spectral**.

## 1. Statistical Domain

Statistical Domain berisi fitur yang menggambarkan karakteristik statistik, distribusi, penyebaran, perubahan nilai, serta energi dari data deret waktu.

1. **abs_energy** — mengukur total energi atau besarnya nilai sinyal berdasarkan kuadrat nilai-nilainya.
2. **auc** — menghitung luas area di bawah kurva deret waktu.
3. **average_power** — mengukur rata-rata daya atau energi sinyal.
4. **calc_max** — menentukan nilai maksimum dalam deret waktu.
5. **calc_mean** — menghitung nilai rata-rata.
6. **calc_median** — menentukan nilai tengah atau median.
7. **calc_min** — menentukan nilai minimum.
8. **calc_std** — menghitung standar deviasi untuk mengetahui tingkat penyebaran data.
9. **calc_var** — menghitung varians data.
10. **ecdf** — menghasilkan karakteristik distribusi kumulatif empiris dari data.
11. **ecdf_percentile** — menentukan persentil berdasarkan distribusi kumulatif empiris.
12. **ecdf_percentile_count** — menghitung jumlah data berdasarkan persentil tertentu.
13. **ecdf_slope** — menggambarkan perubahan atau kemiringan distribusi kumulatif empiris.
14. **entropy** — mengukur tingkat ketidakpastian atau kompleksitas distribusi nilai.
15. **hist_mode** — menentukan modus atau nilai yang paling dominan berdasarkan histogram.
16. **human_range_energy** — mengukur energi sinyal pada rentang tertentu yang berkaitan dengan rentang pengamatan manusia.
17. **interq_range** — menghitung rentang interkuartil atau selisih antara Q3 dan Q1.
18. **kurtosis** — menggambarkan tingkat keruncingan distribusi data.
19. **mean_abs_deviation** — menghitung rata-rata penyimpangan absolut terhadap nilai pusat.
20. **mean_abs_diff** — menghitung rata-rata selisih absolut antar nilai berurutan.
21. **mean_diff** — menghitung rata-rata perubahan atau selisih antar nilai.
22. **median_abs_deviation** — mengukur penyimpangan absolut median.
23. **median_abs_diff** — menghitung median dari selisih absolut antar nilai berurutan.
24. **median_diff** — menghitung median perubahan antar nilai berurutan.
25. **mse** — menghitung mean squared error atau rata-rata kuadrat kesalahan/perbedaan.
26. **pk_pk_distance** — mengukur jarak antara nilai puncak maksimum dan minimum.
27. **rms** — menghitung root mean square sebagai ukuran besarnya sinyal.
28. **skewness** — menggambarkan kemencengan distribusi data.
29. **slope** — mengukur kecenderungan naik atau turun pada deret waktu.
30. **sum_abs_diff** — menghitung jumlah seluruh selisih absolut antar nilai berurutan.

## 2. Temporal Domain

Temporal Domain berfokus pada pola perubahan data berdasarkan urutan waktu, hubungan antarobservasi, kompleksitas, serta karakteristik struktur temporal pada deret waktu.

31. **autocorr** — mengukur korelasi antara nilai deret waktu dengan nilai sebelumnya pada lag tertentu.
32. **dfa** — digunakan untuk menganalisis korelasi jangka panjang dan karakteristik fluktuasi pada deret waktu.
33. **distance** — mengukur karakteristik jarak atau perubahan sepanjang deret waktu.
34. **hurst_exponent** — menggambarkan kecenderungan deret waktu untuk mempertahankan atau membalik pola perubahan sebelumnya.
35. **lempel_ziv** — mengukur kompleksitas deret waktu berdasarkan pola atau urutan yang muncul.
36. **maximum_fractal_length** — mengukur panjang fraktal maksimum yang terbentuk dari deret waktu.
37. **neighbourhood_peaks** — mengidentifikasi karakteristik puncak lokal berdasarkan lingkungan atau titik di sekitarnya.
38. **negative_turning** — menghitung karakteristik titik perubahan arah ke arah negatif.
39. **positive_turning** — menghitung karakteristik titik perubahan arah ke arah positif.
40. **zero_cross** — menghitung jumlah atau karakteristik perpotongan sinyal terhadap nilai nol.
41. **calc_centroid** — menentukan pusat massa atau titik pusat distribusi sinyal.
42. **maximum_fractal_length** — menggambarkan karakteristik panjang maksimum struktur fraktal pada sinyal.

## 3. Spectral Domain

Spectral Domain menganalisis karakteristik data berdasarkan frekuensi. Domain ini digunakan untuk mengetahui distribusi energi, komponen frekuensi, serta karakteristik spektrum dari deret waktu NO₂.

43. **fundamental_frequency** — menentukan frekuensi dasar atau frekuensi utama dari sinyal.
44. **max_frequency** — menentukan frekuensi dengan nilai atau kontribusi maksimum.
45. **max_power_spectrum** — menentukan nilai daya maksimum pada spektrum frekuensi.
46. **median_frequency** — menentukan frekuensi median berdasarkan distribusi energi spektrum.
47. **power_bandwidth** — mengukur lebar rentang frekuensi yang membawa energi tertentu.
48. **spectral_centroid** — menentukan pusat distribusi energi pada spektrum frekuensi.
49. **spectral_decrease** — mengukur tingkat penurunan energi spektrum terhadap frekuensi.
50. **spectral_distance** — mengukur jarak atau perubahan karakteristik antarbagian spektrum.
51. **spectral_entropy** — mengukur tingkat ketidakpastian atau penyebaran energi pada spektrum.
52. **spectral_kurtosis** — menggambarkan keruncingan distribusi energi pada spektrum.
53. **spectral_positive_turning** — mengidentifikasi karakteristik perubahan arah positif pada spektrum.
54. **spectral_roll_off** — menentukan frekuensi batas tempat sebagian besar energi spektrum berada di bawahnya.
55. **spectral_roll_on** — menentukan frekuensi awal dari rentang energi spektrum.
56. **spectral_skewness** — menggambarkan kemencengan distribusi energi pada spektrum.
57. **spectral_slope** — mengukur kemiringan perubahan energi terhadap frekuensi.
58. **spectral_spread** — mengukur penyebaran energi di sekitar spectral centroid.
59. **spectral_variation** — mengukur perubahan karakteristik spektrum.
60. **spectrogram_mean_coeff** — menghitung karakteristik rata-rata koefisien pada spectrogram.
61. **wavelet_abs_mean** — menghitung rata-rata nilai absolut koefisien wavelet.
62. **wavelet_energy** — mengukur energi yang terdapat pada representasi wavelet.
63. **wavelet_entropy** — mengukur kompleksitas atau ketidakpastian distribusi energi pada koefisien wavelet.
64. **wavelet_std** — menghitung standar deviasi koefisien wavelet.
65. **wavelet_var** — menghitung varians koefisien wavelet.
66. **lpcc** — mengekstraksi karakteristik sinyal menggunakan Linear Predictive Cepstral Coefficients.
67. **mfcc** — mengekstraksi karakteristik sinyal menggunakan Mel-Frequency Cepstral Coefficients.
68. **higuchi_fractal_dimension** dan **petrosian_fractal_dimension** — mengukur kompleksitas atau dimensi fraktal dari deret waktu.

## Ringkasan

Secara keseluruhan, terdapat **68 fitur TSFEL** yang digunakan untuk menganalisis karakteristik deret waktu NO₂. Ketiga domain tersebut memberikan sudut pandang yang berbeda:

* **Statistical** → menggambarkan nilai, distribusi, penyebaran, dan perubahan statistik data.
* **Temporal** → menggambarkan pola, hubungan antarwaktu, kompleksitas, dan perubahan arah deret waktu.
* **Spectral** → menggambarkan karakteristik frekuensi, distribusi energi, spektrum, serta representasi wavelet.

Hasil ekstraksi 68 fitur kemudian disimpan dalam file CSV dan digunakan sebagai data masukan untuk tahap penyimpanan ke database Aiven.
