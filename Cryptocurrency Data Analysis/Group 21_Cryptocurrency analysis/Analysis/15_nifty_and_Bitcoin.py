#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import seaborn as sns
import plotly.graph_objects as cs
import matplotlib.pyplot as plt


n50=pd.read_csv("nifty50.csv")
cripto=pd.read_csv("dataset.csv")
cname=list(cripto['Name'])
cdate=list(cripto['Date'])
copen=list(cripto['Open'])
cclose=list(cripto['Close'])
ndate=list(n50['Date'])
nopen=list(n50['Open'])
nclose=list(n50['Close'])
cdict={}
ndict={}
inter=ndate
            
for i in range(len(cclose)):
    if(cname[i]=="Bitcoin"):
        cdict[cdate[i]]=((cclose[i]-copen[i])/copen[i])*100

for i in range(len(nclose)):
    ndict[ndate[i]]=((nclose[i]-nopen[i])/nopen[i])*100

listnif=[]
listcrip=[]
for i in range(len(ndict)):
    listnif.append(ndict[inter[i]])
    listcrip.append(cdict[inter[i]])
    
al= {"Date":inter,'nifty':listnif,"percentage_return":listcrip}
assets= pd.DataFrame(al)
assets['Date'] = pd.to_datetime(assets['Date'])

sns.set(style="whitegrid")
fig, axes = plt.subplots(figsize=(12,4))
axes.set_title(' Daily Returns comparision of nifty and Bitcoin')
sns.lineplot(x=assets.Date,y=assets.percentage_return,color="r", label='Bitcoin')
sns.lineplot(x=assets.Date,y=assets.nifty,color="g" ,label='nifty');
plt.savefig('output/15Daily_Returns_comparision_of_nifty_and_Bitcoin.png')
init=0
bitinvest=[]
for i in range(len(inter)):
    bitinvest.append(((init+100)*cdict[inter[i]]/100)+(init+100))
    init=((init+100)*cdict[inter[i]]/100)+(init+100)

init=0
nifinvest=[]
for i in range(len(inter)):
    nifinvest.append(((init+100)*ndict[inter[i]]/100)+(init+100))
    init=((init+100)*ndict[inter[i]]/100)+(init+100)
nifinvest

invested=[]
init=0
for i in range(len(inter)):
    invested.append(init+100)
    init=init+100

df= {"Date":inter,'nifty':nifinvest,"bitcoin":bitinvest,"invested":invested}
dframe= pd.DataFrame(df)

pnif={"x":dframe.Date,"y":dframe.nifty,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"red"
       },
       "name":"Nifty50"
      }
pbit={"x":dframe.Date,"y":dframe.bitcoin,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"blue"
       },
       "name":"Bitcoin"
      }
inv={"x":dframe.Date,"y":dframe.invested,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"green"
       },
       "name":"Invested"
      }
fig = cs.Figure(data=[pnif,pbit,inv])
fig.update_layout(title='Bitcoin and Nifty50 Returns on investing 100rs/day',yaxis_title='Returns(in rupee)',xaxis_title='Date',xaxis_rangeslider_visible=False)
fig.write_html('output/15Bitcoin and Nifty50 Returns.html', auto_open=False)


