import streamlit as st

def generate_prompt(
    nama_karakter,
    umur,
    jenis_kelamin,
    kebangsaan,
    ciri_fisik,
    outfit,
    suara,
    ekspresi,
    lokasi,
    kegiatan_latar,
    properti_khusus,
    jenis_shot,
    aksi_karakter,
    dialog,
    sfx,
    durasi
):
    return f"""
KARAKTER UTAMA ({nama_karakter.upper()}, {umur} TAHUN)
- {jenis_kelamin} {kebangsaan}, umur {umur}, {ciri_fisik}.
- Outfit: {outfit}.
- Suara: {suara}.
- Ekspresi: {ekspresi}.

SHOT 1 – PERKENALAN USAHA (Durasi ± {durasi} detik)
Visual: {nama_karakter} berdiri di {lokasi}, {kegiatan_latar}, {properti_khusus}.
Angle: {jenis_shot}.

Aksi: {aksi_karakter}

Dialog {nama_karakter} berkata dalam bahasa Indonesia:
“{dialog}”

SFX: {sfx}

[NEGATIVE PROMPT]
Hindari: teks di layar, subtitle, font, logo, distorsi, artefak, anomali, wajah ganda, anggota badan cacat, tangan tidak normal, orang tambahan yang tidak relevan, objek mengganggu, kualitas rendah, buram, glitch, suara robotik, suara pecah.
"""

# UI
st.set_page_config(page_title="Prompt Generator", layout="wide")
st.title("🎬 Prompt Generator untuk VEO 3")

with st.form("prompt_form"):
    col1, col2 = st.columns(2)

    with col1:
        nama_karakter = st.text_input("Nama Karakter")
        umur = st.number_input("Umur", min_value=1, step=1)
        jenis_kelamin = st.text_input("Jenis Kelamin")
        kebangsaan = st.text_input("Kebangsaan")
        ciri_fisik = st.text_area("Ciri Fisik")
        outfit = st.text_input("Outfit")
        suara = st.text_area("Suara")
        ekspresi = st.text_area("Ekspresi")

    with col2:
        lokasi = st.text_input("Lokasi / Setting")
        kegiatan_latar = st.text_area("Kegiatan Latar Belakang")
        properti_khusus = st.text_input("Properti Khusus")
        jenis_shot = st.text_input("Jenis Shot")
        aksi_karakter = st.text_area("Aksi Karakter")
        dialog = st.text_area("Dialog")
        sfx = st.text_input("SFX / Ambience")
        durasi = st.number_input("Durasi (detik)", min_value=1, step=1)

    submitted = st.form_submit_button("🎥 Generate Prompt")

if submitted:
    if not all([nama_karakter, jenis_kelamin, kebangsaan, ciri_fisik, outfit, suara, ekspresi,
                lokasi, kegiatan_latar, properti_khusus, jenis_shot, aksi_karakter, dialog, sfx]):
        st.warning("Mohon isi semua kolom terlebih dahulu.")
    else:
        result = generate_prompt(
            nama_karakter, int(umur), jenis_kelamin, kebangsaan, ciri_fisik,
            outfit, suara, ekspresi, lokasi, kegiatan_latar, properti_khusus,
            jenis_shot, aksi_karakter, dialog, sfx, int(durasi)
        )
        st.subheader("📄 Prompt Anda")
        st.code(result, language="markdown")
