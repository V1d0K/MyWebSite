import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt

#Coger un datafram
with st.container():
    st.title('FILTROS LISTA TITANIC')
    lista_titanic = pd.read_csv('titanic.csv', index_col=0 )
    lista_titanic = pd.DataFrame(lista_titanic)
    st.write('LISTA CARGADA SIN LIMPIAR')
    lista_titanic


#Crear 3 tipos de filtros
with st.container():
    boton1 = st.button('Pulsar aquí para quitar las filas de la lista que tienen algun dato vacío.')
    lista_titanic_dropna = lista_titanic.dropna()
    if boton1:
        st.write('LISTA CARGADA LIMPIA')
        lista_titanic_dropna
        # boton2 = st.button('Quieres además ordenar la lista.')
        # if boton2:
        #     lista_ordenada = lista_titanic_dropna.sort_values('Age')
        #     lista_ordenada

with st.container():
    multi = st.multiselect('Elige que quieres ver:', ('Edad media de los tripulantes', 'Edad media de los supervivientes','Edad media de los fallecidos'))
    if multi == 'Edad media de los tripulantes':
        print(lista_titanic.Age.median())
    elif multi == 'Edad media de los supervivientes':
        superv = lista_titanic[lista_titanic['Survived'] == 1]
        print(superv.Age.median())
    else:
        print('644988777')
    st.write('You selected:', multi)

with st.container():
    option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
    if option == 'email':
        print('fran_tco99@hotmail.com')
    elif option == 'Home phone':
        print('944333666')
    else:
        print('644988777')
    st.write('You selected:', option)


#Visualizar los datos en plot, dataframe, o lo que sea