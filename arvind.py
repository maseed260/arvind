import streamlit as st

#text/title
st.title("Happy Birthday Arvind mama")

#Images
from PIL import Image
img=Image.open("arvind.jpg")
st.image(img,width=700,caption="My manavadu Steve Jobs")

st.balloons()