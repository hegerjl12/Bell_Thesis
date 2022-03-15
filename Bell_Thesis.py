import streamlit as st
import pandas as pd
from PIL import Image
import random


st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")

if 'df' not in st.session_state:
     st.session_state.df = pd.DataFrame(columns = ['Image1', 'Image2', 'Image3', 'Image4', 'Image5', 'Image6', 'Image7', 'Image8', 'Image9', 'Image10'])

if 'image_order' not in st.session_state:
     st.session_state.image_order = []
     
if 'i' not in st.session_state:
     st.session_state.i = random.randint(1,3)


st.write(st.session_state.image_order)

image = Image.open('image' + str(st.session_state.i) + '.jpg')

st.image(image, width=1024)

st.write('Enter 3 words you feel:')

image_input = st.text_area('','', key=i)  

submit = st.button('Submit', key=st.session_state.i+10, disabled=False)

if submit:
     words = image_input.split()
     st.session_state.df = st.session_state.df.append({('Image'+str(st.session_state.i)): words[0]}, ignore_index = True)
     st.session_state.df = st.session_state.df.append({('Image'+str(st.session_state.i)): words[1]}, ignore_index = True)
     st.session_state.df = st.session_state.df.append({('Image'+str(st.session_state.i)): words[2]}, ignore_index = True)

     while st.session_state.i in st.session_state.image_order:
          st.session_state.i = random.randint(1,3)
          
     st.session_state.image_order.append(st.session_state.i)
     st.session_state.i = random.randint(1,3)

     st.write(st.session_state.df)