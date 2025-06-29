
import streamlit as st

# Simpan data di session_state agar tidak hilang saat refresh
if "kontak" not in st.session_state:
    st.session_state.kontak = {}

st.title("📱 Buku Kontak Digital")

menu = st.radio("Pilih menu:", ["Tambah Kontak", "Lihat Semua Kontak", "Hapus Kontak"])

if menu == "Tambah Kontak":
    st.subheader("➕ Tambah Kontak Baru")
    nama = st.text_input("Nama")
    nomor = st.text_input("Nomor Telepon")

    if st.button("Simpan"):
        if nama and nomor:
            st.session_state.kontak[nama] = nomor
            st.success(f"Kontak {nama} disimpan.")
        else:
            st.warning("Mohon isi nama dan nomor telepon.")

elif menu == "Lihat Semua Kontak":
    st.subheader("📇 Daftar Kontak")
    if not st.session_state.kontak:
        st.info("Belum ada kontak yang disimpan.")
    else:
        for nama, nomor in st.session_state.kontak.items():
            st.write(f"**{nama}**: {nomor}")

elif menu == "Hapus Kontak":
    st.subheader("🗑️ Hapus Kontak")
    if not st.session_state.kontak:
        st.info("Belum ada kontak.")
    else:
        nama_dihapus = st.selectbox("Pilih kontak yang akan dihapus", list(st.session_state.kontak.keys()))
        if st.button("Hapus"):
            del st.session_state.kontak[nama_dihapus]
            st.success(f"Kontak {nama_dihapus} telah dihapus.")
