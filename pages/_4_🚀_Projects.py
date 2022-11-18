import streamlit as st
import pandas as pd
import numpy as np

# if 'data' not in pn.state.cache.keys():
#     # Leer datos del CSV
#     df = pd.read_csv('data/owid-co2-data.csv')
#     pn.state.cache['data'] = df.copy()
# else:
#     df = pn.state.cache['data']


st.header('WORLD CO2 EMISSION DASHBOARD')

col01, col02 = st.columns(2, gap = 'large')
with st.container():
    with col01:
        st.subheader('Hi, I am Fran')
        st.image('images/mundo.jpg', width= 300)
        st.sidebar.slider('Widget de deslizamiento', 0.6)
        st.markdown("[Learn More >](http://franaguilar.com/)")

    with col02:
        st.write('A pesar de que el clima de la Tierra siempre ha cambiado de forma natural, por primera vez la actividad humana es la principal fuerza que afecta a este proceso, con consecuencias potencialmente drásticas.')
        st.write('Cada día usamos enormes volúmenes de combustibles fósiles en forma de gasolina, petróleo, carbón y gas natural, liberando dióxido de carbono. Este hecho, junto con otras emisiones generadas por la actividad humana, tales como el metano y el óxido nitroso, acentúan el “efecto invernadero” natural.')
        st.write('Considerando el legado de emisiones de gases invernadero y el creciente consumo mundial de energía, parece inevitable que nos acercamos a un mayor calentamiento de la tierra.Esta velocidad de cambio está amenazando a los sistemas sociales y ambientales, que no pueden adaptarse al mismo ritmo. Aumentan en el mundo los eventos meteorológicos extremos, con graves consecuencias en todos los ámbitos.')

st.sidebar.slider('Widget de deslizamiento', 1750, 2020)

st.subheader('What I do')

col03, col04 = st.columns(2, gap = 'large')

with col03:
    st.write('On my YouTube channel I am creating tutorials for people who:')
    st.write('-are looking for a way to leverage the power of Python in their day-to-day.')
    st.write('-are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.')
    st.write('-want to learn Data Analysis & Big data to be involved in all the it field related with data')

with col04:
    st.image('https://media1.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif?cid=ecf05e47pxeuod76erv1q2oy5yusdqtw96528tv3c7hy5ghz&rid=giphy.gif&ct=g')

# st.select_slider('Deslizame guapo')
st.sidebar.slider('Widget de deslizamiento', 0.6)
st.checkbox('yes')
st.button('Click')
st.radio('Elige tu sexo', ['Hombre', 'Mujer'])
st.selectbox('Elige tu sexo', ['Hombre', 'mujer'])
st.multiselect('Elegir un planeta', ['Jupiter', 'Marte', 'Neptuno'])
st.select_slider('Elige una note', ['Mala', 'buena', 'Excelente'])
st.slider('Elige un numero', 0.50)