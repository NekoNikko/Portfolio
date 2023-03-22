import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
import io

st. set_page_config(layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

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
    styles={
        "container": {"width": "100vw", "height": "100vh", "padding": "0", "margin": "0"},
        "icon": {"color": "orange", "font-size": "22px"}, 
        "nav-link": {"font-size": "22px", "text-align": "left", "margin":"0px", "--hover-color": "#9900ff"},
        "nav-link-selected": {"background-color": "#a928ff"},
    }
)

img_contact_form = Image.open("images/contact_form.png")
img_lottie_animation = Image.open("images/lottie_animation.png")






if selected == "Home":
    local_css("style/style.css")

    # ---- LOAD ASSETS ----
    lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_M9p23l.json")

    # ---- HEADER SECTION ----
    with st.container():

       
        
        st.subheader("Hi, I am Marlon")
        st.title("A IT Specialist From Philippines")
        st.write(
                """
                IT Specialist with technical support and virtualization experience, skilled in Windows Server Administration, Active Directory, Network Administration, and Desktop Virtualization.                 
                Proficient in Hyper-V, Proxmox, Azure AD, AWS, and Office 365 Admin Portal. Experienced in working with Windows, Mac, and Ubuntu.                       
                Skilled in Remote Monitoring and Management tools VSA, ConnectWise Control, IT Glue, ThreatLocker, 2FA, and OPENVPN.                    
                Proficient in Network-Attached Storage (NAS), CCTV Installation, and NVR/DVR. Strong problem-solving skills and commitment to customer service.!                 
                """
        )
        st.write("[Learn More >](https://ph.linkedin.com/in/marlon-argente-95a903195)")

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                 """
                I Like Testing new Software on my Create HomeLab Server with Proxmox and other Projects:                        
                - Install Proxmox Server as My HomeLab Server.                  
                - Install and Test RMM tool VSA, ConnectWise Control, ITarian, and currently testing Action1.                             
                - Install and Test PFsense with OpenVPN, and setup OpenVPN Cloud Onprem and NAT connectors for Server 2019 to access Onprem Devices on Hyper-V.             
                - Azure AD Migration on Active Directory OnPrem Via Connect Sysc. On Hyper-V
                - EC2 AWS Create test 2 Instance and enable ICMP to ping each other.                    
				- Install Server 2019 Active Directory and Creating Domain User and adding Info and Group Policy.                   
				- Assign license in office 365 Admin Portal and other app such as Mail, Office E3,E5, Teams.                    
				- Install and TEST DATTO BACKUP.                    
				- Have hands on IT Glue and ConnectWise Manage por ticketing.                   
				- Beginner on Python, Poetry, Github, Render.                   
                """
            )

            st.write("[More >](https://ph.linkedin.com/in/marlon-argente-95a903195)")
        with right_column:
            st_lottie(lottie_hello, height=450, key="coding")






if selected == "Project":
    st.title(f"Under Construction {selected}")

    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://ph.linkedin.com/in/marlon-argente-95a903195)")
        
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.subheader("How To Add A Contact Form To Your Streamlit App")
            st.write(
                """
                Want to add a contact form to your Streamlit website?
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                """
            )
            st.markdown("[Watch Video...](https://ph.linkedin.com/in/marlon-argente-95a903195)")







if selected == "Contact":
    st.title(f"Under Construction {selected}")

    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/b61ef26490bbc468e7fdff6223ec6ddf" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()






if selected == "About":
    st.title(f"{selected}")

    local_css("style/style.css")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.write(
                """
                Welcome to my About page! I am a IT Specialist beginer on Python developer who is passionate about creating programs and automating processes.                  
                This portfolio site is one of my beginner projects, which I built using the Python programming language, poetry for package management, Streamlit for the user interface,                                  
                and Render for deployment. Through this project, I have gained a deeper understanding of Python programming, and I am excited to further advance my skills in the areas of scripting,                          
                programing, and automation. Please feel free to browse my projects and get in touch if you are interested in collaborating or have any questions. Thank you for visiting!                           
                """
            )


        with right_column:
            # define the lottie_hello variable here
            lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ljotbiif.json")
            st_lottie(lottie_hello, height=450, key="coding")