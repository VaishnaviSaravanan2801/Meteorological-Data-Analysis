
# coding: utf-8

# # Project 1 DA using Pandas Scikit_learn Coding Internship

# ## Topic: Performing Analysis of Meteorological Data

# ## Problem Definition

# 
# Perform Data Analysis on the Meteorological Dataset and convert raw information into knowledge. Perform data cleaning, analysis & testing the given hypothesis and then report the conclusion. The given dataset has Apparent temperature and humidity compared monthly across 10 years of the data indicate an increase due to Global warming.
# Find whether the average Apparent temperature for the month of a month say April starting from 2006 to 2016 and the average humidity for the same period have increased or not.

# ## Import the model

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ## Load the dataset

# In[2]:


df = pd.read_csv('F:\Suven Intern\WeatherHistory.csv')
df.head()


# ## Data Preparation

# In[3]:


df.columns


# In[4]:


df.shape


# In[5]:


df.size


# In[6]:


df.describe()


# In[7]:


df.info()


# In[8]:


df.dtypes


# ## Data Cleaning

# In[9]:


df=df.drop(['Summary','Precip Type','Temperature (C)','Wind Speed (km/h)',
            'Wind Bearing (degrees)','Visibility (km)','Pressure (millibars)','Daily Summary'], axis=1)
df.head()


# ## Data Formatting

# In[10]:


df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df=df.set_index('Formatted Date')
df.head(10)


# ## Resampling

# In[11]:


#after resampling
df1 = df[['Apparent Temperature (C)', 'Humidity']] .resample('MS').mean()
df1.head(10)


# In[12]:


import seaborn as sns
import warnings
warnings.filterwarnings ("ignore") 
plt.figure (figsize=(14,6))
plt.title ("Variation in Apparent Temperature and Humidity with time")
sns.lineplot (data=df1)


# ## Data Analysis

# In[13]:


#retrieving the data of a particular month from every year, say Jan
Jan = df1[df1.index.month==1]
print(Jan)
Jan.dtypes


# In[14]:


#retrieving the data of a Feb month from every year
Feb = df1[df1.index.month==2]
print(Feb)
Feb.dtypes


# In[15]:


#retrieving March month from every year
March = df1[df1.index.month==3]
print(March)
March.dtypes


# In[16]:


#retrieving April month from every year
Apr = df1[df1.index.month==4]
print(Apr)
Apr.dtypes


# In[17]:


#retrieving May month from every year
May = df1[df1.index.month==5]
print(May)
May.dtypes


# In[18]:


#retrieving June month from every year
June = df1[df1.index.month==6]
print(June)
June.dtypes


# In[19]:


#retrieving July month from every year
July = df1[df1.index.month==7]
print(July)
July.dtypes


# In[20]:


#retrieving Aug month from every year
Aug = df1[df1.index.month==8]
print(Aug)
Aug.dtypes


# In[21]:


#retrieving Sep month from every year
Sep = df1[df1.index.month==9]
print(Sep)
Sep.dtypes


# In[22]:


#retrieving Oct month from every year
Oct = df1[df1.index.month==10]
print(Oct)
Oct.dtypes


# In[23]:


#retrieving Nov month from every year
Nov= df1[df1.index.month==11]
print(Nov)
Nov.dtypes


# In[24]:


#retrieving Dec month from every year
Dec= df1[df1.index.month==12]
print(Dec)
Dec.dtypes


# ## Data Visualization 

# In[25]:


Jan.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("January")


# In[26]:


Feb.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("February")


# In[27]:


March.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("March")


# In[28]:


Apr.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("April")


# In[29]:


May.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("May")


# In[30]:


June.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("June")


# In[31]:


July.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("July")


# In[32]:


Aug.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("August")


# In[33]:


Sep.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("September")


# In[34]:


Oct.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("October")


# In[35]:


Nov.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("November")


# In[36]:


Dec.plot(kind='line',marker='o')
plt.xlabel("Year")
plt.title("December")


# ## Observation :

# ### - No change in average humidity over the ten years from 2006 to 2016. 

# ### - Increase in average apparent temperature can be seen in the year 2009 then again it dropped in 2010 ,
# ### then a slight increase in 2011 then a significant drop is observed in 2015 and again it increased in 2016.
