import streamlit as st
sys.path.insert(1, "C:\Users\Neko\Desktop\Portfolio\streamlit_option_menu")
from streamlit_option_menu import option_menu


with st.sidebar:
	selected = option_menu(
		menu_title="Main Menu",
		options=["Home", "Project", "Contact"],
	)

if selected == "Home":
	st.title(f"You have selected {selected}")
if selected == "Project":
	st.title(f"You have selected {selected}")
if selected == "Contact":
	st.title(f"You have selected {selected}")