#!/usr/bin/env python
# coding: utf-8

# In[217]:


import numpy as np
import pandas as pd
from datetime import datetime, date


# In[218]:


df_dropoff=pd.read_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\dropoff\dec_dropoff.csv')


# In[219]:


df_dropoff.head()


# In[220]:


len(df_dropoff)


# 40.7769° N, 73.8740° W

# In[221]:


#df_pickup=df.loc[df.apply(lambda row: row.pickup_longitude>-73.884756 and row.pickup_longitude<-73.857505 and row.pickup_latitude>40.7676 and row.pickup_latitude<40.7818, axis = 1)]


# In[222]:


#df_dropoff=df.loc[df.apply(lambda row: row.dropoff_longitude>-73.884756 and row.dropoff_longitude<-73.857505 and row.dropoff_latitude>40.7676 and row.dropoff_latitude<40.7818, axis = 1)]


# In[223]:


#df_pickup.head()


# In[224]:


df_dropoff.head()


# In[225]:


#df_pickup=df_pickup.drop(['VendorID','RatecodeID','store_and_fwd_flag','payment_type','fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge','total_amount'], axis=1)


# In[226]:


df_dropoff=df_dropoff.drop(['VendorID','RatecodeID','store_and_fwd_flag','payment_type','fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge','total_amount'], axis=1)


# In[227]:


#df_pickup = df_pickup.sort_values('tpep_pickup_datetime')
df_dropoff =df_dropoff.sort_values('tpep_pickup_datetime')


# In[228]:


df_dropoff.head()


# In[229]:


#df_pickup['tpep_pickup_datetime']=pd.to_datetime(df_pickup['tpep_pickup_datetime'], format="%Y-%m-%d %H:%M:%S")
#df_pickup['tpep_dropoff_datetime']=pd.to_datetime(df_pickup['tpep_dropoff_datetime'], format="%Y-%m-%d %H:%M:%S")


# In[230]:


#df_pickup['pickup_date'] = [d.date() for d in df_pickup['tpep_pickup_datetime']]
#df_pickup['pickup_time'] = [d.time() for d in df_pickup['tpep_pickup_datetime']]
#df_pickup['dropoff_time'] = [d.time() for d in df_pickup['tpep_dropoff_datetime']]


# In[231]:


#df_pickup.head()


# In[232]:


df_dropoff['tpep_pickup_datetime']=pd.to_datetime(df_dropoff['tpep_pickup_datetime'], format="%Y-%m-%d %H:%M:%S")
df_dropoff['tpep_dropoff_datetime']=pd.to_datetime(df_dropoff['tpep_dropoff_datetime'], format="%Y-%m-%d %H:%M:%S")


# In[233]:


df_dropoff['pickup_date'] = [d.date() for d in df_dropoff['tpep_pickup_datetime']]
df_dropoff['pickup_time'] = [d.time() for d in df_dropoff['tpep_pickup_datetime']]
df_dropoff['dropoff_time'] = [d.time() for d in df_dropoff['tpep_dropoff_datetime']]


# In[234]:


df_dropoff.head()


# In[235]:


#df_pickup=df_pickup.drop(['tpep_pickup_datetime','tpep_dropoff_datetime'], axis=1)
df_dropoff=df_dropoff.drop(['tpep_pickup_datetime','tpep_dropoff_datetime'], axis=1)


# In[236]:


#df_pickup.head()


# In[237]:


df_dropoff.head()


# In[238]:


#df_pickup=df_pickup.reset_index(drop=True)
df_dropoff=df_dropoff.reset_index(drop=True)


# In[239]:


#df_pickup.index.name = 'TripID'
df_dropoff.index.name= 'TripID'


# In[240]:


column_names=['pickup_date','pickup_time','dropoff_time','passenger_count','trip_distance','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']
#df_pickup = df_pickup.reindex(columns=column_names)
df_dropoff = df_dropoff.reindex(columns=column_names)


# In[246]:


df_dropoff=df_dropoff[abs(df_dropoff.pickup_longitude-df_dropoff.pickup_longitude.mean()) <= (3*df_dropoff.pickup_longitude.std())]


# In[247]:


df_dropoff=df_dropoff[abs(df_dropoff.pickup_latitude-df_dropoff.pickup_latitude.mean()) <= (3*df_dropoff.pickup_latitude.std())]


# In[248]:


len(df_dropoff)


# In[249]:


df_dropoff.to_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\2015\dropoff\dec_dropoff_new.csv')


# In[250]:





# In[251]:





# In[252]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




