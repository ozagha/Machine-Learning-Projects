#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Instagram Reach Analysis using Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

data = pd.read_csv("Instagram_data.csv", encoding = 'latin1')
#print(data.head())

# Checking dataset if it contains any null values or not:
data.isnull().sum()

# To drop all null values 
data = data.dropna()

# Shows all the columns to understand the data types in the columns
data.info()

# C:\Users\Windows\anaconda3\lib\site-packages\seaborn\distributions.py:2619: 
# FutureWarning: `distplot` is a deprecated function and will be removed in a 
# future version. Please adapt your code to use either `displot` 
# (a figure-level function with similar flexibility) or `histplot` 
# (an axes-level function for histograms).warnings.warn(msg, FutureWarning)

plt.figure(figsize=(20, 5))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Home")
sns.histplot(data['From Home'])

plt.figure(figsize=(20, 5))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Hashtags")
sns.histplot(data['From Hashtags'])

plt.figure(figsize=(20, 5))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Profile Visits")
sns.histplot(data['Profile Visits'])

plt.show()


# In[ ]:




