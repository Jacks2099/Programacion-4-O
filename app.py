import streamlit as st
import pandas as pd
import numpy as np

st.title('_Curvas de Titulación_')

option = st.selectbox(
  'Selecciona el tipo de curva',
  ('Acido-Base Fuerte', 'Acido Fuerte-Base Debil', 'Acido Debil-Base Fuerte'))

if 'Acido-Base Fuerte':
  option = st.selectbox(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if '5':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      
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
      
      st.header('Cálculos')
      
      st.write("pH=-log10("+str(x)+")= "+str(np.round(ph1, 2)))
      st.write("pH=-log10("+str(y)+")= "+str(np.round(ph2, 2)))
      st.write("pH=-log10("+str(z)+")= "+str(np.round(ph3, 2)))
      st.write("pH=-log10("+str(z)+")= "+str(np.round(ph4, 2)))
      st.write("pH=-log10("+str(z)+")= "+str(np.round(ph5, 2)))
      
      chart_frame({'Volumen': [a, b, c, d, e], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2)]})
      
  elif '6':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      
      u= 0.1
      v= 0.01
      w= 0.001
      x= 0.0001
      y= 0.00001
      z= 0.000001
      
      ph1= np.log10(u)*-1
      ph2= np.log10(v)*-1
      ph3= np.log10(w)*-1
      ph4= np.log10(x)*-1
      ph5= np.log10(y)*-1
      ph6= np.log10(z)*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6"])
      datos
      
      st.header('Cálculos')
      
      st.write("pH=-log10("+str(x)+")= "+str(np.round(ph1, 2)))
      st.write("pH=-log10("+str(y)+")= "+str(np.round(ph2, 2)))
      st.write("pH=-log10("+str(z)+")= "+str(np.round(ph3, 2)))
      st.write("pH=-log10("+str(z)+")= "+str(np.round(ph4, 2)))
      st.write("pH=-log10("+str(z)+")= "+str(np.round(ph5, 2)))
      st.write("pH=-log10("+str(z)+")= "+str(np.round(ph6, 2)))
      
      st.line_chart(data=pd.DataFrame, x='Volumen', y='pH')

elif 'Acido Fuerte-Base Debil':
  st.write('En proceso:hammer:')
elif 'Acido Debil-Base Fuerte':
  st.write('En proceso:hammer:')
