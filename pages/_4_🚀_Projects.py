import streamlit as st
import pandas as pd
import numpy as np
import panel as pn
pn.extension('tabulator')
import


col1, col2 = st.columns(2, gap = 'large')

with col1:
    st.write('Here you can find some projects that I have done:')

if 'data' not in pn.state.cache.keys():

    df = pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')

    pn.state.cache['data'] = df.copy()

else: 

    df = pn.state.cache['data']

st.df

with col2:
    st.image('https://media1.giphy.com/media/RCtKcMeeIlIFskmH7C/giphy.gif?cid=ecf05e47ox5t6j7sm000fcybhxkpz21jsp58yx4m0xsobs3b&rid=giphy.gif&ct=g')