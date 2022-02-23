#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

dt=pd.read_csv("dataset.csv")
name=dt.iloc[0:,0].tolist()
date=dt.iloc[0:,3].tolist()
vol=dt.iloc[0:,9].tolist()

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
    

data = {"Market Capitalization in Trillion USD":listv,"Name":listn}
dataframe = pd.DataFrame(data=data)
dataframe.plot.bar(x="Name", y="Market Capitalization in Trillion USD", title="Ranking based on Market Capitalization");
plt.savefig("output/2rank_based_on_marketcap.png",bbox_inches='tight')

