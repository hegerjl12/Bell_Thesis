import streamlit as st
import pandas as pd
from PIL import Image
import random

@st.cache
def run_image_order(image_order):
     while len(image_order) != 3:
          num = random.randint(1,3)
     
          if num not in image_order:
               image_order.append(num)

     return image_order


st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")

df = pd.DataFrame(columns = ['Image1', 'Image2', 'Image3', 'Image4', 'Image5', 'Image6', 'Image7', 'Image8', 'Image9', 'Image10'])

image_order = []

image_order = run_image_order(image_order)

for i in image_order:
     if i:
          image = Image.open('image1.jpg')

          st.image(image, width=1024)

          st.write('Enter 3 words you feel:')

          image_input1 = st.text_area('','', key=1)  

          submit1 = st.button('Submit', key=16, disabled=False)

          if submit1:
               words = image_input1.split()
               df = df.append({('Image1': words[0]}, ignore_index = True)
               df = df.append({('Image1': words[1]}, ignore_index = True)
               df = df.append({('Image1': words[2]}, ignore_index = True)
