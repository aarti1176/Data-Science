#!/usr/bin/env python
# coding: utf-8

# # Exploratory data analysis 
# #Zomato Data Set   

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


df=pd.read_csv("zomato.csv",encoding='latin-1')
df.head()


# In[10]:


df.columns


# In[11]:


df.info()


# In[12]:


df.describe()


# # Data Analysis
# # missing value
# # Explore numrical and categorical values
# # Relationship between features

# In[20]:


df.shape


# In[14]:


df.isnull().sum()


# In[18]:


[features for features in df.columns if df[features].isnull().sum()>0]
#List comprehension


# In[73]:


#Plotting for Heat Map
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')


# In[24]:


df_country=pd.read_excel('Country-code.xlsx')
df_country.head()


# In[25]:


df.columns


# # Combining datasets zomato.csv and Country-code.xlsx because they have a common column named Country Code. joing both data sets using 'merge' and putting it in df_final dataset.
# 

# In[27]:


df_final=pd.merge(df,df_country, on='Country Code', how='left')


# In[29]:


df_final.head(2)


# In[30]:


# To check data types
df_final.dtypes


# In[31]:


df_final.columns


# In[36]:


df_final.Country.value_counts()


# In[37]:


Country_names=df_final.Country.value_counts().index #y-axis for pie chart


# In[40]:


Country_val=df_final.Country.value_counts().values #x-axis for pie chart


# In[51]:


# Pie Chart
plt.pie(Country_val[:3],labels=Country_names[:3],autopct='%1.2f%%') #Top 3 countries that use Zomato


# Observation: The country with maximum % records of transactions are from India, then United States and 3rd is United Kingdom.

# In[53]:


df_final.columns


# In[65]:


ratings=df_final.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'}) 
#to chande it to a data frame
#and doing indexing and where column is 0 change it to Rating Count.


# In[66]:


ratings


# # Observation
# 1.When rating is between 4.5 to 4.9....> Excellent
# 2.When rating is between 4.0 to 4.4....> very good
# 3.When rating is between 3.5 to 3.9....> good
# 4.When rating is between 2.5 to 3.4.....> average
# 5.When rating is between 1.8 to 2.4.....> poor
# 

# In[67]:


ratings.head()


# In[75]:


import matplotlib
matplotlib.rcParams['figure.figsize']= (12, 6)
sns.barplot(x='Aggregate rating',y='Rating Count', data=ratings)


# In[79]:


# Mapping color according to the rating
sns.barplot(x='Aggregate rating',y='Rating Count',hue='Rating color', data=ratings, palette=['white', 'red', 'orange', 'yellow', 'green', 'green'])


# In[ ]:


# Observation
1. Not rated count is very high
2. Maximum rating is between 2.5 to 3.4


# In[80]:


# Count plot
sns.countplot(x='Rating color', data=ratings, palette=['white', 'red', 'orange', 'yellow', 'green', 'green'])


# In[81]:


ratings


# In[ ]:


# Countries that has given 0 ratings


# In[85]:


df_final[df_final['Rating color']=='White'].groupby('Country').size().reset_index()


# In[91]:


df_final.groupby(['Aggregate rating', 'Country']).size().reset_index().head(5)


#  Observation
# Maximum number of 0 ratings is from India
# 

# In[93]:


# Which currency is used by which country?
df_final.columns


# In[96]:


df_final.groupby(['Country', 'Currency']).size().reset_index()


# In[101]:


# Another method to see the country and currency is:
df_final[['Country', 'Currency']].groupby(['Country','Currency']).size().reset_index()


# In[109]:


# Which Country do have online delivery options
df_final[df_final['Has Online delivery']=='Yes'].Country.value_counts()


# In[110]:


# Another method to see the countries which has online delivery
df_final.groupby(['Has Online delivery' ,'Country']).size().reset_index()


# # Observation
# 1.Online deliveries are available in India and UAE

# In[112]:


# Create a pie chart for cities distribution
df_final.columns


# In[115]:


df_final.City.value_counts().reset_index()


# In[122]:


City_labels=df_final.City.value_counts().index


# In[123]:


City_val=df_final.City.value_counts().values


# In[127]:


# Top 5 City distribution
plt.pie(City_val[:5],labels=City_labels[:5],autopct='%1.2f%%')


# In[128]:


# Find Top 10 cuisines
df_final.columns


# In[139]:


df_final.Cuisines.value_counts().reset_index().head(10)


# In[ ]:




