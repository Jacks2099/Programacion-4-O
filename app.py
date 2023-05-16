import streamlit as st
import pandas as pd
import numpy as np

button1 = st.button('Acido-Base Fuerte')
button2 = st.button('Acido Fuerte-Base Debil')
button3 = st.button('Acido Debil-Base Fuerte')

if button1:
  x=float(input(""))
  y=float(input(""))
  z=float(input(""))
  
  ph1= np.log10(x)*-1
  ph2= np.log10(y)*-1
  ph3= np.log10(z)*-1

  datos=pd.DataFrame({'Volumen': [1, 2, 3], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2)]}, index=["Lab 1", "Lab 2", "Lab 3"])
  datos

  st.write("pH=-log10("+str(x)+")= "+str(np.round(ph1, 2)))
  st.write("pH=-log10("+str(y)+")= "+str(np.round(ph2, 2)))
  st.write("pH=-log10("+str(z)+")= "+str(np.round(ph3, 2)))

  st.line_chart(data=pd.DataFrame, x='Volumen', y='pH')

elif button2:
  st.write(':poop:')
elif button3:
  st.write(':dog:')
