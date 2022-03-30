import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from deta import Deta
import random

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

def connect_databases():
     # connect to databases
     with st.spinner("Connecting to database..."):
          deta = Deta(st.secrets["deta_key"])
          Image1DB = deta.Base("image1db")
          Image2DB = deta.Base("image2db")
          Image3DB = deta.Base("image3db")
          Image4DB = deta.Base("image4db")
          Image5DB = deta.Base("image5db")

def commit_to_database():
     if st.session_state.i == 1:
          Image1DB.put({"words": st.session_state.text1})
          Image1DB.put({"words": st.session_state.text2})
          Image1DB.put({"words": st.session_state.text3})
     if st.session_state.i == 2:
          Image2DB.put({"words": st.session_state.text1})
          Image2DB.put({"words": st.session_state.text2})
          Image2DB.put({"words": st.session_state.text3})
     if st.session_state.i == 3:
          Image3DB.put({"words": st.session_state.text1})
          Image3DB.put({"words": st.session_state.text2})
          Image3DB.put({"words": st.session_state.text3})

connect_databases()

# loop to print images and collect input
if len(st.session_state.images_left) > 0:

     st.write("Enter 3 words you the image makes you feel: ")
     set_image() 

     form = st.form('wordForm')
     st.session_state.text1 = form.text_input('','', key=st.session_state.i+10)
     st.session_state.text2 = form.text_input('','', key=st.session_state.i+20)
     st.session_state.text3 = form.text_input('','', key=st.session_state.i+30)


     submit = form.form_submit_button('Submit', on_click=commit_to_database)

     st.write(st.session_state.text1+"?")

else:
     st.write("Thank you!")