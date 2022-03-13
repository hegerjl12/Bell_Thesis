import streamlit as st
import pandas as pd
from PIL import Image
from random import seed
from random import randint

@st.cache
def run_image_order(image_order):
     seed(1)
     while len(image_order) == 3:
          num = random.randint(1,3)
     
          if num not in image_order:
               image_order.append(num)

     st.write(image_order)
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

image = Image.open('image' + str(image_order) + '.jpg')

st.image(image, width=1024)

st.write('Enter 5 words you feel:')

image_input1 = st.text_input('','', key=1)  
image_input2 = st.text_input('','', key=2)
image_input3 = st.text_input('','', key=3)
image_input4 = st.text_input('','', key=4)
image_input5 = st.text_input('','', key=5)

submit1 = False

if image_input1 and image_input2 and image_input3 and image_input4 and image_input5:
     submit = st.button('Submit', key=16, disabled=False)

if submit1:
     df = df.append({'Image1' : image_input1}, ignore_index = True)
     df = df.append({'Image1' : image_input2}, ignore_index = True)
     df = df.append({'Image1' : image_input3}, ignore_index = True)
     df = df.append({'Image1' : image_input4}, ignore_index = True)
     df = df.append({'Image1' : image_input5}, ignore_index = True)


image = Image.open('image' + str(image_order[1]) + '.jpg')

st.image(image, width=1024)

st.write('Enter 5 words you feel:')

image_input1 = st.text_input('','', key=6)  
image_input2 = st.text_input('','', key=7)
image_input3 = st.text_input('','', key=8)
image_input4 = st.text_input('','', key=9)
image_input5 = st.text_input('','', key=10)

submit2 = False

if image_input1 and image_input2 and image_input3 and image_input4 and image_input5:
     submit2 = st.button('Submit', key=17, disabled=False)

if submit2:
     df = df.append({'Image2' : image_input1}, ignore_index = True)
     df = df.append({'Image2' : image_input2}, ignore_index = True)
     df = df.append({'Image2' : image_input3}, ignore_index = True)
     df = df.append({'Image2' : image_input4}, ignore_index = True)
     df = df.append({'Image2' : image_input5}, ignore_index = True)

image = Image.open('image' + str(image_order[2]) + '.jpg')

st.image(image, width=1024)

st.write('Enter 5 words you feel:')

image_input1 = st.text_input('','', key=11)  
image_input2 = st.text_input('','', key=12)
image_input3 = st.text_input('','', key=13)
image_input4 = st.text_input('','', key=14)
image_input5 = st.text_input('','', key=15)

submit3 = False

if image_input1 and image_input2 and image_input3 and image_input4 and image_input5:
     submit3 = st.button('Submit', key=18, disabled=False)

if submit3:
     df = df.append({'Image3' : image_input1}, ignore_index = True)
     df = df.append({'Image3' : image_input2}, ignore_index = True)
     df = df.append({'Image3' : image_input3}, ignore_index = True)
     df = df.append({'Image3' : image_input4}, ignore_index = True)
     df = df.append({'Image3' : image_input5}, ignore_index = True)

if submit1 and submit2 and submit3:
     st.write(df)