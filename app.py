import streamlit as st
import pandas as pd
import numpy as np

st.title('_Curvas de Titulación_')

button1 = st.button('Acido-Base Fuerte')
button2 = st.button('Acido Fuerte-Base Debil')
button3 = st.button('Acido Debil-Base Fuerte')

if button1:
  option = st.selectbox(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if '5':
    a= st.input("Ingresa volumen 1: ")))
    b= st.input("Ingresa volumen 2: "))
    c= st.input("Ingresa volumen 3: "))
    d= st.input("Ingresa volumen 4: "))
    e= st.input("Ingresa volumen 4: "))
    
    ph1= np.log10(v)*-1
    ph2= np.log10(w)*-1
    ph3= np.log10(x)*-1
    ph4= np.log10(y)*-1
    ph5= np.log10(z)*-1
    
    datos=pd.DataFrame({'Volumen': [a, b, c, d, e], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5"])
    datos
    
    st.write("pH=-log10("+str(x)+")= "+str(np.round(ph1, 2)))
    st.write("pH=-log10("+str(y)+")= "+str(np.round(ph2, 2)))
    st.write("pH=-log10("+str(z)+")= "+str(np.round(ph3, 2)))
    
  st.line_chart(data=pd.DataFrame, x='Volumen', y='pH')

elif button2:
  st.write(':poop:')
elif button3:
  st.write(':dog:')
