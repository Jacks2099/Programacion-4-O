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
    a= st.write("Ingresa volumen 1:", value=" ")
    b= st.write("Ingresa volumen 2:", value=" ")
    c= st.write("Ingresa volumen 3:", value=" ")
    d= st.write("Ingresa volumen 4:", value=" ")
    e= st.write("Ingresa volumen 5:", value=" ")
    
    v= 0.1
    w= 0.01
    x= 0.001
    y= 0.0001
    z= 0.00001
    
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
  option = st.selectbox(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if '5':
    a= st.write("Ingresa volumen 1:", value=" ")
    b= st.write("Ingresa volumen 2:", value=" ")
    c= st.write("Ingresa volumen 3:", value=" ")
    d= st.write("Ingresa volumen 4:", value=" ")
    e= st.write("Ingresa volumen 5:", value=" ")
    
    v= 0.1
    w= 0.01
    x= 0.001
    y= 0.0001
    z= 0.00001
    
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
elif button3:
  option = st.selectbox(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if '5':
    a= st.write("Ingresa volumen 1:", value=" ")
    b= st.write("Ingresa volumen 2:", value=" ")
    c= st.write("Ingresa volumen 3:", value=" ")
    d= st.write("Ingresa volumen 4:", value=" ")
    e= st.write("Ingresa volumen 5:", value=" ")
    
    v= 0.1
    w= 0.01
    x= 0.001
    y= 0.0001
    z= 0.00001
    
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
