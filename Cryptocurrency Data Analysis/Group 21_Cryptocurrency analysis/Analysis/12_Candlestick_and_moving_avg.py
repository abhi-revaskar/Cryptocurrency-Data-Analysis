#!/usr/bin/env python
# coding: utf-8

# In[18]:


import plotly.graph_objects as cs
import pandas as pd
import time

dt = pd.read_csv('dataset.csv')
name=dt.iloc[0:,0].tolist()
dat=dt.iloc[0:,3].tolist()
op=dt.iloc[0:,4].tolist()
hg=dt.iloc[0:,5].tolist()
low=dt.iloc[0:,6].tolist()
clse=dt.iloc[0:,7].tolist()

name1=[]
dat1=[]
op1=[]
hg1=[]
low1=[]
clse1=[]
for i in range(len(name)):
    if(time.strptime(dat[i], "%d-%m-%Y")>time.strptime("10-11-2020", "%d-%m-%Y") and name[i]=="Bitcoin"):
        name1.append(name[i])
        dat1.append(dat[i])
        op1.append(op[i])
        hg1.append(hg[i])
        low1.append(low[i])
        clse1.append(clse[i])
dict1={'Name':name1,'date':dat1,'open':op1,'high':hg1,'low':low1,'close':clse1}
dframe=pd.DataFrame(dict1)

candles= cs.Candlestick(x=dframe['date'],open=dframe['open'],high=dframe['high'],low=dframe['low'],close=dframe['close'],name="candles")


mva20={"x":dframe.date,"y":dframe.close.rolling(window=20,min_periods=1).mean(),"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"blue"
       },
       "name":"20 moving avg"
      }
mva60={"x":dframe.date,"y":dframe.close.rolling(window=60,min_periods=1).mean(),"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"yellow"
       },
       "name":"60 moving avg"
      }
mva45={"x":dframe.date,"y":dframe.close.rolling(window=45,min_periods=1).mean(),"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"black"
       },
       "name":"45 moving avg"
      }
fig = cs.Figure(data=[candles,mva20,mva45,mva60])
fig.update_layout(title='Bitcoin',yaxis_title='Price($)',xaxis_title='Date',xaxis_rangeslider_visible=False)
fig.show()
fig.write_html('output/12candlestick&movingavg.html', auto_open=False)



