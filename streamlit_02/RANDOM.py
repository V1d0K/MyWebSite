import streamlit as st
import matplotlib as plt
import numpy as np
import pandas as pd
import random
import time

if 'historico' not in st.session_state:
st.session_state['Sesion_nombre'] = lista_resultados

with st.container():
    st.title('LISTA DE NOMBRES')
    lista_nombres = ['Fran', 'Marcos', 'Jaime', 'Andrés', 'Raúl', 'Jaime', 'Joao', 'Jesus', 'Ernesto', 'Carlos']
    lista_resultados = []
    print(lista_resultados)
if st.button('Pulsar aquí para obtener el nombre de un pendejo:'):
    elegido = random.randint(0,8)
    nombre = st.subheader('Este es el intruso:')
    lista_resultados.append(lista_nombres[elegido])

    st.write(lista_nombres[elegido])
    st.session_state[lista_resultados]

fig, ax= plot.subplots()
ax.hist(x=lista_resultados, density=True, bien=30)
st.snow()
st.pyplot(fig)
