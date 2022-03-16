import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np


st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")
arr = np.arange(3)

if 'df' not in st.session_state:
     st.session_state.df = pd.DataFrame(columns = ['Image1', 'Image2', 'Image3', 'Image4', 'Image5', 'Image6', 'Image7', 'Image8', 'Image9', 'Image10'])

if 'image_order' not in st.session_state:
     st.session_state.image_order = [1, 2, 3]

if 'i' not in st.session_state:
     st.session_state.i = 1

if 'next' not in st.session_state:
     st.session_state.next = 0

if 'image_words' not in st.session_state:
     st.session_state.image_words = []

if st.session_state.i < 4:

     image = Image.open('image' + str(st.session_state.i) + '.jpg')

     st.image(image, width=1024)

     st.write('Enter 3 words you feel:')

     with st.form("Enter 3 words you feel: "):
          image_input = st.text_area('','', key=st.session_state.i)  
          submit = st.form_submit_button('Submit', key=st.session_state.i+10)

     if submit:
          words = image_input.split()
          st.session_state.image_words.append(words)

          st.write(st.session_state.image_words)

          st.session_state.i = st.session_state.i + 1

          image = Image.open('image' + str(st.session_state.i) + '.jpg')
          