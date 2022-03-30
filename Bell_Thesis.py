import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt #only for wordcloud
from wordcloud import WordCloud #only for wordcloud
from deta import Deta

# set page config details
st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

st.title("Selina's Thesis")

with st.spinner("Connecting to database..."):
     # connect to databases
     deta = Deta(st.secrets["deta_key"])
     Image1DB = deta.Base("image1db")
     Image2DB = deta.Base("image2db")
     Image3DB = deta.Base("image3db")


st.set_option('deprecation.showPyplotGlobalUse', False) #only for wordcloud

# set selected image to the image container
def set_image():
     st.session_state.i = random.choice(st.session_state.images_left)
     image = Image.open('image' + str(st.session_state.i) + '.jpg')
     with image_container.container():
          st.image(image, width=360, use_column_width='auto')
     st.session_state.images_left.remove(st.session_state.i)
     
# create image container and text container
image_container = st.empty()

# create state variables 
if 'images_left' not in st.session_state:
     st.session_state.images_left = [1, 2, 3]

if 'i' not in st.session_state:
     st.session_state.i = 1


# loop to print images and collect input
if st.session_state.i < 4:

     # set image and form for input
     set_image() 
     with st.form('wordForm', clear_on_submit=True):
          st.write("Enter 3 words you the image makes you feel: ")
          text1 = st.text_input('','', key=str(st.session_state.i)+"1")
          text2 = st.text_input('','', key=str(st.session_state.i)+"2")
          text3 = st.text_input('','', key=str(st.session_state.i)+"3")

          submit = st.form_submit_button('Submit')

     # once form is submitted
     if submit:
          
          # commit input to database
          if st.session_state.i == 1:
               Image1DB.put({"words": text1})
               Image1DB.put({"words": text2})
               Image1DB.put({"words": text3})
          if st.session_state.i == 2:
               Image2DB.put({"words": text1})
               Image2DB.put({"words": text2})
               Image2DB.put({"words": text3})
          if st.session_state.i == 3:
               Image3DB.put({"words": text1})
               Image3DB.put({"words": text2})
               Image3DB.put({"words": text3})

          # increment count
          st.session_state.i = st.session_state.i + 1

          # reset image
          if st.session_state.i < 4:   
               set_image()
          # or clear screen and prep for wordcloud
          else:
               with image_container:
                    st.empty()
                    st.experimental_rerun()

else:

     res = Image1DB.fetch()
     all_items = res.items
     for item in all_items:
          total_words.append(item.get('words'))
     
     total_words = []
     text = " ".join(total_words)
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())

     res = Image2DB.fetch()
     all_items = res.items
     for item in all_items:
          total_words.append(item.get('words'))

     total_words = []
     text = " ".join(total_words)
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())
     
     res = Image3DB.fetch()
     all_items = res.items
     for item in all_items:
          total_words.append(item.get('words'))

     total_words = []
     text = " ".join(total_words)
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())