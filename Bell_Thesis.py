import streamlit as st
from PIL import Image

st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")

image = Image.open("404A4573.jpg")

st.image(image, width=10)