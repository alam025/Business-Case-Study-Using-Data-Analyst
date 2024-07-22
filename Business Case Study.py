#!/usr/bin/env python
# coding: utf-8

# # Business Case Study

# In[42]:


import pandas as pd 
import plotly.express as px
import plotly.io as pio
import plotly.colors as colors
import datetime as datetime
import plotly.graph_objects as go

pio.templates.default ="plotly_white"


# In[21]:


data=pd.read_csv(r"C:\Users\alamm\Downloads\Python Day 28 Data set.csv",encoding='latin-1')


# In[22]:


data.head()


# In[23]:


data.describe()


# In[24]:


data['Order Date']=pd.to_datetime(data['Order Date'])
data['Ship Date']=pd.to_datetime(data['Ship Date'])

data['Order Month']=data['Order Date'].dt.month
data['Order Year']=data['Order Date'].dt.year
data['Order Day of week']=data['Order Date'].dt.dayofweek


# In[25]:


data.head()


# In[26]:


sales_by_month=data.groupby('Order Month')['Sales'].sum().reset_index()
fig=px.line(sales_by_month,x="Order Month",y="Sales",title="Monthly Sales Analysis")
fig.show()


# In[ ]:





# In[32]:


sales_by_category=data.groupby("Category")['Sales'].sum().reset_index()

fig=px.pie(sales_by_category,values="Sales",names="Category",hole=0.5,color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside',textinfo='percent+label')

fig.update_layout(title_text='Sales Analysis by Category',title_font=dict(size=24))

fig.show()
                


# In[ ]:





# In[35]:


profit_by_month=data.groupby('Order Month')['Profit'].sum().reset_index()
fig=px.line(profit_by_month,x="Order Month" , y="Profit",title="Analysis Profits")
fig.show()


# In[ ]:





# In[41]:


profit_by_category=data.groupby('Category')["Profit"].sum().reset_index()
fig=px.pie(profit_by_category,values="Profit",names="Category",hole=0.5,color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside',textinfo='percent+label')

fig.update_layout(title_text='Profit Analysis by Category',title_font=dict(size=24))
fig.show()


# In[ ]:





# In[44]:


sales_profit_by_segment=data.groupby("Segment").agg({'Sales':"sum","Profit":"sum"}).reset_index()
color_palette=colors.qualitative.Pastel
fig=go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                     y=sales_profit_by_segment['Sales'],
                     name="Sales",
                     marker_color=color_palette[6]))

fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                    y=sales_profit_by_segment['Profit'],
                    name="Profit",
                    marker_color=color_palette[0]))

fig.update_layout(title="Sales and Profit Analysis By Customer Segment",
                 xaxis_title="Customer Segment",yaxis_title="Amount")

fig.show()


# In[ ]:





# In[ ]:




