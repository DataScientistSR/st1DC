#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
op=st.selectbox('Please select level1:',('residential_city', 'Cluster', 'cc_status'))
op1=st.selectbox('Please select level2:',('residential_city', 'Cluster', 'cc_status'))
op2=st.selectbox('Please select level3:',('residential_city', 'Cluster', 'cc_status'))
plh=pd.read_csv('regions.csv')
pl=plh.rename(columns={0:'ply'},inplace=True)
df=pd.read_csv('appd.csv')
csv=df.to_csv('app.csv')
h=df.groupby(by=[op,op1,op2]).count()
h=pd.DataFrame(h)
c=h.to_csv().encode('utf-8')
st.map(pl)
st.dataframe(h)
st.download_button(label="Download data", data=c, file_name='downloaded1.csv',mime='text/csv')
col=['10PC PREMIUM ALUMINIUM SET', '13L AIR FRYER', '4PC MEGA SET',
       '6-BLADE BLENDER', '7PC CAST IRON SET', '7PC HONEYCOMB SS',
       '8PC DELUXE HAND BLENDER SET', '9PC KITCHEN MASTER', '9PC QUANTANIUM',
       'BR 1.7L CLASSIQUE GLASS KETTLE', 'INSTANT BOIL', 'INTELLIGENT GRILLER',
       'KRAUSE AND WELLMAN 11PC POT SET', 'KW 11PC NON-STICK COOKWARE',
       'KW 2 PLATE INDUCTION STOVE', 'KW DELUXE 180 GRILLER', 'KW GRILLER',
       'UPGRADE KW 11PC NON-STICK COOKWARE to 9PC QUANTANIUM',
       'UPGRADE KW 11PC NON-STICK COOKWARE to 9PC QUANTATNIUM',
       'VENUS STEEL DEEP POT SET']
l=[]
for i in col:
    l.append(h[i].sum())
sd=pd.DataFrame(col)
sd['sums']=l

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = sd[0]
sizes=sd['sums']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)
