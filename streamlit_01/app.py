import streamlit as st

st.title("Fran's WEB SITE")
st.header('Into this web site you can find all my projects related with the programming field and a bit of my personal life.')
st.subheader('Currently I am studying a python data science course and a big data course too. I am trying to get ready to pass a junior level interview in this field')

st.image('https://media-exp1.licdn.com/dms/image/C5603AQEgWCNLcXcG3Q/profile-displayphoto-shrink_800_800/0/1593649438902?e=2147483647&v=beta&t=PZXeqnrm9T9KH_tkSuqoGVYH_5aVCVcr36Rr1Bl1cPE')
st.audio('https://www.videvo.net/es/efecto-de-sonido/pedo-humano-28/428207/')
st.video('https://vlipsy.com/vlip/meme-stretch-band-nut-shot-SokbYsbx')

st.select_slider('Deslizame guapo', 0.3)
st.slider('Widget de deslizamiento', 0.6)
st.checkbox('yes')
st.button('Click')
st.radio('Elige tu sexo', ['Hombre', 'Mujer'])
st.selectbox('Elige tu sexo', ['Hombre', 'mujer'])
st.multiselect('Elegir un planeta', ['Jupiter', 'Marte', 'Neptuno'])
st.select_slider('Elige una note', ['Mala', 'buena', 'Excelente'])
st.slider('Elige un numero', 0.50)