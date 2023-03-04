import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

selected = option_menu(
    menu_title=None,
    options=["Home", "Project", "Contact", "About"],
    icons=["house", "book", "envelope", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    st.title(f"You have selected {selected}")
elif selected == "Project":
    st.title(f"You have selected {selected}")
elif selected == "Contact":
    st.title(f"You have selected {selected}")
else:
    st.title(f"{selected}")
    st.title("This Site is Created On Streamlit With poetry, python, github, render and this is Compilation of MY works and Project")

    lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_M9p23l.json")
    st_lottie(lottie_hello, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key="hello")
