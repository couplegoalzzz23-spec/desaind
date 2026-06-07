import streamlit as st

# 1. Konfigurasi Halaman (Lebar Penuh agar Mirip Website Resmi)
st.set_page_config(
    page_title="Naval Meteorology & Oceanography Command Clone",
    page_icon="⛈️",
    layout="wide", # Menggunakan mode lebar
)

# 2. Menampilkan Banner Atas dari Canva
# Pastikan file banner satu folder dengan script atau di folder 'assets'
st.image("assets/canva_banner_top.png", use_container_width=True)

st.write("---") # Garis pembatas horizontal

# 3. Membuat Struktur Navigasi Kiri (Sidebar)
with st.sidebar:
    st.markdown("## **Navigation**")
    st.write("---")
    
    # Contoh Menu dengan Logo dan Teks (Bisa menggunakan kolom)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("assets/logo_jtwc.png", width=50) # Logo dari Canva
    with col2:
        st.markdown("### [**JTWC**](#jtwc)")
        
    st.write("---")
    
    col3, col4 = st.columns([1, 3])
    with col3:
        st.image("assets/logo_fwcsd.png", width=50)
    with col4:
        st.markdown("### [**FWC-SD**](#fwc-sd)")

# 4. Membuat Konten Utama (Main Content)
st.subheader("Naval Meteorology & Oceanography Command | Public Facing Website")
st.title("Naval Meteorology & Oceanography Command | Public Facing")

st.markdown("""
The **United States Naval Meteorology and Oceanography Command (NMOC)** provides critical information 
from the ocean depths to the most distant reaches of space, meeting needs in the military, scientific, 
and civilian communities.

The following NMOC components make their products available to the public through this portal:
""")

# Menggunakan expander atau container untuk tiap komponen teks
st.markdown("### **The Joint Typhoon Warning Center (JTWC)**")
st.write(
    "The Joint Typhoon Warning Center (JTWC) is the U.S. Department of Defense agency "
    "responsible for issuing tropical cyclone warnings for the Pacific and Indian Oceans."
)

st.markdown("### **The Fleet Numerical Meteorology and Oceanography Center (FNMOC)**")
st.write(
    "FNMOC provides the highest quality, most relevant and timely worldwide meteorology "
    "and oceanography support to U.S. and coalition forces."
)
