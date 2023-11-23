import streamlit as st
import pandas as pd
import re
from deep_translator import MyMemoryTranslator


def app():

    st.subheader("Enter the String:")
    string = st.text_input("")

    st.write('')
    if st.button("Enter"):
        res = MyMemoryTranslator(source="fr-FR", target='en-IN').translate(text=string)
        st.subheader("Translated String:")
        st.markdown(
            f'<div style="background-color: #f0f0f0; padding: 10px;color:#000000;font-size:24px;">{res.capitalize()}</div>',
            unsafe_allow_html=True)
