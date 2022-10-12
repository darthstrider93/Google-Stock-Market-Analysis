#!/usr/bin/env python
# coding: utf-8

# #### To analyze the stock market, we will collect the stock price data of Google. 
# ##### Let’s start by collecting the stock price data of Google. here we will use the yfinance API of Yahoo Finance for such

# In[1]:


pip install yfinance


# In[1]:


#import libraries
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px


# In[2]:


#Establishing dates
today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date =d2


# In[3]:


#Get data for stock by google. 
data = yf.download('GOOG', start=start_date, end=end_date, progress=False)
data["Date"] =data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
data.head()


# In[4]:


#Analyse the pirce movement of stock by candlestick chart
figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"],
                                        high=data["High"], low=data["High"],close=data["Close"])])
figure.update_layout(title="Google Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()


# In[5]:


# Box plot to visualize the analyse Stock market
figure = px.bar(data, x="Date", y="Close")
figure.show()


# In[6]:


# Employing range slider to analyse between two specific points
figure = px.line(data, x="Date", y="Close", title="Stock Market Analysis using Rangeslider")
figure.update_xaxes(rangeslider_visible=True)
figure.show()


# In[7]:


#Using time period selector for an interactive approach
figure = px.line(data, x='Date', y='Close',title='Stock Market Analysis with Time Period Selectors')

figure.update_xaxes(rangeselector=dict(buttons=list([dict(count=1, label="1m", step="month", stepmode="backward"),
                                                     dict(count=6, label="6m", step="month", stepmode="backward"),
                                                     dict(count=3, label="3m", step="month", stepmode="backward"),
                                                     dict(count=1, label="1y", step="year", stepmode="backward"),
                                                     dict(step="all")])))
figure.show()


# In[10]:


#Removing weekends to better identfy trends
figure = px.scatter(data, x='Date', y='Close', range_x=['2021-07-12', '2022-07-11'],
                    title="Stock Market Analysis by Hiding Weekend Gaps")
figure.update_xaxes(rangebreaks=[dict(bounds=["sat", "sun"])])
figure.show()


# In[ ]:




