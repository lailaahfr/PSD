"""Dashboard evaluasi tutupan lahan Jawa Timur (Sentinel-2 + KNN).

Jalankan dari direktori proyek:
    python -m streamlit run streamlit_app.py

Aplikasi membaca hasil notebook; tidak melatih model ulang.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


# =============================================================================
# 1. KONFIGURASI
# =============================================================================
st.set_page_config(
    page_title="Klasifikasi Tutupan Lahan Jawa Timur",
    page_icon="🛰️",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
HASIL_DIR = BASE_DIR / "hasil"
IMG_DIR = BASE_DIR / "img"


def cari_file(*lokasi: Path) -> Path | None:
    """Ambil file pertama yang ada, tanpa bergantung pada working directory."""
    return next((p for p in lokasi if p.is_file()), None)


FILE_METRIK = cari_file(HASIL_DIR / "metrik_knn.json", BASE_DIR / "metrik_knn.json")
FILE_TABEL = cari_file(HASIL_DIR / "evaluasi_poligon.csv", BASE_DIR / "evaluasi_poligon.csv")
FILE_CM = cari_file(
    IMG_DIR / "image.png",                       # lokasi gambar pengguna
    HASIL_DIR / "confusion_matrix_knn.png",       # jika disimpan dari notebook
    IMG_DIR / "confusion_matrix_knn.png",
    HASIL_DIR / "image.png",
)
PETA_EVALUASI = cari_file(
    HASIL_DIR / "peta_evaluasi_knn.html",
    BASE_DIR / "peta_evaluasi_knn.html",
    HASIL_DIR / "peta_evaluasi.html",
    BASE_DIR / "peta_evaluasi.html",
)
PETA_KLASIFIKASI = cari_file(
    HASIL_DIR / "peta_klasifikasi_knn.html",
    BASE_DIR / "peta_klasifikasi_knn.html",
)


# =============================================================================
# 2. MEMBACA HASIL NOTEBOOK
# =============================================================================
@st.cache_data(show_spinner=False)
def baca_metrik(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Isi JSON harus berupa objek/dictionary.")
    return data


@st.cache_data(show_spinner=False)
def baca_tabel(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    if "benar" in data.columns:
        status = data["benar"].astype("string").str.strip().str.lower()
        data["status"] = status.map({
            "true": "Benar", "1": "Benar", "1.0": "Benar",
            "false": "Salah", "0": "Salah", "0.0": "Salah",
        }).fillna("Belum dievaluasi")
    elif {"kelas_aktual", "kelas_prediksi"}.issubset(data.columns):
        ada_prediksi = data["kelas_aktual"].notna() & data["kelas_prediksi"].notna()
        data["status"] = "Belum dievaluasi"
        data.loc[ada_prediksi, "status"] = (
            data.loc[ada_prediksi, "kelas_aktual"]
            == data.loc[ada_prediksi, "kelas_prediksi"]
        ).map({True: "Benar", False: "Salah"})
    else:
        data["status"] = "Belum dievaluasi"
    return data


def persen(angka: object) -> str:
    try:
        return f"{float(angka):.2%}"
    except (TypeError, ValueError):
        return "—"


def tampil_peta(path: Path, tinggi: int) -> None:
    components.html(path.read_text(encoding="utf-8"), height=tinggi, scrolling=True)


metrik = {}
if FILE_METRIK:
    try:
        metrik = baca_metrik(str(FILE_METRIK))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        st.warning(f"Gagal membaca metrik: {error}")

tabel = pd.DataFrame()
if FILE_TABEL:
    try:
        tabel = baca_tabel(str(FILE_TABEL))
    except (OSError, ValueError, pd.errors.ParserError) as error:
        st.warning(f"Gagal membaca tabel evaluasi: {error}")

poligon_teruji = (
    tabel[tabel["status"].isin(["Benar", "Salah"])]
    if not tabel.empty else pd.DataFrame()
)
n_teruji = len(poligon_teruji)
n_salah = (
    int((poligon_teruji["status"] == "Salah").sum())
    if not poligon_teruji.empty else 0
)


# =============================================================================
# 3. SIDEBAR
# =============================================================================
st.sidebar.header("Pengaturan Peta")
tata_letak = st.sidebar.radio(
    "Tata letak",
    ["Atas-bawah", "Berdampingan", "Fokus satu peta"],
)
tinggi_peta = st.sidebar.slider("Tinggi peta (px)", 450, 900, 600, step=50)

st.sidebar.markdown("---")
st.sidebar.markdown("### Keterangan Kelas")
st.sidebar.markdown("""
- 🟡 **Sawah:** Lahan pertanian padi.
- 🔴 **Bangunan:** Permukiman dan infrastruktur.
- 🟢 **Hutan:** Vegetasi dan pepohonan rapat.
- 🔵 **Danau:** Perairan tawar, ranu, dan waduk.
- 🌊 **Laut:** Perairan laut terbuka.
- 🟣 **Mangrove:** Vegetasi bakau di pesisir.
""")
st.sidebar.caption("Warna sebenarnya mengikuti legenda pada peta Folium.")


# =============================================================================
# 4. JUDUL DAN METRIK
# =============================================================================
st.title("🛰️ Klasifikasi Tutupan Lahan Jawa Timur")
st.caption("Sentinel-2 Level-2A · K-Nearest Neighbors (KNN) · 6 Kelas Tutupan Lahan")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Accuracy (piksel)", persen(metrik.get("accuracy")))
k2.metric("F1 Macro (piksel)", persen(metrik.get("f1_macro")))
k3.metric("Poligon dievaluasi", f"{n_teruji:,}" if FILE_TABEL else "—")
k4.metric("Salah klasifikasi", f"{n_salah:,}" if FILE_TABEL else "—")

if not FILE_METRIK:
    st.info("File hasil/metrik_knn.json belum tersedia.")


# =============================================================================
# 5. CONFUSION MATRIX
# =============================================================================
st.subheader("Confusion Matrix - KNN")
if FILE_CM:
    st.image(
        str(FILE_CM),
        caption="Confusion Matrix hasil evaluasi KNN",
        use_container_width=True,
    )
else:
    st.warning(
        "Gambar Confusion Matrix belum ditemukan. Simpan gambar pada "
        "img/image.png atau hasil/confusion_matrix_knn.png, "
        "kemudian refresh aplikasi."
    )


# =============================================================================
# 6. PETA INTERAKTIF
# =============================================================================
st.subheader("Peta Interaktif")
peta_tersedia = []
if PETA_EVALUASI:
    peta_tersedia.append(("Peta Evaluasi Poligon", PETA_EVALUASI))
if PETA_KLASIFIKASI:
    peta_tersedia.append(("Peta Hasil Klasifikasi", PETA_KLASIFIKASI))

if not peta_tersedia:
    st.warning("Peta belum tersedia. Simpan Folium ke hasil/peta_evaluasi_knn.html.")
elif tata_letak == "Fokus satu peta":
    nama = st.selectbox("Pilih peta", [item[0] for item in peta_tersedia])
    tampil_peta(dict(peta_tersedia)[nama], tinggi_peta)
elif tata_letak == "Berdampingan" and len(peta_tersedia) == 2:
    kiri, kanan = st.columns(2)
    for tempat, (nama, lokasi) in zip((kiri, kanan), peta_tersedia):
        with tempat:
            st.markdown(f"**{nama}**")
            tampil_peta(lokasi, tinggi_peta)
else:
    for nama, lokasi in peta_tersedia:
        st.markdown(f"**{nama}**")
        tampil_peta(lokasi, tinggi_peta)


# =============================================================================
# 7. TABEL EVALUASI POLIGON
# =============================================================================
st.subheader("Tabel Hasil Evaluasi Poligon")
if tabel.empty:
    st.info("File hasil/evaluasi_poligon.csv belum tersedia.")
else:
    opsi_status = ["Semua"] + [
        nama for nama in ["Benar", "Salah", "Belum dievaluasi"]
        if nama in tabel["status"].values
    ]
    status_dipilih = st.selectbox("Filter status prediksi", opsi_status)
    tabel_tampil = (
        tabel if status_dipilih == "Semua"
        else tabel[tabel["status"] == status_dipilih]
    )
    st.dataframe(tabel_tampil, use_container_width=True, hide_index=True)
    st.download_button(
        "Unduh Hasil Evaluasi (CSV)",
        data=tabel_tampil.to_csv(index=False).encode("utf-8-sig"),
        file_name="evaluasi_poligon_knn.csv",
        mime="text/csv",
    )

st.caption(
    "Accuracy/F1 dihitung pada tingkat piksel; jumlah poligon dan salah klasifikasi "
    "dihitung pada tingkat poligon."
)
