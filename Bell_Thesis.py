import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from deta import Deta
import random
import time

# set page config details
st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

st.title("Selina's Thesis")

# create image container and text container
image_container = st.empty()

# create state variables 
if 'images_left' not in st.session_state:
     st.session_state.images_left = [1, 2, 3]

if 'i' not in st.session_state:
     st.session_state.i = 1

if 'text1' not in st.session_state:
     st.session_state.text1 = ""

if 'text2' not in st.session_state:
     st.session_state.text2 = ""

if 'text3' not in st.session_state:
     st.session_state.text3 = ""



# set selected image to the image container
def set_image():
     if len(st.session_state.images_left) > 0:
          st.session_state.i = random.choice(st.session_state.images_left)
          image = Image.open('image' + str(st.session_state.i) + '.jpg')
          with image_container.container():
               st.image(image, width=360, use_column_width='auto')

          # remove last image
               st.session_state.images_left.remove(st.session_state.i)

#with st.spinner("Connecting to database..."):
          #deta = Deta(st.secrets["deta_key"])
          #Image1DB = deta.Base("testdb1")
         # Image2DB = deta.Base("testdb2")
        #  Image3DB = deta.Base("testdb3")
         # Image4DB = deta.Base("image4db")
        #  Image5DB = deta.Base("image5db")

# loop to print images and collect input
if len(st.session_state.images_left) > 0:

     st.write("Enter 3 words you the image makes you feel: ")
     set_image() 
     text1 = st.text_input('', '', key='test')
     st.write(text1)
     with st.form(key='wordForm'+str(st.session_state.i)):
         # text1 = st.text_area('','', key=st.session_state.i+10)
          text2 = st.text_input('','', key=st.session_state.i+20)
          text3 = st.text_input('','', key=st.session_state.i+30)

          submit = st.form_submit_button('Submit')

     if submit:
          st.write(len(text1))
          if st.session_state.i == 1:
               st.write(text1)

            #   Image1DB.put({"words": text1})
               st.write(text2)
             #  Image1DB.put({"words": text2})
               st.write(text3)
              # Image1DB.put({"words": text3})
          if st.session_state.i == 2:
               st.write(text1)
              # Image2DB.put({"words": text1})
               st.write(text2)
              # Image2DB.put({"words": text2})
               st.write(text3)
              # Image2DB.put({"words": text3})
          if st.session_state.i == 3:
               st.write(text1)
              # Image3DB.put({"words": text1})
               st.write(text2)
              # Image3DB.put({"words": text2})
               st.write(text3)
              # Image3DB.put({"words": text3})

else:
     st.write("Thank you!")