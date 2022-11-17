import streamlit as st
import pandas as pd
import numpy as np
import psycopg2

col01, col02 = st.columns(2, gap = 'large')

with col01:
    st.header('Hi, I am Fran')
    st.audio('files/audio.mp3')

with col02:
    st.image('files/Yo.jpg', width= 200)

st.title("A Data Analyst From Spain")
st.write('I am passionate about finding ways to use Python and VBA to be more efficiente and effective in business settings.')
st.markdown("[Learn More >](http://franaguilar.com/)")

st.subheader('What I do')

col1, col2 = st.columns(2, gap = 'large')

with col1:
    st.write('On my YouTube channel I am creating tutorials for people who:')
    st.write('-are looking for a way to leverage the power of Python in their day-to-day.')
    st.write('-are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.')
    st.write('-want to learn Data Analysis & Big data to be involved in all the it field related with data')

with col2:
    st.image('https://media1.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif?cid=ecf05e47pxeuod76erv1q2oy5yusdqtw96528tv3c7hy5ghz&rid=giphy.gif&ct=g')

# st.select_slider('Deslizame guapo')
st.slider('Widget de deslizamiento', 0.6)
st.checkbox('yes')
st.button('Click')
st.radio('Elige tu sexo', ['Hombre', 'Mujer'])
st.selectbox('Elige tu sexo', ['Hombre', 'mujer'])
st.multiselect('Elegir un planeta', ['Jupiter', 'Marte', 'Neptuno'])
st.select_slider('Elige una note', ['Mala', 'buena', 'Excelente'])
st.slider('Elige un numero', 0.50)