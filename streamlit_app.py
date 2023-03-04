import streamlit as st
from streamlit_option_menu import option_menu



selected = option_menu(
		menu_title=None,
		options=["Home", "Project", "Contact"],
		icons=["house", "book", "envelope"],
	menu_icon="cast",
	default_index=0,
	orientation="horizontal",
	)

if selected == "Home":
	st.title(f"You have selected {selected}")
if selected == "Project":
	st.title(f"You have selected {selected}")
if selected == "Contact":
	st.title(f"You have selected {selected}")
if selected == "About":
	st.title(f"You have selected {selected}")