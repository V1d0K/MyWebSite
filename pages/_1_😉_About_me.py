import streamlit as st
import pandas as pd
import numpy as np


col1, col2 = st.columns(2, gap = 'large')

with col1:
    st.write('I always liked to build things.')
    st.write('-are looking for a way to leverage the power of Python in their day-to-day.')
    st.write('-are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.')
    st.write('-want to learn Data Analysis & Big data to be involved in all the it field related with data')

with col2:
    st.image('https://media2.giphy.com/media/MT5UUV1d4CXE2A37Dg/giphy.gif?cid=ecf05e47s05xj7ooap6s3s6bh1xougqsgyc0lv0pxb4vhp27&rid=giphy.gif&ct=g')

st.subheader('Here you can watch one of my adventures:')
st.video('https://youtu.be/eYwHwYJRSqc')