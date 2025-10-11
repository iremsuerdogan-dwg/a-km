import streamlit as st
import base64
from pathlib import Path

# Sayfa ayarları
st.set_page_config(page_title="Aşkım Uygulaması", page_icon="💙", layout="centered")

# Session state (hangi sayfada olduğumuzu tutmak için)
if "page" not in st.session_state:
    st.session_state.page = "mavi"

# --- SAYFA 1: MAVİ EKRAN ---
if st.session_state.page == "mavi":
    st.markdown(
        """
        <style>
        body {
            background-color: #007BFF;
        }
        div.stButton > button {
            background-color: white;
            color: #007BFF;
            border-radius: 20px;
            font-size: 20px;
            padding: 10px 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align:center; color:white;'>💙 canım karım 💙</h1>", unsafe_allow_html=True)
    if st.button("buraya bas aşkım"):
        st.session_state.page = "kırmızı"
        st.rerun()


# --- SAYFA 2: KIRMIZI EKRAN ---
elif st.session_state.page == "kırmızı":
    st.markdown(
        """
        <style>
        body {
            background-color: #FF0000;
        }
        div.stButton > button {
            background-color: white;
            color: #FF0000;
            border-radius: 20px;
            font-size: 20px;
            padding: 10px 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align:center; color:white;'>❤️ bebeğim benim götünü yerim ❤️</h1>", unsafe_allow_html=True)
    if st.button("buraya da bas aşkım"):
        img_path = Path("aa.jpg")

        if img_path.exists():
            with open(img_path, "rb") as f:
                img_bytes = f.read()
                img_base64 = base64.b64encode(img_bytes).decode()
                img_html = f'<img src="data:image/jpeg;base64,{img_base64}" width="100%" />'
                st.markdown(img_html, unsafe_allow_html=True)
        else:
            st.error("aa.jpg dosyası bulunamadı! Lütfen proje klasörüne ekle.")
