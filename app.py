import streamlit as st
import pandas as pd
import numpy as np

st.title('_Curvas de Titulación_')

option = st.selectbox(
  'Selecciona el tipo de curva',
  ('Acido-Base (Fuertes)', 'Base-Acido (Fuertes)', 'Experimental'))

CA = st.text_input("Ingresa la concentración del _analito_:", value=" ")
VA = st.text_input("Ingresa volumen del _analito_:", value=" ")
CT = st.text_input("Ingresa la concentración del _titulante_:", value=" ")

if option == 'Acido-Base (Fuertes)':
  volumen = st.radio(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if volumen == '5':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      elif mT1==mA:
        ph1==7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      elif mT2=mA:
        ph2==7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      elif mT3=mA:
        ph3==7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      elif mT4=mA:
        ph4==7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      mT5 = np.multiply(float(CT), float(e))
      if mT4<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= np.log10(float(C4))*-1
      elif mT4=mA:
        ph5==7
      elif mT4>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5"])
      datos
      
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
elif option == 'Base-Acido (Fuertes)':
  st.write('En proceso:hammer:')
elif option == 'Experimental':
  st.write('En proceso:hammer:')
