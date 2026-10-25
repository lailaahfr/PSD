# Data Understanding

Data Understanding merupakan tahap untuk mengenali dan memahami data yang digunakan sebelum masuk ke proses pengolahan dan analisis lebih lanjut. Pada tahap ini dilakukan identifikasi sumber data, wilayah dan periode pengamatan, struktur data, kelengkapan nilai, karakteristik distribusi, serta pola awal yang terdapat pada data.

Dalam proyek ini, data yang dianalisis merupakan hasil pengamatan satelit **Sentinel-5P** untuk tiga polutan utama, yaitu **karbon monoksida (CO)**, **nitrogen dioksida (NO₂)**, dan **sulfur dioksida (SO₂)**.

## Sumber Data

Data polutan udara diperoleh melalui **Copernicus Data Space Ecosystem** pada [dataspace.copernicus.eu](https://dataspace.copernicus.eu/). Data berasal dari pengamatan satelit **Sentinel-5P** yang diakses menggunakan layanan **openEO**.

Sentinel-5P membawa instrumen **TROPOMI (Tropospheric Monitoring Instrument)** yang digunakan untuk melakukan pengamatan berbagai komponen atmosfer. Pada proyek ini digunakan koleksi **Sentinel-5P Level-2 (`SENTINEL_5P_L2`)** dengan tiga parameter:

| Variabel | Polutan | Representasi |
|---|---|---|
| `CO` | Karbon Monoksida | Total kolom CO |
| `NO2` | Nitrogen Dioksida | Kolom troposfer NO₂ |
| `SO2` | Sulfur Dioksida | Total kolom SO₂ |

Nilai yang diperoleh dari Sentinel-5P merupakan pengukuran pada **kolom atmosfer**, sehingga tidak secara langsung sama dengan konsentrasi polutan yang diukur oleh stasiun kualitas udara di permukaan.

Periode pengamatan pada proyek ini adalah **31 Agustus 2025 sampai 31 Agustus 2026**.

## Penentuan Wilayah Pengamatan

Wilayah pengamatan ditentukan menggunakan **Area of Interest (AOI)**. AOI digunakan untuk membatasi pengambilan data agar hanya mencakup wilayah **Kamal, Bangkalan**.

Batas AOI dibentuk dalam format **GeoJSON Polygon**. Koordinat polygon menggunakan susunan `[longitude, latitude]`. Penentuan koordinat dapat dilakukan menggunakan alat bantu pemetaan seperti [geojson.io](https://geojson.io/).

Batas spasial yang digunakan pada implementasi adalah:

| Atribut | Nilai | Keterangan |
|---|---:|---|
| `west` | 112.6883396 | Longitude terkecil |
| `south` | -7.174627 | Latitude terkecil |
| `east` | 112.7587724 | Longitude terbesar |
| `north` | -7.1108073 | Latitude terbesar |

AOI kemudian didefinisikan dalam Python sebagai berikut.

```python
aoi = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [112.7587724,-7.1108073],
            [112.6883396,-7.1108073],
            [112.6883396,-7.174627],
            [112.7587724,-7.174627],
            [112.7587724,-7.1108073]
          ]
        ]
      }
    }
  ]
}
```

Dengan AOI tersebut, proses pengambilan data dapat dibatasi pada wilayah kajian sehingga data di luar batas pengamatan tidak ikut diproses.
## Pengumpulan Data

### Instalasi Library

Pengambilan data Sentinel-5P dilakukan menggunakan library `openeo`. Library ini digunakan untuk berkomunikasi dengan backend openEO pada Copernicus Data Space Ecosystem.

```python
!pip install openeo
```

Library kemudian diimpor ke dalam notebook.

```python
import openeo
import pandas as pd
import matplotlib.pyplot as plt
```

### Koneksi dan Autentikasi

Langkah berikutnya adalah menghubungkan Python dengan backend openEO Copernicus Data Space Ecosystem.

```python
connection = openeo.connect(
    "openeo.dataspace.copernicus.eu"
).authenticate_oidc()
```
```
Visit https://identity.dataspace.copernicus.eu/auth/realms/CDSE/device?user_code=JTRO-IJCZ 📋 to authenticate.
✅ Authorized successfully
Authenticated using device code flow.
```

Setelah kode dijalankan, proses autentikasi dilakukan menggunakan akun Copernicus Data Space Ecosystem.

Autentikasi diperlukan sebelum pengguna dapat mengakses dan menjalankan proses pengolahan data pada infrastruktur openEO.

## Pengambilan Data Sentinel-5P

Pengambilan data dilakukan secara terpisah untuk masing-masing polutan. Pada setiap data dilakukan dua proses agregasi:

1. **Agregasi temporal**, yaitu menghitung nilai rata-rata pengamatan dalam periode harian.
2. **Agregasi spasial**, yaitu menghitung nilai rata-rata seluruh pengamatan yang berada di dalam AOI.

Dengan proses tersebut, hasil akhirnya berupa deret waktu yang mewakili **nilai rata-rata harian polutan pada wilayah pengamatan**.

### Nitrogen Dioksida (NO₂)

Data NO₂ dimuat dari koleksi `SENTINEL_5P_L2` dengan band `NO2`.

```python
s5NO2 = connection.load_collection(
    "SENTINEL_5P_L2",
    temporal_extent=["2025-08-31", "2026-08-31"],
    spatial_extent={
        "west": 112.6883396,
        "south": -7.174627,
        "east": 112.7587724,
        "north": -7.1108073
    },
    bands=["NO2"],
)
```

Data kemudian diagregasi menjadi nilai rata-rata harian.

```python
s5p_NO2_daily = s5NO2.aggregate_temporal_period(reducer="mean",period="day")
```

Selanjutnya dilakukan agregasi spasial berdasarkan AOI.

```python
s5p_NO2_aoi = s5p_NO2_daily.aggregate_spatial(reducer="mean",geometries=aoi)
```

Hasil pengolahan disimpan dalam format CSV.

```python
# Simpan hasil sebagai CSV
result_NO2 = s5p_NO2_aoi.save_result(format="CSV")

# Jalankan job
job_NO2 = result_NO2.create_job(title="s5p_NO2_timeseries")
job_NO2.start_and_wait()

# Download CSV
job_NO2.get_results().download_files("mystorage/Kec.Kamal/N02_Kamal")
```

### Karbon Monoksida (CO)

Proses yang sama diterapkan pada band `CO`.

```python
s5CO = connection.load_collection(
    "SENTINEL_5P_L2",
    temporal_extent=["2025-08-31", "2026-08-31"],
    spatial_extent={
        "west": 112.6883396,
        "south": -7.174627,
        "east": 112.7587724,
        "north": -7.1108073
    },
    bands=["CO"],
)
```

Agregasi temporal dilakukan untuk memperoleh rata-rata harian.

```python
s5p_CO_daily = s5CO.aggregate_temporal_period(reducer="mean",period="day")
```

Kemudian dilakukan agregasi berdasarkan wilayah AOI.

```python
s5p_CO_aoi = s5p_CO_daily.aggregate_spatial(reducer="mean",geometries=aoi)
```

Data kemudian disimpan sebagai CSV.

```python
# Simpan hasil sebagai CSV
result_CO = s5p_CO_aoi.save_result(format="CSV")

# Jalankan job
job_CO = result_CO.create_job(title="s5p__timeseries")
job_CO.start_and_wait()

# Download CSV
job_CO.get_results().download_files("mystorage/Kec.Kamal/CO_Kamal")
```
### Sulfur Dioksida (SO₂)

Untuk SO₂ digunakan band `SO2`.

```python
s5SO2 = connection.load_collection(
    "SENTINEL_5P_L2",
    temporal_extent=["2025-08-31", "2026-08-31"],
    spatial_extent={
        "west": 112.6883396,
        "south": -7.174627,
        "east": 112.7587724,
        "north": -7.1108073
    },
    bands=["SO2"],
)
```

Data diagregasi secara temporal menjadi rata-rata harian.

```python
s5p_SO2_daily = s5SO2.aggregate_temporal_period(reducer="mean",period="day")
```

Selanjutnya dilakukan agregasi spasial pada AOI.

```python
s5p_SO2_aoi = s5p_SO2_daily.aggregate_spatial(reducer="mean",geometries=aoi)
```

Hasil kemudian disimpan dalam format CSV.

```python
# Simpan hasil sebagai CSV
result_SO2 = s5p_SO2_aoi.save_result(format="CSV")

# Jalankan job
job_SO2 = result_SO2.create_job(title="s5p_SO2_timeseries")
job_SO2.start_and_wait()

# Download CSV
job_SO2.get_results().download_files("mystorage/Kec.Kamal/SO2_Kamal")
```

Dengan proses tersebut, masing-masing polutan menghasilkan satu dataset deret waktu yang berisi nilai rata-rata pengamatan setiap hari pada wilayah **Kamal, Bangkalan**.

## Mengenali Data Hasil Pengumpulan
Setelah proses pengambilan selesai, ketiga file CSV dibaca menggunakan `pandas`.

```python
import pandas as pd

# Membaca masing-masing data polutan
df_CO = pd.read_csv("mystorage/Kec.Kamal/CO_Kamal/timeseries.csv")
df_NO2 = pd.read_csv("mystorage/Kec.Kamal/N02_Kamal/timeseries.csv")
df_SO2 = pd.read_csv("mystorage/Kec.Kamal/SO2_Kamal/timeseries.csv")
```

Beberapa baris awal ditampilkan untuk mengetahui struktur data yang diperoleh.

```python
print("CO:")
display(df_CO.head(5))

print("NO₂:")
display(df_NO2.head(5))

print("SO₂:")
display(df_SO2.head(5))
```

Pemeriksaan awal ini digunakan untuk memastikan bahwa masing-masing dataset memiliki informasi waktu dan nilai polutan yang dibutuhkan.

## Eksplorasi Data

Setelah struktur data diketahui, dilakukan eksplorasi untuk memahami kondisi data sebelum dilakukan transformasi atau ekstraksi fitur.

### Pemeriksaan Missing Values

Tidak semua tanggal pengamatan satelit selalu menghasilkan nilai yang tersedia. Oleh karena itu, pemeriksaan **missing value** diperlukan untuk mengetahui kelengkapan masing-masing dataset.

```python
missing_CO = df_CO["CO"].isna().sum()
missing_NO2 = df_NO2["NO2"].isna().sum()
missing_SO2 = df_SO2["SO2"].isna().sum()

print("Missing values CO  :", missing_CO)
print("Missing values NO₂ :", missing_NO2)
print("Missing values SO₂ :", missing_SO2)
```

Agar lebih mudah dibandingkan, hasil pemeriksaan dapat dirangkum ke dalam tabel.

```python
missing_summary = pd.DataFrame({
    "Polutan": ["CO", "NO2", "SO2"],
    "Missing Value": [
        missing_CO,
        missing_NO2,
        missing_SO2
    ],
    "Jumlah Data": [
        len(df_CO),
        len(df_NO2),
        len(df_SO2)
    ]
})

missing_summary["Persentase Missing (%)"] = (
    missing_summary["Missing Value"]
    / missing_summary["Jumlah Data"]
    * 100
).round(2)

display(missing_summary)
```

Nilai kosong tidak langsung dianggap sebagai nilai `0`. Missing value menunjukkan bahwa pada waktu tertentu tidak tersedia nilai pengamatan yang dapat digunakan.

Keberadaan missing value akan menjadi pertimbangan pada tahap pengolahan data berikutnya.

### Menggabungkan Data Polutan

Untuk memudahkan proses eksplorasi, ketiga dataset digabungkan berdasarkan tanggal.

Pertama, kolom tanggal diubah menjadi tipe `datetime`.

```python
df_CO["date"] = pd.to_datetime(
    df_CO["date"]
)

df_NO2["date"] = pd.to_datetime(
    df_NO2["date"]
)

df_SO2["date"] = pd.to_datetime(
    df_SO2["date"]
)
```

Selanjutnya ketiga dataset digabungkan menggunakan `outer join`.

```python
df = df_CO[["date", "CO"]].merge(
    df_NO2[["date", "NO2"]],
    on="date",
    how="outer"
).merge(
    df_SO2[["date", "SO2"]],
    on="date",
    how="outer"
)
```

Data kemudian diurutkan berdasarkan tanggal.

```python
df = (
    df
    .sort_values("date")
    .reset_index(drop=True)
)

display(df.head())
```

Penggunaan `outer join` mempertahankan seluruh tanggal yang tersedia meskipun salah satu polutan tidak memiliki nilai pada tanggal tersebut.

### Statistik Deskriptif

Statistik deskriptif digunakan untuk memperoleh gambaran awal mengenai distribusi nilai CO, NO₂, dan SO₂.

```python
df[["CO", "NO2", "SO2"]].describe().T
```

Beberapa informasi yang diperoleh meliputi:

- `count` menunjukkan jumlah data yang tersedia,
- `mean` menunjukkan nilai rata-rata,
- `std` menunjukkan variasi nilai,
- `min` dan `max` menunjukkan nilai terendah dan tertinggi,
- serta kuartil 25%, 50%, dan 75%.

Statistik ini digunakan untuk mengenali karakteristik awal data dan bukan untuk menentukan secara langsung apakah kondisi kualitas udara termasuk baik atau buruk.

## Identifikasi Outlier

**Outlier** merupakan nilai pengamatan yang berada cukup jauh dari sebagian besar distribusi data.

Dalam konteks data polutan, nilai yang tinggi tidak selalu menunjukkan kesalahan. Nilai tersebut dapat berasal dari kondisi atmosfer atau kejadian tertentu pada waktu pengamatan. Oleh karena itu, pada tahap Data Understanding, outlier **hanya diidentifikasi dan tidak langsung dihapus**.

Metode yang digunakan adalah **Interquartile Range (IQR)**.Implementasinya adalah sebagai berikut.

```python
polutan = ["CO", "NO2", "SO2"]

hasil_outlier = []
data_outlier = {}

for kolom in polutan:

    data = df[
        ["date", kolom]
    ].dropna()

    Q1 = data[kolom].quantile(0.25)
    Q3 = data[kolom].quantile(0.75)

    IQR = Q3 - Q1

    batas_bawah = Q1 - 1.5 * IQR
    batas_atas = Q3 + 1.5 * IQR

    outlier = data[
        (data[kolom] < batas_bawah)
        |
        (data[kolom] > batas_atas)
    ]

    hasil_outlier.append({
        "Polutan": kolom,
        "Jumlah Data": len(data),
        "Q1": Q1,
        "Q3": Q3,
        "IQR": IQR,
        "Batas Bawah": batas_bawah,
        "Batas Atas": batas_atas,
        "Jumlah Outlier": len(outlier)
    })

    data_outlier[kolom] = (
        outlier
        .sort_values(
            by=kolom,
            ascending=False
        )
    )
```

Ringkasan hasil identifikasi ditampilkan dalam bentuk tabel.

```python
outlier_summary = pd.DataFrame(
    hasil_outlier
)

print("=== OUTLIER ===")
display(outlier_summary)
```

Tabel tersebut menunjukkan jumlah outlier pada setiap polutan beserta nilai Q1, Q3, IQR, batas bawah, dan batas atas yang digunakan.

### Visualisasi Outlier

Distribusi data dapat diamati lebih mudah menggunakan **boxplot**.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

df[
    ["CO", "NO2", "SO2"]
].boxplot()

plt.title(
    "Distribusi dan Outlier Data Polutan"
)

plt.xlabel("Polutan")
plt.ylabel("Nilai Pengamatan (mol/m²)")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.show()
```

Titik yang berada di luar *whisker* pada boxplot menunjukkan nilai yang secara statistik teridentifikasi sebagai outlier berdasarkan distribusi masing-masing variabel.

Namun, hasil ini belum cukup untuk menyatakan bahwa nilai tersebut merupakan kesalahan data. Oleh karena itu, data outlier tetap dipertahankan pada tahap Data Understanding.

## Visualisasi Time Series

Visualisasi **time series** digunakan untuk mengamati perubahan nilai masing-masing polutan dari waktu ke waktu.

Data yang digunakan merupakan data harian pada periode **31 Agustus 2025 sampai 31 Agustus 2026**.

Sebelum divisualisasikan, data dipastikan telah diurutkan berdasarkan tanggal.

```python
df["date"] = pd.to_datetime(
    df["date"]
)

df = df.sort_values("date")
```

### Time Series CO

```python
plt.figure(figsize=(14, 5))

plt.plot(
    df["date"],
    df["CO"],
    linewidth=1
)

plt.title(
    "Time Series Harian CO di Kamal, Bangkalan"
)

plt.xlabel("Tanggal")
plt.ylabel("CO (mol/m²)")

plt.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
```

Grafik digunakan untuk melihat perubahan nilai CO selama periode pengamatan, termasuk periode dengan peningkatan, penurunan, atau data yang tidak tersedia.

### Time Series NO₂

```python
plt.figure(figsize=(14, 5))

plt.plot(
    df["date"],
    df["NO2"],
    linewidth=1
)

plt.title(
    "Time Series Harian NO₂ di Kamal, Bangkalan"
)

plt.xlabel("Tanggal")
plt.ylabel("NO₂ (mol/m²)")

plt.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
```

Visualisasi memberikan gambaran mengenai variasi nilai NO₂ dari satu waktu pengamatan ke waktu berikutnya.

### Time Series SO₂

```python
plt.figure(figsize=(14, 5))

plt.plot(
    df["date"],
    df["SO2"],
    linewidth=1
)

plt.title(
    "Time Series Harian SO₂ di Kamal, Bangkalan"
)

plt.xlabel("Tanggal")
plt.ylabel("SO₂ (mol/m²)")

plt.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
```

Grafik SO₂ digunakan untuk mengamati variasi nilai pengamatan serta keberadaan nilai yang relatif tinggi atau rendah selama periode penelitian.