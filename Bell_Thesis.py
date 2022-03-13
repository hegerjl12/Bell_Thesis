import streamlit as st
import pandas as pd
from PIL import Image
import random

@st.cache
def run_image_order(image_order):
     first = random.randint(1,3)

     second = random.randint(1,3)
     while(first == second):
          second = random.randint(1,3)
     
     third = random.randint(1,3)
     while(third == first or third == second):
          third = random.randint(1,3)

     image_order.append(first)
     image_order.append(second)
     image_order.append(third)
     
     return image_order


st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")

df = pd.DataFrame(columns = ['Image1', 'Image2', 'Image3', 'Image4', 'Image5'])

image_order = []

image_order = run_image_order(image_order)

image = Image.open('image' + str(image_order[0]) + '.jpg')

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
     df = df.append({'Image1' : image_input1}, ignore_index = True)
     df = df.append({'Image1' : image_input2}, ignore_index = True)
     df = df.append({'Image1' : image_input3}, ignore_index = True)
     df = df.append({'Image1' : image_input4}, ignore_index = True)
     df = df.append({'Image1' : image_input5}, ignore_index = True)


image = Image.open('image' + str(image_order[1]) + '.jpg')

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

image = Image.open('image' + str(image_order[2]) + '.jpg')

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
     df = df.append({'Image3' : image_input1}, ignore_index = True)
     df = df.append({'Image3' : image_input2}, ignore_index = True)
     df = df.append({'Image3' : image_input3}, ignore_index = True)
     df = df.append({'Image3' : image_input4}, ignore_index = True)
     df = df.append({'Image3 : image_input5}, ignore_index = True)