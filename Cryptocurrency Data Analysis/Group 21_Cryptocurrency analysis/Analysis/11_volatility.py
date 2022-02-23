#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from datetime import datetime
import plotly.express as px
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
    
crypto["Gain"]=mainli
li1=dictgain["Bitcoin"]
li2=dictgain["Ethereum"]
li3=dictgain["Binance Coin"]
li4=dictgain["Tether"]
li5=dictgain["Cardano"]

datelist=crypto["Date"].to_list()
crypto['Date'] = pd.to_datetime(crypto['Date'])

idx=datelist.index("13-01-2020")
bitcoin = crypto[crypto.Name == 'Bitcoin']
ethereum = crypto[crypto.Name == 'Ethereum']
binance_Coin = crypto[crypto.Name == 'Binance Coin']
tether = crypto[crypto.Name == 'Tether']
cardano = crypto[crypto.Name == 'Cardano']

bitcoin_gain = list(bitcoin["Gain"])
bitcoin_gain = bitcoin_gain[:idx]
ethereum_gain = list(ethereum["Gain"])
ethereum_gain = ethereum_gain[:idx]
binance_Coin_gain = list(binance_Coin["Gain"])
binance_Coin_gain=binance_Coin_gain[:idx]
tether_gain = list(tether["Gain"])
tether_gain=tether_gain[:idx]
cardano_gain = list(cardano["Gain"])
cardano_gain=cardano_gain[:idx]

bitcoin_std=bitcoin["Gain"].std()
ethereum_std=ethereum["Gain"].std()
binance_Coin_std=binance_Coin["Gain"].std()
tether_std=tether["Gain"].std()
cardano_std=cardano["Gain"].std()

bitcoin_vol=bitcoin_std*np.sqrt(366)
ethereum_vol=ethereum_std*np.sqrt(366)
binance_Coin_vol=binance_Coin_std*np.sqrt(366)
tether_vol=tether_std*np.sqrt(366)
cardano_vol=cardano_std*np.sqrt(366)


coins = ['Bitcoin', 'Ethereum', 'Binance Coin', 'Tether', 'Cardano']
volatility = [bitcoin_vol, ethereum_vol, binance_Coin_vol, tether_vol, cardano_vol]
dt= {"Coins":coins,'volatility':volatility}
dt1= pd.DataFrame(dt)
fig = px.bar(dt1,x='Coins',y='volatility')
fig.show()

fig.write_html('output/11volatility.html', auto_open=False)

