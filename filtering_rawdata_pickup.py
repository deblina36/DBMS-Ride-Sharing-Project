#!/usr/bin/env python
# coding: utf-8

# In[265]:


import numpy as np
import pandas as pd
from datetime import datetime, date


# In[266]:


df_pickup=pd.read_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\pickup\dec_pickup.csv')


# In[267]:


df_pickup.head()


# In[268]:


len(df_pickup)


# 40.7769° N, 73.8740° W

# In[269]:


#df_pickup=df.loc[df.apply(lambda row: row.pickup_longitude>-73.884756 and row.pickup_longitude<-73.857505 and row.pickup_latitude>40.7676 and row.pickup_latitude<40.7818, axis = 1)]


# In[270]:


#df_dropoff=df.loc[df.apply(lambda row: row.dropoff_longitude>-73.884756 and row.dropoff_longitude<-73.857505 and row.dropoff_latitude>40.7676 and row.dropoff_latitude<40.7818, axis = 1)]


# In[271]:


df_pickup.head()


# In[272]:


#df_dropoff.head()


# In[273]:


df_pickup=df_pickup.drop(['VendorID','RatecodeID','store_and_fwd_flag','payment_type','fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge','total_amount'], axis=1)


# In[274]:


#df_dropoff=df_dropoff.drop(['VendorID','RatecodeID','store_and_fwd_flag','payment_type','fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge','total_amount'], axis=1)


# In[275]:


df_pickup = df_pickup.sort_values('tpep_pickup_datetime')
#df_dropoff =df_dropoff.sort_values('tpep_pickup_datetime')


# In[276]:


df_pickup.head()


# In[277]:


df_pickup['tpep_pickup_datetime']=pd.to_datetime(df_pickup['tpep_pickup_datetime'], format="%Y-%m-%d %H:%M:%S")
df_pickup['tpep_dropoff_datetime']=pd.to_datetime(df_pickup['tpep_dropoff_datetime'], format="%Y-%m-%d %H:%M:%S")


# In[278]:


df_pickup['pickup_date'] = [d.date() for d in df_pickup['tpep_pickup_datetime']]
df_pickup['pickup_time'] = [d.time() for d in df_pickup['tpep_pickup_datetime']]
df_pickup['dropoff_time'] = [d.time() for d in df_pickup['tpep_dropoff_datetime']]


# In[279]:


df_pickup.head()


# In[280]:


#df_dropoff['tpep_pickup_datetime']=pd.to_datetime(df_dropoff['tpep_pickup_datetime'], format="%Y-%m-%d %H:%M:%S")
#df_dropoff['tpep_dropoff_datetime']=pd.to_datetime(df_dropoff['tpep_dropoff_datetime'], format="%Y-%m-%d %H:%M:%S")


# In[281]:


#df_dropoff['pickup_date'] = [d.date() for d in df_dropoff['tpep_pickup_datetime']]
#df_dropoff['pickup_time'] = [d.time() for d in df_dropoff['tpep_pickup_datetime']]
#df_dropoff['dropoff_time'] = [d.time() for d in df_dropoff['tpep_dropoff_datetime']]


# In[282]:


#df_dropoff.head()


# In[283]:


df_pickup=df_pickup.drop(['tpep_pickup_datetime','tpep_dropoff_datetime'], axis=1)
#df_dropoff=df_dropoff.drop(['tpep_pickup_datetime','tpep_dropoff_datetime'], axis=1)


# In[284]:


df_pickup.head()


# In[285]:


#df_dropoff.head()


# In[286]:


df_pickup=df_pickup.reset_index(drop=True)
#df_dropoff=df_dropoff.reset_index(drop=True)


# In[287]:


df_pickup.index.name = 'TripID'
#df_dropoff.index.name= 'TripID'


# In[288]:


column_names=['pickup_date','pickup_time','dropoff_time','passenger_count','trip_distance','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude']
df_pickup = df_pickup.reindex(columns=column_names)
#df_dropoff = df_dropoff.reindex(columns=column_names)


# In[289]:


#df_pickup.to_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\2016\pickup\jun_pickup.csv')


# In[290]:


#df_dropoff.to_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\2016\dropoff\jun_dropoff.csv')


# In[291]:


df_pickup=df_pickup[abs(df_pickup.dropoff_longitude-df_pickup.dropoff_longitude.mean()) <= (3*df_pickup.dropoff_longitude.std())]


# In[292]:


df_pickup=df_pickup[abs(df_pickup.dropoff_latitude-df_pickup.dropoff_latitude.mean()) <= (3*df_pickup.dropoff_latitude.std())]


# In[293]:


#df_outlier=pd.read_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\2016\pickup\may_pickup_before.csv')


# In[294]:


df_pickup.to_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\2015\pickup\dec_pickup_new.csv')


# In[295]:


len(df_pickup)


# In[296]:


#df_outlier=df_outlier[abs(df_outlier.dropoff_longitude-df_outlier.dropoff_longitude.mean()) <= (3*df_outlier.dropoff_longitude.std())]


# In[297]:


#df_outlier=df_outlier[abs(df_outlier.dropoff_latitude-df_outlier.dropoff_latitude.mean()) <= (3*df_outlier.dropoff_latitude.std())]


# In[298]:


#len(df_outlier)


# In[299]:


#df_outlier.to_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\2016\pickup\may_pickup_2016.csv')


# In[300]:


#df_outlier.head()


# In[301]:


#df_check=pd.read_csv(r'C:\Users\srika\OneDrive\Desktop\Spring20\Subjects\ADBMS\Project\Filtereddatasets\2016\may_pickup_after.csv')


# In[302]:


#len(df_check)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




