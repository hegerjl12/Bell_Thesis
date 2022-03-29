import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from deta import Deta


st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

deta = Deta(st.secrets["deta_key"])
WordDB = deta.Base("words")


st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Selina's Thesis")

def set_image():
     image = Image.open('image' + str(st.session_state.i) + '.jpg')
     with image_container:
          st.empty()
          st.image(image, width=360)

image_container = st.empty()
image_input = st.empty()

#if 'df' not in st.session_state:
 #    st.session_state.df = pd.DataFrame(columns = ['Image1', 'Image2', 'Image3', 'Image4', 'Image5', 'Image6', 'Image7', 'Image8', 'Image9', 'Image10'])

if 'image_order' not in st.session_state:
     st.session_state.image_order = [1, 2, 3]

if 'i' not in st.session_state:
     st.session_state.i = 1

#if 'next' not in st.session_state:
 #    st.session_state.next = 0

if 'image_words' not in st.session_state:
     st.session_state.image_words = []

if st.session_state.i < 4:

     set_image()

     with st.form('wordForm'):
          text = image_input.text_area('Enter 3 words you feel: ','', key=st.session_state.i)  
          submit = st.form_submit_button('Submit')

     if submit:
          words = text.split()
          image_input.empty()  
          
          st.session_state.image_words.append(words)
          WordDB.put({str(st.session_state.i): words[0]}, key=str(st.session_state.i))
          WordDB.put({str(st.session_state.i): words[1]}, key=str(st.session_state.i))
          WordDB.put({str(st.session_state.i): words[2]}, key=str(st.session_state.i))

          st.write(st.session_state.image_words)

          st.session_state.i = st.session_state.i + 1

          if st.session_state.i < 4:   
               set_image()
               text = image_input.text_area('Enter 3 words you feel: ','', key=st.session_state.i)
          else:
               with image_container:
                    st.empty()
                    st.experimental_rerun()

else:

    # text = " ".join(st.session_state.image_words[0])
     text = " ".join(WordDB.get("1"))
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())

     text = " ".join(st.session_state.image_words[1])
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())

     text = " ".join(st.session_state.image_words[2])
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())