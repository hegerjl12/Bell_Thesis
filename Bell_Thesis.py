import streamlit as st
import pandas as pd
from PIL import Image
import random

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

i = random.randint(1,3)

while i is in image_order:
     i = random.randint(1,3)

st.write(image_order)

image = Image.open('image' + str(i) + '.jpg')

st.image(image, width=1024)

st.write('Enter 3 words you feel:')

image_input = st.text_area('','', key=i)  

submit = st.button('Submit', key=i+10, disabled=False)

if submit:
     words = image_input1.split()
     df = df.append({('Image'+str(i)): words[0]}, ignore_index = True)
     df = df.append({('Image'+str(i)): words[1]}, ignore_index = True)
     df = df.append({('Image'+str(i)): words[2]}, ignore_index = True)

     image_order.append(i)
