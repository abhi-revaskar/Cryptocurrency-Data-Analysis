#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

crypto=pd.read_csv("dataset.csv")
names=list(crypto["Name"])
crypto.columns=["Name","Symbol","Rank","Date","Open","High","Low","Close","Volume","Market"]
crypto['Date'] = pd.to_datetime(crypto['Date'])
crypto["log_close"]=np.log(crypto["Close"])

top6=[]
for i in names:
    if i not in top6:
        top6.append(i)
    if len(top6)==6:
        break

data1 = crypto[crypto.Name == top6[0]]
data2 = crypto[crypto.Name == top6[1]]
data3 = crypto[crypto.Name == top6[2]]
data4 = crypto[crypto.Name == top6[3]]
data5 = crypto[crypto.Name == top6[4]]

from datetime import datetime
start = datetime(2015, 1, 1)
end = datetime(2021, 11, 11)
# GOLD PRICE
import quandl
quandl.ApiConfig.api_key = 'jou3Hy9N_sKPZxy9mgxt'
gold_price = quandl.get("LBMA/GOLD", start_date = start, end_date = end)
gold_usd1=list(gold_price["USD (AM)"])
gold_usd2=list(gold_price["USD (PM)"])
gold_returns=[]

for i in range(len(gold_usd1)):
    gold_returns.append((gold_usd2[i]-gold_usd1[i])*100/gold_usd1[i])
    
gold_price["gold_gain"]=gold_returns


# S&P 500 INDEX 
from pandas_datareader import data
stock_index = data.DataReader('^GSPC', 'yahoo', start, end)

stock_open=list(stock_index["Open"])
stock_close=list(stock_index["Close"])

stock_returns=[]

for i in range(len(stock_open)):
    stock_returns.append((stock_close[i]-stock_open[i])*100/stock_open[i])
stock_index["stock_gain"]=stock_returns

# DOLLAR INDEX 
USD_index = data.DataReader('DX-Y.NYB', 'yahoo', start, end)

usd_open=list(USD_index["Open"])
usd_close=list(USD_index["Close"])

usd_returns=[]

for i in range(len(usd_open)):
    usd_returns.append((usd_close[i]-usd_open[i])*100/usd_open[i])
USD_index["usd_gain"]=usd_returns

real_asset = pd.merge(gold_price, stock_index, how = 'inner', on = 'Date')
real_asset = pd.merge(real_asset, USD_index, how = 'inner', on = 'Date')
real_asset = real_asset[['gold_gain', 'stock_gain', 'usd_gain']]
real_asset.columns = ['Gold_Price', 'Stock_Index', 'USD_Index']
    
coin_open=list(data1["Open"])
coin_close=list(data1["Close"])

coin_returns=[]

for i in range(len(coin_open)):
    coin_returns.append((coin_close[i]-coin_open[i])*100/coin_open[i])
data1["coin_gain"]=coin_returns
all_assets=pd.merge(real_asset,data1,how='inner',on='Date')
all_assets.tail()

sns.set(style="whitegrid")
fig, axes = plt.subplots(figsize=(12,4))
axes.set_title('Returns comparison between Gold and Bitcoin')
sns.lineplot(x= all_assets.Date,y= all_assets.coin_gain,color="r", label=top6[0])
sns.lineplot(x= all_assets.Date,y= all_assets.Gold_Price,color="g" ,label='Gold')
plt.savefig("output/Gold_and_Bitcoin.png")

sns.set(style="whitegrid")
fig, axes = plt.subplots(figsize=(12,4))
axes.set_title('Returns comparison between Stocks and Bitcoin')
sns.lineplot(x= all_assets.Date,y= all_assets.coin_gain,color="r", label=top6[0])

sns.lineplot(x= all_assets.Date,y= all_assets.Stock_Index,color="b",label="S&P 500 Index")
plt.savefig("output/14Stocks_and_Bitcoin.png")

