import streamlit as st
from PIL import Image

st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)


st.title("Selina's Thesis")

answer_table1 = []

for i in range(len(5)):
          
     image = Image.open('404A4573.jpg')

     st.image(image, width=1024)

     st.write('Enter 5 words you feel:')

     image1_input1 = st.text_input('','', key=1)  
     image1_input2 = st.text_input('','', key=2)
     image1_input3 = st.text_input('','', key=3)
     image1_input4 = st.text_input('','', key=4)
     image1_input5 = st.text_input('','', key=5)



     if image1_input1 and image1_input2 and image1_input3 and image1_input4 and image1_input5:
          submit = st.button('Submit', key=6, disabled=False)

     if submit:
          answer_table1 += image1_input1
          answer_table1 += image1_input2
          answer_table1 += image1_input3
          answer_table1 += image1_input4
          answer_table1 += image1_input5

          st.write(answer_table)