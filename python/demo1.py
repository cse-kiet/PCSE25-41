#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('C:\\Users\\abhis\\Downloads\\student_results.csv')
print(df)
print(type(df))


# In[2]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv')
print(df1)


# In[3]:


type(df1)


# In[4]:


df1.columns


# In[5]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', nrows=5)
print(df1)


# In[6]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', usecols=[0])
print(df1)


# In[7]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', na_values= ['non available','no value'])
print(df1)


# In[8]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', na_values= {'industry':'no value'})
print(df1)


# In[9]:


df2=pd.read_csv('C:\\Users\\abhis\\Downloads\\Top-10-IT-Companies-in-India.csv')
print(df2)


# In[10]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', usecols=[1,2])
print(df1)


# In[11]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', usecols=[2,4])
print(df1)


# In[12]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', skiprows=1)
print(df1)


# In[13]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', skiprows=2)
print(df1)


# In[14]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', skiprows=[0])
print(df1)


# In[15]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', index_col='ID')
print(df1)


# In[16]:


df1=pd.read_csv('C:\\Users\\abhis\\Downloads\\Fortune_10.csv', index_col= 'Name')
print(df1)


# In[ ]:




