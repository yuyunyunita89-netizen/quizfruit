import streamlit as st
import random

# Judul aplikasi
st.title("🍎 Game Tebak Buah-Buahan 🍌")
st.write("Tebak nama buah berdasarkan petunjuk yang diberikan!")

# Daftar buah dan petunjuk
buah = {
    "apel": "Buah ini berwarna merah atau hijau dan sering dijadikan jus.",
    "pisang": "Buah kuning panjang yang kaya potassium.",
    "jeruk": "Buah ini berwarna oranye dan terkenal dengan vitamin C-nya.",
    "mangga": "Buah tropis ini berwarna kuning oranye dan manis.",
    "anggur": "Buah kecil yang bisa berwarna ungu, hijau, atau merah, sering dibuat jus atau wine."
}

# Session state untuk skor dan urutan buah
if "skor" not in st.session_state:
    st.session_state.skor = 0
if "daftar_buah" not in st.session_state:
    st.session_state.daftar_buah = list(buah.keys())
    random.shuffle(st.session_state.daftar_buah)
if "index_buah" not in st.session_state:
    st.session_state.index_buah = 0

# Ambil buah saat ini
if st.session_state.index_buah < len(st.session_state.daftar_buah):
    nama_buah = st.session_state.daftar_buah[st.session_state.index_buah]
    petunjuk = buah[nama_buah]

    st.write("Petunjuk:", petunjuk)
    tebakan = st.text_input("Tebak buah:")

    if st.button("Submit"):
        if tebakan.lower() == nama_buah:
            st.success("✅ Benar!")
            st.session_state.skor += 1
        else:
            st.error(f"❌ Salah! Jawaban yang benar adalah {nama_buah}")
        
        st.session_state.index_buah += 1
        st.experimental_rerun()
else:
    st.write(f"🎉 Permainan selesai! Skormu: {st.session_state.skor}/{len(buah)}")
    if st.button("Main Lagi"):
        st.session_state.skor = 0
        st.session_state.index_buah = 0
        st.session_state.daftar_buah = list(buah.keys())
        random.shuffle(st.session_state.daftar_buah)
        st.experimental_rerun()
