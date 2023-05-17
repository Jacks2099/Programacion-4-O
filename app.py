import streamlit as st
import pandas as pd
import numpy as np

st.title('_Curvas de Titulación_')

option = st.selectbox(
  'Selecciona el tipo de curva',
  ('Acido-Base Fuerte', 'Acido Fuerte-Base Debil', 'Acido Debil-Base Fuerte'))

CA = st.text_input("Ingresa la concentración del _analito_:", value=" ")
VA = st.text_input("Ingresa volumen del _analito_:", value=" ")
CT = st.text_input("Ingresa la concentración del _titulante_:", value=" ")
mmolA = np.multiply(CA, VA)

if option == 'Acido-Base Fuerte':
  volumen = st.radio(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if volumen == '5':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")

      mmolT1 = np.multiply(CT,a)
      mmolT2 = np.multiply(CT,b)
      mmolT3 = np.multiply(CT,c)
      mmolT4 = np.multiply(CT,d)
      
      C1= (mmolA-mmolT1)/(VA+a)
      C2= (mmolA-mmolT2)/(VA+b)
      C3= (mmolA-mmolT3)/(VA+c)
      C4= (mmolA-mmolT4)/(VA+d)
      
      ph1= np.log10(CA)*-1
      ph2= np.log10(C1)*-1
      ph3= np.log10(C2)*-1
      ph4= np.log10(C3)*-1
      ph5= np.log10(C4)*-1
      
      datos=pd.DataFrame({'Volumen': [0, a, b, c, d], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5"])
      datos
      
      st.header('Cálculos')
      
      st.write("pH=-log10("+str(CA)+")= "+str(np.round(ph1, 2)))
      st.write("pH=-log10("+str(C1)+")= "+str(np.round(ph2, 2)))
      st.write("pH=-log10("+str(C2)+")= "+str(np.round(ph3, 2)))
      st.write("pH=-log10("+str(C3)+")= "+str(np.round(ph4, 2)))
      st.write("pH=-log10("+str(C4)+")= "+str(np.round(ph5, 2)))
      
      st.line_chart(datos, x='Volumen', y='pH')
      
  elif volumen == '6':
      st.write('En proceso:hammer:')
  elif volumen == '7':
      st.write('En proceso:hammer:')
  elif volumen == '8':
    st.write('En proceso:hammer:')
  elif volumen == '9':
    st.write('En proceso:hammer:')
  elif volumen == '10':
    st.write('En proceso:hammer:')
elif option == 'Acido Fuerte-Base Debil':
  st.write('En proceso:hammer:')
elif option == 'Acido Debil-Base Fuerte':
  st.write('En proceso:hammer:')
