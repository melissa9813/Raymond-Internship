#!/usr/bin/env python
# coding: utf-8

# # Raymond Industrial Ltd
# ## Assignment 2: Python vs Excel
# ### Melissa Eom
# - Datasets obtained from Kaggle (https://www.kaggle.com/olistbr/brazilian-ecommerce)

# In[1]:


# import libraries

import pandas as pd
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import warnings
warnings.filterwarnings('ignore')


# ## Data Load

# In[2]:


df = pd.read_csv('https://github.com/melissa9813/brazil_ecommerce_analysis/blob/main/Brazilian%20E-Commerce%20Public%20Dataset/olist_products_dataset.csv?raw=true')
df_eng = pd.read_csv('https://github.com/melissa9813/brazil_ecommerce_analysis/raw/main/Brazilian%20E-Commerce%20Public%20Dataset/product_category_name_translation.csv')


# ## Data Preprocessing

# In[3]:


# Check # of Null
df.isnull().sum()


# In[4]:


# Delete Null 
df_clean = df.dropna(axis=0)
df_clean.isnull().sum()


# In[5]:


# Count # of rows and columns
df_clean.shape


# In[6]:


df_clean.head()


# In[7]:


# Get descriptive statistics
df_clean.describe()


# ## Merge Two Tables
# #### To translate Portuguese category name into English

# In[8]:


df_eng.head()


# In[9]:


# Merge two tables
df_merge = pd.merge(df_clean, df_eng, how='inner', on=['product_category_name'])
# df_merge.drop_duplicates(inplace=True)
df_merge.reset_index(drop=True, inplace=True)
df_merge


# ## Analysis
# ### Step 1) Get average weight by product category

# In[10]:


# Average weight for each product category
temp = pd.DataFrame(df_merge.groupby(by=['product_category_name_english'])['product_weight_g'].mean().reset_index())
temp


# ### 2. Get Top 10

# In[11]:


# Get top 10
top_10 = temp.sort_values(by='product_weight_g', ascending=False)
top_10.reset_index(drop=True, inplace=True)
top_10 = top_10[:10]
top_10


# ## Data Visualization

# In[12]:


# Graph top_10

plt.figure(figsize=(20,10))
sns.barplot(data=top_10, y='product_weight_g', x='product_category_name_english', palette="Blues")
plt.xticks(rotation=30, fontsize=12)
plt.xlabel("Category", fontsize=15)
plt.ylabel("Weight (g)", fontsize=15)
plt.title("Avg Delivery Time by Product Category", fontsize=20)

