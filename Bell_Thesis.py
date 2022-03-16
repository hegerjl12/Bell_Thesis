import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

st.title("Selina's Thesis")

def set_image():
     image = Image.open('image' + str(st.session_state.i) + '.jpg')
     with image_container:
          st.empty()
          st.image(image, width=1024)

def cloud(image, text, max_word, max_font, random):
    stopwords = set(STOPWORDS)
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem', 'asked', 'made', 'half', 'much',
    'certainly', 'might', 'came'])

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

          st.write(st.session_state.image_words)

          st.session_state.i = st.session_state.i + 1

          if st.session_state.i < 4:   
               set_image()
               text = image_input.text_area('','', key=st.session_state.i)
          else:
               with image_container:
                    st.empty()
                    st.experimental_rerun()

else:
     wc = WordCloud(background_color="white", colormap="hot", max_words=max_word, mask=image,
          stopwords=stopwords, max_font_size=max_font, random_state=random)
     
     wc.generate(text)
     image_colors = ImageColorGenerator(image)

     # show the figure
    plt.figure(figsize=(100,100))
    fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]})
    axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")

    for ax in axes:
        ax.set_axis_off()
    st.pyplot()