import streamlit as st

def snow():
    st.snow()

st.set_page_config(layout="wide")
st.header('Hello, World')
st.button('Make it Snow', on_click=snow())