#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime 
import plotly.graph_objects as cs
import matplotlib.dates as mdates

df=pd.read_csv('dataset.csv')
conv_dict={'Rank':int,'Open':float,'High':float,'Low':float,'Volume':float,'Market-cap':float}
df=df.astype(conv_dict)
df.head(10)

df1=df.loc[df['Date'] == "11-11-2021"]
df1.head(100)

df2=df.loc[df['Symbol'] == 'BTC']
df2

bitcoindate=list(df2['Date'])
bitcoindate1=[]
def dmy_to_ymd(d):
    return datetime.datetime.strptime(d,'%d-%m-%Y').strftime('%Y-%m-%d')
for i in bitcoindate:
    bitcoindate1.append(dmy_to_ymd(i))

bitcoincap=list(df2['Market-cap'])
# bitdict=zip(bitcoindate1,bitcoincap)
bitdict={}
for i in range(len(bitcoindate1)):
    bitdict[bitcoindate1[i]]=bitcoincap[i]
    
start_date=datetime.date(2015,1,1)
end_date=datetime.date(2021,11,11)
delta=datetime.timedelta(days=1)
bitcoin=[]
while start_date <= end_date:
    if start_date.strftime('%Y-%m-%d') not in bitcoindate1:
        bitcoin.append(0)
    else:
        bitcoin.append(bitdict[start_date.strftime('%Y-%m-%d')])
    start_date += delta
    
                      
        

df3=df.loc[df['Symbol'] == 'ETH']
df3

ethereumdate=list(df3['Date'])
ethereumdate1=[]
def dmy_to_ymd(d):
    return datetime.datetime.strptime(d,'%d-%m-%Y').strftime('%Y-%m-%d')
for i in ethereumdate:
    ethereumdate1.append(dmy_to_ymd(i))

ethereumcap=list(df3['Market-cap'])
# ethdict=dict(zip(ethereumdate1,ethereumcap))
ethdict={}
for i in range(len(ethereumdate1)):
    ethdict[ethereumdate1[i]]=ethereumcap[i]
    
start_date=datetime.date(2015,1,1)
end_date=datetime.date(2021,11,11)
delta=datetime.timedelta(days=1)
ethereum=[]
while start_date <= end_date:
    if start_date.strftime('%Y-%m-%d') not in ethereumdate1:
        ethereum.append(0)
    else:
        ethereum.append(ethdict[start_date.strftime('%Y-%m-%d')])
    start_date += delta
    
                      
        

df4=df.loc[df['Symbol'] == 'BNB']
df4

binancedate=list(df4['Date'])
binancedate1=[]
def dmy_to_ymd(d):
    return datetime.datetime.strptime(d,'%d-%m-%Y').strftime('%Y-%m-%d')
for i in binancedate:
    binancedate1.append(dmy_to_ymd(i))

binancecap=list(df4['Market-cap'])
# bnbdict=dict(zip(binancedate1,binancecap))
bnbdict={}
for i in range(len(binancedate1)):
    bnbdict[binancedate1[i]]=binancecap[i]
    
start_date=datetime.date(2015,1,1)
end_date=datetime.date(2021,11,11)
delta=datetime.timedelta(days=1)
binance=[]
while start_date <= end_date:
    if start_date.strftime('%Y-%m-%d') not in binancedate1:
        binance.append(0)
    else:
        binance.append(bnbdict[start_date.strftime('%Y-%m-%d')])
    start_date += delta
    
                      
        

df5=df.loc[df['Symbol'] == 'USDT']
df5

tetherdate=list(df5['Date'])
tetherdate1=[]
def dmy_to_ymd(d):
    return datetime.datetime.strptime(d,'%d-%m-%Y').strftime('%Y-%m-%d')
for i in tetherdate:
    tetherdate1.append(dmy_to_ymd(i))

tethercap=list(df5['Market-cap'])
# usdtdict=dict(zip(tetherdate1,tethercap))
usdtdict={}
for i in range(len(tetherdate1)):
    usdtdict[tetherdate1[i]]=tethercap[i]
    
start_date=datetime.date(2015,1,1)
end_date=datetime.date(2021,11,11)
delta=datetime.timedelta(days=1)
tether=[]
while start_date <= end_date:
    if start_date.strftime('%Y-%m-%d') not in tetherdate1:
        tether.append(0)
    else:
        tether.append(usdtdict[start_date.strftime('%Y-%m-%d')])
    start_date += delta
    
                      
        

df6=df.loc[df['Symbol'] == 'SOL']
df6

solanadate=list(df6['Date'])
solanadate1=[]
def dmy_to_ymd(d):
    return datetime.datetime.strptime(d,'%d-%m-%Y').strftime('%Y-%m-%d')
for i in solanadate:
    solanadate1.append(dmy_to_ymd(i))

solanacap=list(df6['Market-cap'])
# soldict=dict(zip(solanadate1,solanacap))
soldict={}
for i in range(len(solanadate1)):
    soldict[solanadate1[i]]=solanacap[i]
    
start_date=datetime.date(2015,1,1)
end_date=datetime.date(2021,11,11)
delta=datetime.timedelta(days=1)
solana=[]
while start_date <= end_date:
    if start_date.strftime('%Y-%m-%d') not in solanadate1:
        solana.append(0)
    else:
        solana.append(soldict[start_date.strftime('%Y-%m-%d')])
    start_date += delta
    
                      
        



dict={'Date':bitcoindate1,'Bitcoin':bitcoin,'Ethereum':ethereum,'Binance_Coin':binance,'Tether':tether,'Solana':solana}
df_main=pd.DataFrame(dict)
df_main['Date'] = pd.to_datetime(df_main['Date'])
df_main

bit={"x":df_main.Date,"y":df_main.Bitcoin,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"blue"
       },
       "name":"Bitcoin"
      }
eth={"x":df_main.Date,"y":df_main.Ethereum,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"red"
       },
       "name":"Ethereum"
      }
bc={"x":df_main.Date,"y":df_main.Binance_Coin,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"black"
       },
       "name":"Binance_Coin"
      }
teth={"x":df_main.Date,"y":df_main.Tether,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"violet"
       },
       "name":"Tether"
      }
sola={"x":df_main.Date,"y":df_main.Solana,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"yellowgreen"
       },
       "name":"Solana"
      }
fig = cs.Figure(data=[bit,teth,bc,eth,sola])
fig.update_layout(title='comparision of market cap of top 5 cryptocurrencies',yaxis_title='Marketcap($)',xaxis_title='Date',xaxis_rangeslider_visible=True)
fig.show()
fig.write_html('output/4comparision_of_market_cap_of_top_5_cryptocurrencie.html', auto_open=False)

