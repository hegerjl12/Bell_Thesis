import streamlit as st
import pandas as pd
from PIL import Image
import random

@st.cache
def run_image_1(which_image):
     which_image = random.randint(1,3)
     return which_image

@st.cache
def run_image_2(which_image):
     which_image = random.randint(1,3)
     return which_image

@st.cache
def run_image_3(which_image):
     which_image = random.randint(1,3)
     return which_image

@st.cache
def run_image_4(which_image):
     which_image = random.randint(1,3)
     return which_image

@st.cache
def run_image_5(which_image):
     which_image = random.randint(1,3)
     return which_image


st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")

df = pd.DataFrame(columns = ['Image1', 'Image2', 'Image3', 'Image4', 'Image5'])

which_image = 0
done_images = []

which_image = run_image_1(which_image)

image = Image.open('image' + str(which_image) + '.jpg')

st.image(image, width=1024)

st.write('Enter 5 words you feel:')

image_input1 = st.text_input('','', key=1)  
image_input2 = st.text_input('','', key=2)
image_input3 = st.text_input('','', key=3)
image_input4 = st.text_input('','', key=4)
image_input5 = st.text_input('','', key=5)

submit = False

if image_input and image_input2 and image_input3 and image_input4 and image_input5:
     submit = st.button('Submit', key=6, disabled=False)

if submit:
     df = df.append({'Image1' : image_input1}, ignore_index = True)
     df = df.append({'Image1' : image_input2}, ignore_index = True)
     df = df.append({'Image1' : image_input3}, ignore_index = True)
     df = df.append({'Image1' : image_input4}, ignore_index = True)
     df = df.append({'Image1' : image_input5}, ignore_index = True)

     done_images.append(which_image)

which_image = run_image_2(which_image)

image = Image.open('image' + str(which_image) + '.jpg')

st.image(image, width=1024)

st.write('Enter 5 words you feel:')

image_input1 = st.text_input('','', key=1)  
image_input2 = st.text_input('','', key=2)
image_input3 = st.text_input('','', key=3)
image_input4 = st.text_input('','', key=4)
image_input5 = st.text_input('','', key=5)

submit = False

if image_input1 and image_input2 and image_input3 and image_input4 and image_input5:
     submit = st.button('Submit', key=6, disabled=False)

if submit:
     df = df.append({'Image2' : image_input1}, ignore_index = True)
     df = df.append({'Image2' : image_input2}, ignore_index = True)
     df = df.append({'Image2' : image_input3}, ignore_index = True)
     df = df.append({'Image2' : image_input4}, ignore_index = True)
     df = df.append({'Image2' : image_input5}, ignore_index = True)

     done_images.append(which_image)
