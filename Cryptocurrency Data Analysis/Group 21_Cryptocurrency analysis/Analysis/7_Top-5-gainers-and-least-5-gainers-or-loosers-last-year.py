#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import numpy as np
from datetime import datetime,date,timedelta


# In[2]:


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

# declaring empty lists to take inputs

curr_name=[]
gain_lst=[]
gain_loss=[]
rank=[]
# iteratively calculating the loss and gain
for i in nm_list:
    indx=[j for j in range(len(name_lst)) if name_lst[j]==i]
    cls=0
    opn=0
    diff1=0
    for k in indx:
        if(dt_lst[k]==our_date_list[0]):
            opn=opn_lst[k]
        elif(dt_lst[k]==our_date_list[1]):
            cls=cls_lst[k]
    diff1=cls-opn
    if (diff1>=0):
        gain_loss.append(diff1)
        gain_lst.append('Gainer')
        
    else:
        gain_loss.append(abs(diff1))
        gain_lst.append('Looser')
    curr_name.append(i)

#Sorting the loss or gain accorgingly
new_dir2={'Currency-Name':curr_name,'Type':gain_lst,'Gain-Loss':gain_loss}
final_frame1=pd.DataFrame(new_dir2)
final_frame1=final_frame1.sort_values(by=['Gain-Loss'],ascending=False)
final_frame1=final_frame1[:5]
new_dir3={'Currency-Name':curr_name,'Type':gain_lst,'Gain-Loss':gain_loss}
final_frame2=pd.DataFrame(new_dir3)
final_frame2=final_frame2.sort_values(by=['Gain-Loss'],ascending=True)
final_frame2=final_frame2[:5]
ff=pd.concat([final_frame1,final_frame2],axis=0)
ff.to_csv('output/7Top-5-gainers-and-least-5-gainers-or-loosers-last-year.csv',index=0)


# In[ ]:





# In[ ]:





# In[ ]:




