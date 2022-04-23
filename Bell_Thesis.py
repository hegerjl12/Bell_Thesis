import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from deta import Deta
import random

# set page config details
st.set_page_config(
     page_title="Lina's Thesis Experiment",
     page_icon="🔔",
     layout="wide",
)

st.title("Clear your mind...")
st.write("")
st.write("")

# create image container and text container
image_container = st.empty()
input_container = st.empty()

# create state variables 
if 'images_left' not in st.session_state:
     st.session_state.images_left = [1, 2, 3]

if 'i' not in st.session_state:
     st.session_state.i = 1

if 'last_image' not in st.session_state:
     st.session_state.last_image = []

if 'text1' not in st.session_state:
     st.session_state.text1 = ""

if 'text2' not in st.session_state:
     st.session_state.text2 = ""

if 'text3' not in st.session_state:
     st.session_state.text3 = ""

if 'submitted' not in st.session_state:
     st.session_state.submitted = False

if 'count' not in st.session_state:
     st.session_state.count = 0


# set selected image to the image container
def set_image():
     st.session_state.count = st.session_state.count + 1
     if len(st.session_state.images_left) > 0:
          st.session_state.i = random.choice(st.session_state.images_left)
          image = Image.open('image' + str(st.session_state.i) + '.jpg')
          with image_container.container():
               st.image(image, width=360, use_column_width='auto')
               st.write("Enter the first three words that come to your mind: ")

          # remove last image
               st.session_state.last_image.append(st.session_state.i)
               st.session_state.images_left.remove(st.session_state.i)
     else:
          image_container.empty()

def commit_words(text1, text2, text3):

     if st.session_state.last_image[-2] == 1:
          Image1DB.put({"words": text1})
          Image1DB.put({"words": text2})
          Image1DB.put({"words": text3})
     if st.session_state.last_image[-2] == 2:
          Image2DB.put({"words": text1})
          Image2DB.put({"words": text2})
          Image2DB.put({"words": text3})
     if st.session_state.last_image[-2] == 3:
          Image3DB.put({"words": text1})
          Image3DB.put({"words": text2})
          Image3DB.put({"words": text3})

def commit_wordsFinal(text1, text2, text3):

     if st.session_state.last_image[-1] == 1:
          Image1DB.put({"words": text1})
          Image1DB.put({"words": text2})
          Image1DB.put({"words": text3})
     if st.session_state.last_image[-1] == 2:
          Image2DB.put({"words": text1})
          Image2DB.put({"words": text2})
          Image2DB.put({"words": text3})
     if st.session_state.last_image[-1] == 3:
          Image3DB.put({"words": text1})
          Image3DB.put({"words": text2})
          Image3DB.put({"words": text3})

     
with st.spinner("Connecting to database..."):
          deta = Deta(st.secrets["deta_key"])
          Image1DB = deta.Base("testdb1")
          Image2DB = deta.Base("testdb2")
          Image3DB = deta.Base("testdb3")
          Image4DB = deta.Base("image4db")
          Image5DB = deta.Base("image5db")

# loop to print images and collect input
#if len(st.session_state.images_left) > 0:

#st.write("Enter 3 words the image makes you feel: ")
set_image() 

#  text = st.text_input(label='')
#  commit_words(text, text, text, st.session_state.i)

with input_container.form('entries', clear_on_submit=True):
     st.session_state.text1 = st.text_input(label="",key=1)
     st.session_state.text2 = st.text_input(label="",key=2)
     st.session_state.text3 = st.text_input(label="",key=3)
     
     st.session_state.submitted = st.form_submit_button('Submit')

if st.session_state.submitted:
     if st.session_state.count < 4:
          commit_words(st.session_state.text1.lower(), st.session_state.text2.lower(), st.session_state.text3.lower())
     else:
          commit_wordsFinal(st.session_state.text1.lower(), st.session_state.text2.lower(), st.session_state.text3.lower())
          input_container.empty()
          st.write("Thank you!")
          st.stop()
