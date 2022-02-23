#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import numpy as np
from datetime import datetime,date,timedelta


# In[3]:


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
# declaring empty lists to take inputs

curr_name=[]
high_lst=[]
high_date=[]
low_date=[]
low_lst=[]
#Iteratively calculating or fetching highest value of the year for each crypto currency
for i in nm_list:
    indx1=[j for j in range(len(name_lst)) if name_lst[j]==i]
    high=0
    dt=0
    for k in indx1:
        if(high<hi_lst[k]):
            high=hi_lst[k]
            dt=dt_lst[k]
    low=1000000000000000
    dtl=0
    for k in indx1:
        if(low>lo_lst[k]):
            low=lo_lst[k]
            dtl=dt_lst[k]
    curr_name.append(i)
    high_lst.append(high)
    high_date.append(dt)
    low_lst.append(low)
    low_date.append(dtl)

new_dir5={'Currency-Name':curr_name,'High':high_lst,'Date-high':high_date,'Low':low_lst,'Date-low':low_date}
final_frame12=pd.DataFrame(new_dir5)
final_frame12=final_frame12.sort_values(by=['Currency-Name'],ascending=True)
final_frame12.to_csv('output/652-week-high-low.csv',index=0)


# In[ ]:





# In[ ]:




