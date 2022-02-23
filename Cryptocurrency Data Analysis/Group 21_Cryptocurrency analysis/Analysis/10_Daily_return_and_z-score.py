#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from datetime import datetime


# In[6]:


crypto = pd.read_csv("dataset.csv")
liname=list(crypto["Name"])
lisymbol=list(crypto["Symbol"])
lidate=list(crypto["Date"])
liopen=list(crypto["Open"])
liclose=list(crypto["Close"])
dictgain={}
licurr=crypto['Name'].unique()
mainli=[]

for i in licurr:
    idx=[]
    for j in range(len(liname)):
        if liname[j] == i:
            idx.append(j)
    li=[]
    for j in idx:
        if liopen[j]==0:
            val=0
            li.append(val)
            mainli.append(val)
        else:
            val=(liclose[j]-liopen[j])/liopen[j]*100
            li.append(val)
            mainli.append(val)
    dictgain[i]=li

crypto["returns"]=mainli
li1=dictgain["Bitcoin"]
li2=dictgain["Ethereum"]
li3=dictgain["Binance Coin"]
li4=dictgain["Tether"]
li5=dictgain["Cardano"]
btcc = {'Name': liname,"Date":lidate,'returns':mainli}
btcc = pd.DataFrame(btcc)
btcc.to_csv('output/10dailyreturn.csv',index=False)


# In[7]:


crypto['Date'] = pd.to_datetime(crypto['Date'])
bitcoin = crypto[crypto.Name == 'Bitcoin']
ethereum = crypto[crypto.Name == 'Ethereum']
binance_Coin = crypto[crypto.Name == 'Binance Coin']
tether = crypto[crypto.Name == 'Tether']
cardano = crypto[crypto.Name == 'Cardano']
sns.set(style="whitegrid")
fig, axes = plt.subplots(5, 1, figsize=(12,20))
axes[0].set_title('Daily return')
sns.lineplot(ax=axes[0],x= bitcoin.Date,y= bitcoin.returns,color="r", label='Bitcoin')
sns.lineplot(ax=axes[1],x= ethereum.Date,y= ethereum.returns,color="g", label='Ethereum')
sns.lineplot(ax=axes[2],x= binance_Coin.Date,y= binance_Coin.returns,color="b", label='Binance Coin')
sns.lineplot(ax=axes[3],x= tether.Date,y= tether.returns,color="m", label='Tether')
sns.lineplot(ax=axes[4],x= cardano.Date,y= cardano.returns,color="k", label='Cardano')
plt.savefig('output/10dailyreturngraph.png')


# In[9]:


bitcoin["z_score"]=(bitcoin["returns"]-bitcoin["returns"].mean())/bitcoin["returns"].std()
ethereum["z_score"]=(ethereum["returns"]-ethereum["returns"].mean())/ethereum["returns"].std()
binance_Coin["z_score"]=(binance_Coin["returns"]-binance_Coin["returns"].mean())/binance_Coin["returns"].std()
cardano["z_score"]=(cardano["returns"]-cardano["returns"].mean())/cardano["returns"].std()
sns.set(style="whitegrid")
fig, axes = plt.subplots(4,1, figsize=(12,20))
sns.lineplot(ax=axes[0],x= bitcoin.Date,y= bitcoin.z_score,color="r", label='Bitcoin')
sns.lineplot(ax=axes[1],x= ethereum.Date,y= ethereum.z_score,color="g", label='Ethereum')
sns.lineplot(ax=axes[2],x= binance_Coin.Date,y= binance_Coin.z_score,color="b", label='Binance Coin')
sns.lineplot(ax=axes[3],x= cardano.Date,y= cardano.z_score,color="k", label='Cardano')
val1=bitcoin[bitcoin["z_score"]>=3].shape[0]
val2=bitcoin[bitcoin["z_score"]<=-3].shape[0]
print("No. of outlier in bitcoin",val1+val2)
val1=ethereum[ethereum["z_score"]>=3].shape[0]
val2=ethereum[ethereum["z_score"]<=-3].shape[0]
print("No. of outlier in ethereum",val1+val2)
val1=binance_Coin[binance_Coin["z_score"]>=3].shape[0]
val2=binance_Coin[binance_Coin["z_score"]<=-3].shape[0]
print("No. of outlier in binance_Coin",val1+val2)
val1=cardano[cardano["z_score"]>=3].shape[0]
val2=cardano[cardano["z_score"]<=-3].shape[0]
print("No. of outlier in cardano",val1+val2)
plt.savefig('output/10dailyreturnzscoregraph.png')


# In[ ]:





# In[ ]:




