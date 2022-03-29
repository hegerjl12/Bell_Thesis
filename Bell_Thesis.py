import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from gsheetsdb import connect
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path


st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.json'):
     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
     if not creds or not creds.valid:
          if creds and creds.expired and creds.refresh_token:
               creds.refresh(Request())
          else:
               flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
               creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
     with open('token.json', 'w') as token:
          token.write(creds.to_json())

service = build('sheets', 'v4', credentials=creds)

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=5)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

for row in rows:
     st.write(row)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Selina's Thesis")

def set_image():
     image = Image.open('image' + str(st.session_state.i) + '.jpg')
     with image_container:
          st.empty()
          st.image(image, width=360)

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