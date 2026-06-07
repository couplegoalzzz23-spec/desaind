import streamlit as st

# 1. Konfigurasi Halaman Web (Mode Lebar Penuh)
st.set_page_config(
    page_title="Naval Meteorology & Oceanography Command",
    page_icon="⛈️",
    layout="wide",
)

# Kustomisasi Warna Sidebar via CSS agar Taktis/Gelap
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1a1a1a;
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

# 2. Menampilkan Banner Canva yang Baru Saja Anda Upload
st.image("assetdashboard/banner_atas.png", use_container_width=True)
st.write("---")

# 3. Struktur Navigasi Kiri (Sidebar)
with st.sidebar:
    st.markdown("## **Navigation**")
    st.write("---")
    st.markdown("### [**JTWC**](#jtwc)")
    st.write("---")
    st.markdown("### [**FNMOC (FWC-SD)**](#fnmoc)")
    st.write("---")

# 4. Konten Utama Website
st.markdown("#### **Naval Meteorology & Oceanography Command | Public Facing**")
st.title("Naval Meteorology & Oceanography Command | Public Facing Website")

st.write(
    "The **United States Naval Meteorology and Oceanography Command (NMOC)** provides critical information "
    "from the ocean depths to the most distant reaches of space, meeting needs in the military, scientific, "
    "and civilian communities."
)
st.write("The following NMOC components make their products available to the public through this portal:")
st.write("---")

# Konten JTWC
st.markdown("<div id='jtwc'></div>", unsafe_allow_html=True)
st.subheader("The Joint Typhoon Warning Center (JTWC)")
st.write(
    "The Joint Typhoon Warning Center (JTWC) is the U.S. Department of Defense agency "
    "responsible for issuing tropical cyclone warnings for the Pacific and Indian Oceans."
)
st.write("---")

# Konten FNMOC
st.markdown("<div id='fnmoc'></div>", unsafe_allow_html=True)
st.subheader("The Fleet Numerical Meteorology and Oceanography Center (FNMOC)")
st.write(
    "FNMOC provides the highest quality, most relevant and timely worldwide meteorology "
    "and oceanography support to U.S. and coalition forces."
)
