#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from datetime import datetime


# In[2]:


crypto = pd.read_csv("dataset.csv")


# In[3]:


dict1={}
from datetime import datetime

crypto['Date'] = pd.to_datetime(crypto['Date'], format='%d-%m-%Y')
liname=list(crypto["Name"])
lisymbol=list(crypto["Symbol"])
lidate=list(crypto["Date"])
liopen=list(crypto["Open"])
liclose=list(crypto["Close"])

for i in range(len(liname)):
    if lidate[i]== datetime(2021,11,11):
        dict1[liname[i]]=liclose[i]
dict2=dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
rank=[]
name=[]
close=[]
p=1
for i in dict2:
    name.append(i)
    rank.append(p)
    close.append(dict2[i])
    p=p+1
btcc = {'Name': name,"Rank":rank,'Close':close}
btcc = pd.DataFrame(btcc)
btcc.to_csv('output/1Rankbyclosingprice.csv',index=False)


# In[ ]:





# In[ ]:





# In[ ]:




