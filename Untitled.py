#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("matches.csv")


# In[3]:


df


# In[8]:


df.isnull()


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


# Total number of Column and rows presents in data sets
df.shape


# In[10]:


# returns the total no.of rows presents in datasets
df.shape[0]


# In[11]:


# returns the total no.of columns presents in datasets
df.shape[1]


# In[12]:


# iloc is the function provide specific rows information
df.iloc[0]


# In[13]:


# fetch the specific column information
df.iloc[0,7]


# In[14]:


df.iloc[0,14]


# In[15]:


# fetch specific rows from dataset
df.iloc[[0,7,2]]


# In[16]:


df.index


# In[17]:


df['winner']


# In[18]:


type(df['winner'])


# In[19]:


# convert series into dataframes use 'reset_index()'.
df['winner'].reset_index()


# In[20]:


type(df['winner'].reset_index())


# In[21]:


# Total Win by each teams/// this is series type..
df['winner'].value_counts()


# In[64]:


# series type
myseries=df['winner'].value_counts()
myseries


# In[65]:


# fetch specific value[Royal Challengers Bangalore won 73 matches ]
myseries['Royal Challengers Bangalore']


# In[68]:


# so here team1 played number of matches
df['team1'].value_counts()


# In[69]:


# so here team2 played number of matches
df['team2'].value_counts()


# In[89]:


# find total matches played by team1 and team2
(df['team1'].value_counts()+df['team2'].value_counts()).sort_values(ascending=False)


# In[72]:


# total decision 
df['toss_decision'].value_counts()


# In[73]:


df['toss_decision'].value_counts().plot(kind='pie')


# In[22]:


# dataframe type..
df['winner'].value_counts().reset_index()


# In[23]:


df['winner'].value_counts().plot(kind='bar')


# In[24]:


mask=df['city']=='Hyderabad'
mask.head(22)


# In[59]:


man_of_match=df['player_of_match'].value_counts().head(20)
man_of_match


# In[60]:


man_of_match.plot(kind='bar')


# In[27]:


df.drop_duplicates('season',keep='last')[['season','winner']]


# In[28]:


# fetch final winner along with team runnerup team, team1 and team2
winners=df.drop_duplicates('season',keep='last')[['season','team1','team2','winner']].sort_values(by='season')


# In[29]:


winners


# In[30]:


# fetch final winner along with player_of_match
df.drop_duplicates('season',keep='last')[['season','team1','team2','winner','player_of_match']]


# In[31]:


win=df.drop_duplicates('season',keep='last')[['season','winner','venue','win_by_runs','win_by_wickets']]
win.sort_values(by='season').reset_index()


# In[32]:


# this is boolean searies
df['city']=='Hyderabad'


# In[33]:


# now add in variable
# fetch only city name of hyderabad
mask=df['city']=='Hyderabad'
df[mask]


# In[34]:


# count total matches palyed in hyderabad
mask=df['city']=='Hyderabad'
df[mask].shape[0]


# In[35]:


def get_city_matchcount(city):
    mask=df['city']==city
    return df[mask]
    


# In[36]:


get_city_matchcount('Mumbai').shape[0]


# In[38]:


# fetch matches played in Mumbai after 2010
mask=df['city']=='Mumbai'
mask1=df['season']>2010
df[mask & mask1].shape[0]


# In[39]:


def match_winner(winner):
    win=df['winner']==winner
    return df[win]
    


# In[48]:


match_winner('Mumbai Indians')


# In[44]:


match_winner('Mumbai Indians').shape


# In[97]:


# operning matches winner by each ipl season
df.drop_duplicates('season',keep='first')[['season','team1','team2','winner',]].sort_values(by='season')


# In[ ]:




