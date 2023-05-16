import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.button('Acido-Base Fuerte')
st.button('Acido Fuerte-Base Debil')
st.button('Acido Debil-Base Fuerte')

x=float(input(""))
y=float(input(""))
z=float(input(""))

ph1= np.log10(x)*-1
ph2= np.log10(y)*-1
ph3= np.log10(z)*-1

datos=pd.DataFrame({'Volumen': [1, 2, 3], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2)]}, index=["Lab 1", "Lab 2", "Lab 3"])
datos

print("pH=-log10("+str(x)+")= "+str(np.round(ph1, 2)))
print("pH=-log10("+str(y)+")= "+str(np.round(ph2, 2)))
print("pH=-log10("+str(z)+")= "+str(np.round(ph3, 2)))

df = pd.DataFrame({'Volumen':[1, 2, 3],
                   'pH':[ph1, ph2, ph3]})
df = df.set_index('Volumen')
fig, ax = plt.subplots()
df.plot(ax = ax)
ax.set_title('Curva Acido-Base', loc = "Center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_xlabel("Volumen usado", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("pH")
plt.show()
