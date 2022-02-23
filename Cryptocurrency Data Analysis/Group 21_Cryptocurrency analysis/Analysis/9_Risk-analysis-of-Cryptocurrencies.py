#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from datetime import datetime
import statistics

crypto = pd.read_csv("dataset.csv")

## Daily gain percentage 

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



curr_lst=[]
type_lst=[]
factor_lst=[]
cnt=0
for i in licurr:
    zscr_lst=[]
    zscr_lst=(stats.zscore(dictgain[i]))
    fact=statistics.stdev(dictgain[i])
    leng= len(zscr_lst)
    count=0
    if (fact<8):
        type_lst.append("Not-Risky")
        curr_lst.append(i)
        factor_lst.append(fact)
    else:
        type_lst.append("Risky")
        curr_lst.append(i)
        factor_lst.append(fact)

new_dir={'Currency-Name':curr_lst,'Risk-or-not':type_lst,'Risk-factor':factor_lst}
ff1=pd.DataFrame(new_dir)
ff1=ff1.sort_values(by=['Risk-or-not','Risk-factor'])
ff1.to_csv('output/9Risk-analysis-of-Cryptocurrencies.csv',index=0)


