import streamlit as st
import pandas as pd
import numpy as np

st.header('WORLD CO2 EMISSION DASHBOARD')

col01, col02 = st.columns(2, gap = 'large')
with st.container():
    with col01:
        st.image('images/mundo.jpg', width= 375)
        ano = st.slider('Año',  1750, 2020)
        st.markdown("[Learn More >](http://franaguilar.com/)")

    with col02:
        st.write('A pesar de que el clima de la Tierra siempre ha cambiado de forma natural, por primera vez la actividad humana es la principal fuerza que afecta a este proceso, con consecuencias potencialmente drásticas.')
        st.write('Cada día usamos enormes volúmenes de combustibles fósiles en forma de gasolina, petróleo, carbón y gas natural, liberando dióxido de carbono. Este hecho, junto con otras emisiones generadas por la actividad humana, tales como el metano y el óxido nitroso, acentúan el “efecto invernadero” natural.')
        st.write('Considerando el legado de emisiones de gases invernadero y el creciente consumo mundial de energía, parece inevitable que nos acercamos a un mayor calentamiento de la tierra.Esta velocidad de cambio está amenazando a los sistemas sociales y ambientales, que no pueden adaptarse al mismo ritmo. Aumentan en el mundo los eventos meteorológicos extremos, con graves consecuencias en todos los ámbitos.')

#Leemos el csv que tenmos que utilizar para las tablas.
df = pd.read_csv('data/owid-co2-data.csv')

#Rellenamos los huecos vacios con UN 0.
df.fillna(0, inplace = True) # Para quedarlo fijo se pone inplace = True
df['gdp_per_capita'] = np.where(df['population']!= 0, df['gdp']/ df['population'], 0)

# Crear el panel de control con botones y sliders
# st.slider('Widget de deslizamiento',  1750, 2020) Creado arriba en la col01



# co2_pipeline = (df[(df.year <= ano) & (df.country.isin(continents))].groupby(['country', 'year'])[yaxis_co2].mean().to_frame().reset_index().sort_values(by='year').reset_index(drop=True))
# st.bar_chart(co2_pipeline,'country', 'year',use_container_width=True)

# co2_plot = co2_pipeline.hvplot(x = 'year', by='country', y=yaxis_co2,line_width=2, title="CO2 emission by continent")
# co2_plot









st.subheader('What I do')

col03, col04 = st.columns(2, gap = 'large')

with col03:
    continents = ['World', 'Asia', 'Oceania', 'Europe', 'Africa', 'North America', 'South America', 'Antarctica']
    yaxis_co2 = st.radio("Select CO2 Measures",('co2','co2_per_capita'))
    if yaxis_co2 == 'co2':
        st.line_chart(df, x='year', y='co2')
    else:
        st.line_chart(df, x='country', y='co2_per_capita',use_container_width=True)

with col04:
    st.image('https://media1.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif?cid=ecf05e47pxeuod76erv1q2oy5yusdqtw96528tv3c7hy5ghz&rid=giphy.gif&ct=g')

# st.select_slider('Deslizame guapo')
# st.sidebar.slider('Widget de deslizamiento', 0.6)
# st.checkbox('yes')
# st.button('Click')
# st.radio('Elige tu sexo', ['Hombre', 'Mujer'])
# st.selectbox('Elige tu sexo', ['Hombre', 'mujer'])
# st.multiselect('Elegir un planeta', ['Jupiter', 'Marte', 'Neptuno'])
# st.select_slider('Elige una note', ['Mala', 'buena', 'Excelente'])
# st.slider('Elige un numero', 0.50)