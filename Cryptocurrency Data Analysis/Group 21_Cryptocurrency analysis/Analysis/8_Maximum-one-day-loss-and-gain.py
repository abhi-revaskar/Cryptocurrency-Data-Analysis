#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import numpy as np
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

#declaring empty lists to take outputs
curr_name=[]
date_loss=[]
date_gain=[]
gain_prcnt=[]
loss_prcnt=[]

#Calculating the values iteratively
for i in nm_list:
    idx=[j for j in range(len(name_lst)) if name_lst[j]==i]
    profit=0
    loss=0
    dt_loss='abc'
    dt_prft='mno'
    for k in idx:
        diff=cls_lst[k]-opn_lst[k]
        if (diff>0):
            if(profit<diff):
                profit=diff
                dt_prft=dt_lst[k]
        elif (diff<0):
            if(loss>diff):
                loss=diff
                dt_loss=dt_lst[k]
    curr_name.append(i)
    date_loss.append(dt_loss)
    date_gain.append(dt_prft)
    gain_prcnt.append(profit)
    loss_prcnt.append(abs(loss))
    

#assigning the list of output values to the headings and outputting the csv file as output
new_dir={'Currency-Name':curr_name,'Maximum-loss':loss_prcnt,'Loss-Date':date_loss,'Maximum-gain':gain_prcnt,'Gain-Date':date_gain}
final_frame=pd.DataFrame(new_dir)
final_frame=final_frame.sort_values(by=['Currency-Name'],ascending=True)
final_frame.to_csv('output/8Maximum-one-day-loss-gain.csv',index=False)

