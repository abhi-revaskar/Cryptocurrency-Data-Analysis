#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
dt=pd.read_csv("dataset.csv")
name=dt.iloc[0:,0].tolist()
date=dt.iloc[0:,3].tolist()
vol=dt.iloc[0:,8].tolist()

tgt=[]
for i in range(len(vol)):
    lst=[]
    if(date[i]=="11-11-2021"):
        lst.append(vol[i])
        lst.append(name[i])
        tgt.append(lst)
tgt.sort(reverse=True)
listv=[]
listn=[]
for i in range(10):
    listv.append(tgt[i][0])
    listn.append(tgt[i][1])
    

data = {"Volume":listv,"Name":listn}
dataframe = pd.DataFrame(data=data)
data = {"Volume":listv,"Name":listn}
dataframe = pd.DataFrame(data=data)
fig = px.bar(data,y='Volume',x='Name',title="Ranking based on Volume")
fig.show()

fig.write_html('output/3rankingbasedonvalume.html', auto_open=False)

