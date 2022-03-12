import streamlit as st
import pandas as pd
from PIL import Image
import random

@st.cache
def run_image_1(which_image):
     which_image = random.randint(1,3)


st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")

df = pd.DataFrame(columns = ['Image1', 'Image2', 'Image3', 'Image4', 'Image5'])

which_image = 0

run_image_1(which_image, df)

image = Image.open('image' + str(which_image) + '.jpg')

st.image(image, width=1024)

st.write('Enter 5 words you feel:')

image1_input1 = st.text_input('','', key=1)  
image1_input2 = st.text_input('','', key=2)
image1_input3 = st.text_input('','', key=3)
image1_input4 = st.text_input('','', key=4)
image1_input5 = st.text_input('','', key=5)

submit = False

if image1_input1 and image1_input2 and image1_input3 and image1_input4 and image1_input5:
     submit = st.button('Submit', key=6, disabled=False)

if submit:
     df = df.append({'Image1' : image1_input1}, ignore_index = True)
     df = df.append({'Image1' : image1_input2}, ignore_index = True)
     df = df.append({'Image1' : image1_input3}, ignore_index = True)
     df = df.append({'Image1' : image1_input4}, ignore_index = True)
     df = df.append({'Image1' : image1_input5}, ignore_index = True)

     st.write(df)
