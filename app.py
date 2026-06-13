import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. Konfigurasi Halaman Web (Mode Lebar Penuh)
st.set_page_config(
    page_title="Naval Meteorology & Oceanography Command",
    page_icon="⛈️",
    layout="wide",
)

# Kustomisasi CSS: Merapatkan jarak atas dan Sidebar Gelap
st.markdown("""
    <style>
        /* Mengurangi padding atas bawaan Streamlit */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
        }
        
        /* Kustomisasi Sidebar */
        [data-testid="stSidebar"] {
            background-color: #222222;
            color: #ffffff;
        }
        hr {
            margin-top: 1rem;
            margin-bottom: 1rem;
            border: 0;
            border-top: 1px solid #444;
        }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk membaca gambar lokal dan mengubahnya ke Base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

# Daftar file banner yang ada di folder Anda
image_paths = [
    "assetdashboard/banner_atas1.png",
    "assetdashboard/banner_atas2.png",
    "assetdashboard/banner_atas3.png"
]

# Mengumpulkan tag gambar HTML
slides_html = ""
for path in image_paths:
    img_b64 = get_base64_image(path)
    if img_b64:
         slides_html += f'<div class="swiper-slide"><img src="data:image/png;base64,{img_b64}" /></div>\n'

# 2. Menampilkan Banner Carousel dengan Swiper.js
if slides_html:
    carousel_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />
      <style>
        html, body {{
          margin: 0; padding: 0; background: transparent; height: 100%;
        }}
        .swiper {{
          width: 100%; 
          height: 100%; 
          overflow: hidden;
        }}
        .swiper-slide {{
          display: flex; justify-content: center; align-items: flex-start; background: transparent;
        }}
        .swiper-slide img {{
          display: block; 
          width: 100%; /* Memaksa gambar melebar penuh ke layar */
          height: auto; /* Tinggi menyesuaikan secara proporsional, anti peyang */
          object-fit: contain; 
        }}
        .swiper-button-next, .swiper-button-prev {{
          color: #ffffff !important; 
          text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
          transform: scale(0.7);
        }}
        .swiper-pagination-bullet {{
          background: #ffffff !important; opacity: 0.7;
        }}
        .swiper-pagination-bullet-active {{
          opacity: 1;
        }}
      </style>
    </head>
    <body>
      <div class="swiper mySwiper">
        <div class="swiper-wrapper">
          {slides_html}
        </div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-pagination"></div>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
      <script>
        var swiper = new Swiper(".mySwiper", {{
          spaceBetween: 0,
          centeredSlides: true,
          loop: true,
          autoplay: {{
            delay: 4000, 
            disableOnInteraction: false, 
          }},
          pagination: {{
            el: ".swiper-pagination",
            clickable: true,
          }},
          navigation: {{
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
          }},
        }});
      </script>
    </body>
    </html>
    """
    # TINGGI KONTRIBUTOR DINAIKKAN KE 400
    # Karena gambarnya sekarang utuh dan proporsional, tingginya secara otomatis akan memakan ruang lebih banyak.
    # Jika bagian bawah aspal masih terpotong di layar Anda, naikkan angka 400 ini menjadi 450 atau 500.
    components.html(carousel_html, height=400)
else:
    st.warning("⚠️ Menunggu gambar diunggah. Pastikan file banner_atas1.png, banner_atas2.png, dan banner_atas3.png sudah berada di dalam folder 'assetdashboard'.")


# 3. Struktur Navigasi Kiri (Sidebar)
with st.sidebar:
    st.markdown("### **Navigation**")
    st.write("---")
    st.markdown("#### <a href='#jtwc' style='color: white; text-decoration: none;'>JTWC</a>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("#### <a href='#fnmoc' style='color: white; text-decoration: none;'>FWC-SD</a>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("#### <a href='#fnmoc' style='color: white; text-decoration: none;'>FWC-N</a>", unsafe_allow_html=True)
    st.write("---")

# 4. Konten Utama Website
st.markdown("<div style='background-color: #333333; color: white; padding: 10px; border-radius: 5px;'><b>Naval Meteorology & Oceanography Command | Public Facing</b></div>", unsafe_allow_html=True)
st.markdown("## Naval Meteorology & Oceanography Command | Public Facing Website")

st.write(
    "**The United States Naval Meteorology and Oceanography Command (NMOC)** provides critical information "
    "from the ocean depths to the most distant reaches of space, meeting needs in the military, scientific, "
    "and civilian communities."
)
st.write("The following NMOC components make their products available to the public through this portal:")

st.write("")

# Konten JTWC
st.markdown("<div id='jtwc'></div>", unsafe_allow_html=True)
st.write(
    "The [Joint Typhoon Warning Center (JTWC)](#) is the U.S. Department of Defense agency "
    "responsible for issuing tropical cyclone warnings for the Pacific and Indian Oceans."
)
st.write("")

# Konten FNMOC
st.markdown("<div id='fnmoc'></div>", unsafe_allow_html=True)
st.write(
    "The [Fleet Numerical Meteorology and Oceanography Center (FNMOC)](#) provides the highest quality, most relevant and timely worldwide meteorology "
    "and oceanography support to U.S. and coalition forces from its Operations Center in Monterey, California."
)
