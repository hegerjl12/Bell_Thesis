import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from shillelagh.backends.apsw.db import connect

st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

# Create a connection object.
conn = connect(":memory:")

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
     cursor = conn.cursor()
     return cursor.execute(query)
    #rows = conn.execute(query, headers=1)
    #rows = rows.fetchall()
    #return rows

def set_image():
     image = Image.open('image' + str(st.session_state.i) + '.jpg')
     with image_container:
          st.empty()
          st.image(image, width=360)

sheet_url = st.secrets["public_gsheets_url"]
st.write(sheet_url)
#rows = run_query('SELECT * FROM '+ str(sheet_url))
st.write(rows)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Selina's Thesis")

image_container = st.empty()
image_input = st.empty()

if 'image_order' not in st.session_state:
     st.session_state.image_order = [1, 2, 3]

if 'i' not in st.session_state:
     st.session_state.i = 1

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

          #st.write(st.session_state.image_words)

          st.session_state.i = st.session_state.i + 1

          if st.session_state.i < 4:   
               set_image()
               text = image_input.text_area('Enter 3 words you feel: ','', key=st.session_state.i)
          else:
               with image_container:
                    st.empty()
                    st.experimental_rerun()

else:

     text = " ".join(st.session_state.image_words[0])
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