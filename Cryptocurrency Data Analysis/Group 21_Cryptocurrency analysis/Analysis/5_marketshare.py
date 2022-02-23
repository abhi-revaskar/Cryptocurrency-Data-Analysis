#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df=pd.read_csv('dataset.csv')
conv_dict={'Rank':int,'Open':float,'High':float,'Low':float,'Volume':float,'Market-cap':float}
df=df.astype(conv_dict)
df.head(10)

df1=df.loc[df['Date'] == "11-11-2021"]
df1.head(100)

listname=list(df1['Name'])
listmarketcap=list(df1['Market-cap'])

namelst=[]
marketcaplst=[]
summ=0
for i in range(100):
    if i<=14:
        namelst.append(listname[i])
        marketcaplst.append(listmarketcap[i])
        if i==14:
            namelst.append('others')
    else:
        summ=summ + listmarketcap[i]
marketcaplst.append(summ)




dt={'market':marketcaplst,'name':namelst}
df1= pd.DataFrame(dt)
fig = px.pie(df1, values='market', names='name')
fig.update_layout(
    title={
        'text': "Market-Share",
         'y':0.959,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.show()

fig.write_html('output/5MarketShare.html', auto_open=False)





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




