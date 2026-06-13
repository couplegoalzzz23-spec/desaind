import streamlit as st
import streamlit.components.v1 as components
import base64

# Konfigurasi Halaman
st.set_page_config(page_title="Naval Meteorology & Oceanography Command", layout="wide")

# CSS untuk memastikan padding Streamlit tidak memotong area banner
st.markdown("""
    <style>
        .block-container { padding-top: 1rem !important; }
        [data-testid="stSidebar"] { background-color: #222222; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

image_paths = ["assetdashboard/banner_atas1.png", "assetdashboard/banner_atas2.png", "assetdashboard/banner_atas3.png"]
slides_html = ""
for path in image_paths:
    img_b64 = get_base64_image(path)
    if img_b64:
         slides_html += f'<div class="swiper-slide"><img src="data:image/png;base64,{img_b64}" /></div>\n'

# PERBAIKAN: Menghapus batasan tinggi statis yang kaku dan menggunakan CSS agar gambar menyesuaikan secara proporsional
carousel_html = f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />
    <style>
        .swiper {{ width: 100%; height: auto; }}
        .swiper-slide img {{ 
            width: 100%; 
            height: auto; /* KUNCI: Biarkan tinggi mengikuti lebar secara proporsional agar tidak terpotong */
            display: block;
        }}
    </style>
    <div class="swiper mySwiper">
        <div class="swiper-wrapper">{slides_html}</div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-pagination"></div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
    <script>
        var swiper = new Swiper(".mySwiper", {{ loop: true, autoplay: {{ delay: 4000 }}, 
        pagination: {{ el: ".swiper-pagination" }}, navigation: {{ nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" }} }});
    </script>
"""

# Gunakan height yang cukup besar agar tidak memotong, 
# atau biarkan Streamlit mengelola secara otomatis
components.html(carousel_html, height=450)
