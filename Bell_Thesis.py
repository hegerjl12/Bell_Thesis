import streamlit as st
from PIL import Image

st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")

image = Image.open('404A4573.jpg')

st.image(image, width=1024)

image1_inputs = []

image1_input.append(st.text_input('Enter 5 words you feel:', '', key=1))
image1_input2 = st.text_input('','', key=2)
image1_input3 = st.text_input('','', key=3)
image1_input4 = st.text_input('','', key=4)
image1_input5 = st.text_input('','', key=5)