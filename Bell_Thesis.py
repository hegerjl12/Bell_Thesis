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

image1_input1 = st.text_input('Enter 5 words you feel:', '')
image1_input2 = st.text_input('','')
image1_input3 = st.text_input('','')
image1_input4 = st.text_input('','')
image1_input5 = st.text_input('','')