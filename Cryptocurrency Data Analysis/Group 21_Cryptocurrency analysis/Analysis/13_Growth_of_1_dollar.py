#!/usr/bin/env python
# coding: utf-8

# In[13]:


import csv
import pandas as pd
import numpy as np
import plotly.graph_objects as cs
from datetime import datetime,date,timedelta

#loading the dataset creating list of required columns
data= pd.read_csv('dataset.csv')
df=pd.DataFrame(data,columns=['Name','Symbol','Date','High','Low','Open','Close'])
name_lst=df.Name.to_list()
sbl_lst=df.Symbol.to_list()
hi_lst=df.High.to_list()
lo_lst=df.Low.to_list()
dt_lst=df.Date.to_list()
opn_lst=df.Open.to_list()
cls_lst=df.Close.to_list()
name_set=set(name_lst)
nm_list=list(name_set)
our_date_list=[]
my_lst=[]
end_date=date(2021,11,11)
start_date=date(2020,11,11)
timestampStr='String'
day_count = (end_date - start_date).days + 1
for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
    dt=single_date.strftime("%d-%m")
    if(dt=="11-11"):
            timestampStr = single_date.strftime("%d-%m-%Y")
            our_date_list.append(timestampStr)
    timestampStr = single_date.strftime("%d-%m-%Y")
    my_lst.append(timestampStr)

#declaring empty lists for output plotting
import matplotlib.pyplot as plt
prc_in_doll=[]
date1=[]
ind=[i for i in range(len(name_lst)) if name_lst[i]=='Bitcoin' and dt_lst[i] in my_lst]

count1=0
for k in ind:
    if dt_lst[k]==our_date_list[0]:
        num=1/cls_lst[k]
        prc_in_doll.append(1)
        count1=count1+1
        date1.append(dt_lst[k])
    else:
        prc_in_doll.append(cls_lst[k]*num)
        date1.append(dt_lst[k])

prc_in_doll1=[]
ind=[i for i in range(len(name_lst)) if name_lst[i]=='Ethereum' and dt_lst[i] in my_lst]

count1=0
for k in ind:
    if dt_lst[k]==our_date_list[0]:
        num=1/cls_lst[k]
        prc_in_doll1.append(1)
        count1=count1+1
    else:
        prc_in_doll1.append(cls_lst[k]*num)
        
prc_in_doll2=[]
ind=[i for i in range(len(name_lst)) if name_lst[i]=='Binance Coin' and dt_lst[i] in my_lst]

count1=0
for k in ind:
    if dt_lst[k]==our_date_list[0]:
        num=1/cls_lst[k]
        prc_in_doll2.append(1)
        count1=count1+1
    else:
        prc_in_doll2.append(cls_lst[k]*num)
        

bit={"x":pd.date_range('11/11/2020', periods=366),"y":prc_in_doll,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"red"
       },
       "name":"Bitcoin"
      }
eth={"x":pd.date_range('11/11/2020', periods=366),"y":prc_in_doll1,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"black"
       },
       "name":"Ethereum"
      }
bcn={"x":pd.date_range('11/11/2020', periods=366),"y":prc_in_doll2,"type":"scatter","mode":"lines",
       "line":{
           "width":1,
           "color":"green"
       },
       "name":"Binance Coin"
      }
fig = cs.Figure(data=[bit,eth,bcn])
fig.update_layout(title='Growth of 1 dollar',yaxis_title='Growth($)',xaxis_title='Date',xaxis_rangeslider_visible=True)
fig.show()
fig.write_html('output/13Growth_of_1$.html', auto_open=False)


# In[ ]:





# In[ ]:





# In[ ]:




