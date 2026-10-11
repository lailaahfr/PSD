"""Dashboard evaluasi klasifikasi tutupan lahan Jawa Timur (KNN + Sentinel-2).

Jalankan dari direktori proyek: streamlit run streamlit_app.py
Semua hasil diambil dari folder hasil/; aplikasi ini tidak melatih model.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Klasifikasi Tutupan Lahan Jawa Timur",
    page_icon="🛰️",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
HASIL_DIR = BASE_DIR / "C:\\project\\PSD\\hasil"


def cari_file(*pilihan: str) -> Path | None:
    """Cari file dari beberapa nama/path tanpa menggantungkan working directory."""
    for nama in pilihan:
        file = BASE_DIR / nama
        if file.is_file():
            return file
    return None


@st.cache_data(show_spinner=False)
def baca_metrik(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("metrik_knn.json harus berisi objek JSON.")
    return data


@st.cache_data(show_spinner=False)
def baca_tabel(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Kolom benar dari CSV mungkin dibaca sebagai string/boolean.
    if "benar" in df.columns:
        nilai = df["benar"].astype("string").str.strip().str.lower()
        df["status" ] = nilai.map({
            "true": "Benar", "1": "Benar", "1.0": "Benar",
            "false": "Salah", "0": "Salah", "0.0": "Salah",
        }).fillna("Belum dievaluasi")
    elif {"kelas_aktual", "kelas_prediksi"}.issubset(df.columns):
        dapat_dinilai = df["kelas_aktual"].notna() & df["kelas_prediksi"].notna()
        df["status"] = "Belum dievaluasi"
        df.loc[dapat_dinilai, "status"] = (
            df.loc[dapat_dinilai, "kelas_aktual"]
            == df.loc[dapat_dinilai, "kelas_prediksi"]
        ).map({True: "Benar", False: "Salah"})
    else:
        df["status"] = "Belum dievaluasi"
    return df


def persen(value) -> str:
    try:
        return f"{float(value):.2%}"
    except (TypeError, ValueError):
        return "—"


def tampil_peta(path: Path, tinggi: int) -> None:
    # HTML Folium harus dibuat dan disimpan oleh notebook sebelumnya.
    html = path.read_text(encoding="utf-8")
    components.html(html, height=tinggi, scrolling=True)


st.title("🛰️ Klasifikasi Tutupan Lahan Jawa Timur")
st.caption("Sentinel-2 Level-2A · K-Nearest Neighbors (KNN) · Enam kelas tutupan lahan")

FILE_METRIK = cari_file("hasil/metrik_knn.json", "metrik_knn.json")
FILE_TABEL = cari_file("hasil/evaluasi_poligon.csv", "evaluasi_poligon.csv")
PETA_EVALUASI = cari_file(
    "hasil/peta_evaluasi_knn.html",
    "peta_evaluasi_knn.html",
    "peta_evaluasi.html",
)
PETA_KLASIFIKASI = cari_file(
    "hasil/peta_klasifikasi_knn.html",
    "peta_klasifikasi_knn.html",
)

metrik = {}
if FILE_METRIK:
    try:
        metrik = baca_metrik(str(FILE_METRIK))
    except (OSError, ValueError, json.JSONDecodeError) as e:
        st.warning(f"Tidak bisa membaca metrik_knn.json: {e}")

tabel = pd.DataFrame()
if FILE_TABEL:
    try:
        tabel = baca_tabel(str(FILE_TABEL))
    except (OSError, ValueError, pd.errors.ParserError) as e:
        st.warning(f"Tidak bisa membaca evaluasi_poligon.csv: {e}")

teruji = tabel[tabel["status"].isin(["Benar", "Salah"])] if not tabel.empty else pd.DataFrame()
n_poligon = len(teruji) if not teruji.empty else 0
n_salah = int((teruji["status"] == "Salah").sum()) if not teruji.empty else 0

kolom = st.columns(4)
kolom[0].metric("Accuracy (piksel)", persen(metrik.get("accuracy")))
kolom[1].metric("F1 Macro (piksel)", persen(metrik.get("f1_macro")))
kolom[2].metric("Poligon dievaluasi", f"{n_poligon:,}" if FILE_TABEL else "—")
kolom[3].metric("Salah klasifikasi", f"{n_salah:,}" if FILE_TABEL else "—")

if not FILE_METRIK:
    st.info("Metrik belum tersedia. Simpan hasil evaluasi notebook ke hasil/metrik_knn.json agar Accuracy dan F1 tampil.")

st.sidebar.header("Pengaturan peta")
pilihan_tata_letak = st.sidebar.radio(
    "Tata letak",
    ["Atas-bawah", "Berdampingan", "Fokus satu peta"],
    index=0,
)
tinggi_peta = st.sidebar.slider("Tinggi peta (px)", 450, 900, 600, step=50)

st.sidebar.markdown("---")
st.sidebar.markdown("### Keterangan Kelas")

st.sidebar.markdown("""
- 🟡 **Sawah:** Lahan pertanian yang digunakan untuk budidaya padi.
- 🔴 **Bangunan:** Kawasan permukiman, gedung, dan infrastruktur.
- 🟢 **Hutan:** Kawasan yang didominasi pepohonan dan vegetasi rapat.
- 🔵 **Danau:** Perairan tawar seperti danau, ranu, dan waduk.
- 🔵 **Laut:** Wilayah perairan laut terbuka.
- 🟣 **Mangrove:** Vegetasi bakau yang tumbuh di kawasan pesisir.
""")

st.sidebar.caption(
    "Warna pada peta digunakan untuk membedakan "
    "enam kelas tutupan lahan di Jawa Timur."
)

import streamlit as st
from pathlib import Path

st.subheader("Confusion Matrix - KNN")

file_cm = Path("C:\\project\\PSD\\img\\image.png")

if file_cm.exists():
    st.image(
        str(file_cm),
        caption="Hasil Evaluasi Klasifikasi KNN",
        use_container_width=True
    )
else:
    st.warning("Confusion Matrix belum tersedia.")

st.subheader("Peta interaktif")
peta_tersedia = []
if PETA_EVALUASI:
    peta_tersedia.append(("Peta evaluasi poligon", PETA_EVALUASI))
if PETA_KLASIFIKASI:
    peta_tersedia.append(("Peta hasil klasifikasi", PETA_KLASIFIKASI))

if not peta_tersedia:
    st.warning(
        "File peta belum ditemukan. Simpan peta Folium dari notebook sebagai "
        "hasil/peta_evaluasi_knn.html, lalu refresh halaman."
    )
elif pilihan_tata_letak == "Fokus satu peta":
    nama_peta = st.selectbox("Pilih peta", [nama for nama, _ in peta_tersedia])
    path_peta = dict(peta_tersedia)[nama_peta]
    tampil_peta(path_peta, tinggi_peta)
elif pilihan_tata_letak == "Berdampingan" and len(peta_tersedia) == 2:
    kiri, kanan = st.columns(2)
    for tempat, (nama, path) in zip((kiri, kanan), peta_tersedia):
        with tempat:
            st.markdown(f"**{nama}**")
            tampil_peta(path, tinggi_peta)
else:
    for nama, path in peta_tersedia:
        st.markdown(f"**{nama}**")
        tampil_peta(path, tinggi_peta)

st.subheader("Tabel hasil evaluasi poligon")
if tabel.empty:
    st.info("File hasil/evaluasi_poligon.csv belum tersedia.")
else:
    status_tersedia = ["Semua"] + [
        x for x in ["Benar", "Salah", "Belum dievaluasi"]
        if x in tabel["status"].values
    ]
    status_filter = st.selectbox("Filter status prediksi", status_tersedia)
    tampil = tabel if status_filter == "Semua" else tabel[tabel["status"] == status_filter]
    st.dataframe(tampil, use_container_width=True, hide_index=True)
    st.download_button(
        "Unduh hasil evaluasi (CSV)",
        data=tampil.to_csv(index=False).encode("utf-8-sig"),
        file_name="evaluasi_poligon_knn.csv",
        mime="text/csv",
    )

st.caption(
    "Catatan: metrik Accuracy dan F1 diambil dari evaluasi piksel; tabel dan jumlah "
    "kesalahan menampilkan evaluasi per poligon. Keduanya merupakan unit analisis berbeda."
)
