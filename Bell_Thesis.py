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
     image = Image.open('image' + str(st.session_state.i) + '.jpg')
     with image_container:
          st.empty()
          st.image(image, width=360, use_column_width='auto')

# create image container and text container
image_container = st.empty()
st.write("Enter 3 words you the image makes you feel: ")
image_input = st.empty()

# create state variables 
if 'image_order' not in st.session_state:
     st.session_state.image_order = [1, 2, 3]

if 'i' not in st.session_state:
     st.session_state.i = 1

#if 'image_words' not in st.session_state:
 #    st.session_state.image_words = []

# volital variables
total_words = []

if st.session_state.i < 4:
     
     with st.form('wordForm', clear_on_submit=True):
          set_image() 
          text = image_input.text_area('','', key=str(st.session_state.i))

          submit = st.form_submit_button('Submit')

     if submit:
          words = text.split()
          image_input.empty()  
          
      #    st.session_state.image_words.append(words)
          
          if st.session_state.i == 1:
               Image1DB.put({"words": words[0]})
               Image1DB.put({"words": words[1]})
               Image1DB.put({"words": words[2]})
          if st.session_state.i == 2:
               Image2DB.put({"words": words[0]})
               Image2DB.put({"words": words[1]})
               Image2DB.put({"words": words[2]})
          if st.session_state.i == 3:
               Image3DB.put({"words": words[0]})
               Image3DB.put({"words": words[1]})
               Image3DB.put({"words": words[2]})


          st.session_state.i = st.session_state.i + 1

          if st.session_state.i < 4:   
            #   set_image()
          else:
               with image_container:
                    st.empty()
                    st.experimental_rerun()

else:

     res = Image1DB.fetch()
     all_items = res.items
     for item in all_items:
          total_words.append(item.get('words'))
     
     
     text = " ".join(total_words)
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())

     res = Image2DB.fetch()
     all_items = res.items
     for item in all_items:
          total_words.append(item.get('words'))

     text = " ".join(total_words)
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())
     
     res = Image3DB.fetch()
     all_items = res.items
     for item in all_items:
          total_words.append(item.get('words'))

     text = " ".join(total_words)
     word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
     fig = plt.imshow(word_cloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(plt.show())