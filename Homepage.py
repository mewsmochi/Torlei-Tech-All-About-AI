import streamlit as st

st.set_page_config(page_title="Torlei AI Image Identifier")

st.sidebar.success("Select a page above!")

page_by_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://codehs.com/uploads/0531fad341ed0ae09a9e2f627ed498a0");
    background-size: cover;
    }
    </style>
"""

st.markdown(page_by_img, unsafe_allow_html=True)

