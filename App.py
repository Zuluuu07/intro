import streamlit as st
from PIL import Image

st.title("Mi Primera App!!")

st.header("En este espacio comienzo a desarrolar mis apliicaciones para mi")
st.write("Facilmente puedo relizar backend y fronted.")
image = Image.open('descarga.jpg')

st.image(image, caption='Interfaces multimodales' )
