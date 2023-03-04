import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Define function to load Lottie JSON file from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

selected = option_menu(
    menu_title=None,
    options=["Home", "Project", "Contact", "About"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    local_css("style/style.css")

    # ---- LOAD ASSETS ----
    lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_M9p23l.json")

    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Hi, I am Marlon")
        st.title("A IT Specialist From Philippines")
        st.write(
            "IT Specialist with technical support and virtualization experience, skilled in Windows Server Administration, Active Directory, Network Administration, and Desktop Virtualization. Proficient in Hyper-V, Proxmox, Azure AD, AWS, and Office 365 Admin Portal. Experienced in working with Windows, Mac, and Ubuntu. Skilled in Remote Monitoring and Management tools VSA, ConnectWise Control, IT Glue, ThreatLocker, 2FA, and OPENVPN. Proficient in Network-Attached Storage (NAS), CCTV Installation, and NVR/DVR. Strong problem-solving skills and commitment to customer service."
        )
        st.write("[Learn More >](https://www.linkedin.com/in/marlon-argente/)")

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                I Like Testing new Soptware on my Create HomeLab Server With Proxmox and other Projects:
                - Install Proxmox Server as My HomeLab Server.
                - Install and Test RMM tool VSA, ConnectWise Control, ITarian, currently testing Action1.
                - Install and Test PFsense with OpenVPN, and setup OpenVPN Cloud On and NAT connectors for Server 2019 to access Onprem Devices on Hyper-V.
                - Azure AD Migration on Active Directory OnPrem Via Connect Sysc. On Hyper-V
                - EC2 AWS Create test 2 Instance and enable ICMP to ping each other.
				- Install Server 2019 Active Directory and Creating Domain User and adding Info and Group Policy.
				- Assign license in office 365 Admin Portal and other app such as Mail, Office E3,E5, Teams.
				- Install and TEST DATTO BACKUP.
				- Have hands on IT Glue and ConnectWise Manage por ticketing.
				- Beginner on Python, Poetry, Github, Render.
                """
            )
            st.write("[More >](https://www.linkedin.com/in/marlon-argente/)")
        with right_column:
            st_lottie(lottie_hello, height=300, key="coding")

if selected == "Project":
    st.title(f"Under Construction {selected}")
if selected == "Contact":
    st.title(f"Under Construction {selected}")
if selected == "About":
    lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_M9p23l.json")

    st.title(f"About {selected}")
    st.title("Under Construction")
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=None,
        width=None,
        key=None,
    )
    st_lottie(lottie_hello, key="hello")