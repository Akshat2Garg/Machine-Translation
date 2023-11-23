import streamlit as st
from streamlit_option_menu import option_menu
import first, home, second

with st.sidebar:
    selected = option_menu(
            "Main Menu",
            ["Home", "English - French", "French - English"],
            icons=['house', 'phone', 'book'],
            menu_icon="cast",
            default_index=0,
        )

if selected == "Home":
    home.app()
elif selected == "English - French":
    first.app()
elif selected == "French - English":
    second.app()

