import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
backend: TkAgg >> .matplotlib/matplotlibrc

st.title('_Curvas de Titulación_')

option = st.selectbox(
  'Selecciona el tipo de curva',
  ('Acido-Base Fuerte', 'Acido Fuerte-Base Debil', 'Acido Debil-Base Fuerte'))

if option == 'Acido-Base Fuerte':
  volumen = st.radio(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if volumen == '5':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      
      C1= 0.05
      C2= 0.0125
      C3= 1e-7
      C4= 8.33e-3
      C5= 0.01429
      
      ph1= 14+np.log10(C1)
      ph2= 14+np.log10(C2)
      ph3= np.log10(C3)*-1
      ph4= np.log10(C4)*-1
      ph5= np.log10(C5)*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5"])
      datos
      
      st.header('Cálculos')
      
      st.write("pH=14+log10("+str(C1)+")= "+str(np.round(ph1, 2)))
      st.write("pH=14+log10("+str(C2)+")= "+str(np.round(ph2, 2)))
      st.write("pH=-log10("+str(C3)+")= "+str(np.round(ph3, 2)))
      st.write("pH=-log10("+str(C4)+")= "+str(np.round(ph4, 2)))
      st.write("pH=-log10("+str(C5)+")= "+str(np.round(ph5, 2)))
      
      st.line_chart(datos, x='Volumen', y='pH')
      
  elif volumen == '6':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      
      C1= 0.05
      C2= 0.02143
      C3= 5.5555e-3
      C4= 4.5454e-3
      C5= 0.01154
      C6= 0.01429
      
      ph1= 14+np.log10(C1)
      ph2= 14+np.log10(C2)
      ph3= 14+np.log10(C3)
      ph4= np.log10(C4)*-1
      ph5= np.log10(C5)*-1
      ph6= np.log10(C6)*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6"])
      datos
      
      st.header('Cálculos')
      
      st.write("pH=14+log10("+str(C1)+")= "+str(np.round(ph1, 2)))
      st.write("pH=14+log10("+str(C2)+")= "+str(np.round(ph2, 2)))
      st.write("pH=14+log10("+str(C3)+")= "+str(np.round(ph3, 2)))
      st.write("pH=-log10("+str(C4)+")= "+str(np.round(ph4, 2)))
      st.write("pH=-log10("+str(C5)+")= "+str(np.round(ph5, 2)))
      st.write("pH=-log10("+str(C6)+")= "+str(np.round(ph6, 2)))
      
      st.line_chart(datos, x='Volumen', y='pH')
      
  elif volumen == '7':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      
      C1= 0.05
      C2= 0.02143
      C3= 5.5555e-3
      C4= 1e-7
      C5= 4.5454e-3
      C6= 0.01154
      C7= 0.01429
      
      ph1= 14+np.log10(C1)
      ph2= 14+np.log10(C2)
      ph3= 14+np.log10(C3)
      ph4= np.log10(C4)*-1
      ph5= np.log10(C5)*-1
      ph6= np.log10(C6)*-1
      ph7= np.log10(C7)*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7"])
      datos
      
      st.header('Cálculos')
      
      st.write("pH=14+log10("+str(C1)+")= "+str(np.round(ph1, 2)))
      st.write("pH=14+log10("+str(C2)+")= "+str(np.round(ph2, 2)))
      st.write("pH=14+log10("+str(C3)+")= "+str(np.round(ph3, 2)))
      st.write("pH=-log10("+str(C4)+")= "+str(np.round(ph4, 2)))
      st.write("pH=-log10("+str(C5)+")= "+str(np.round(ph5, 2)))
      st.write("pH=-log10("+str(C6)+")= "+str(np.round(ph6, 2)))
      st.write("pH=-log10("+str(C7)+")= "+str(np.round(ph7, 2)))
      
      st.line_chart(datos, x='Volumen', y='pH')
elif option == 'Acido Fuerte-Base Debil':
  st.write('En proceso:hammer:')
elif option == 'Acido Debil-Base Fuerte':
  st.write('En proceso:hammer:')
