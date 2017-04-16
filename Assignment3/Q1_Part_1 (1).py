
# coding: utf-8

# In[4]:

from pandas import DataFrame
import pandas as pd
import numpy as np
import os
vehicle = pd.read_csv('C:/Users/mahesh/Desktop/Data analysis spring 2017/Data_Analysis_Assignments/wagh_rijuta_spring2017/Assignment 3/Data/vehicle_collisions.csv')
df = DataFrame(vehicle)
df

#df = pd.read_csv(os.path.join(os.path.dirname(__file__), "..Data analysis spring 2017/Data_Analysis_Assignments/wagh_rijuta_spring2017/Assignment 3/Data/vehicle_collisions.csv"))


# ### Percentage of collisions in Manhattan for each month in 2016

# In[10]:

import datetime
import calendar
df['DATE'] = pd.to_datetime(vehicle['DATE']) 

df1 = df[(df['DATE'] > '2015-12-31') & (df['DATE'] < '2017-01-01')]
df1['MONTH'] = df['DATE'].dt.month
#newFrame=frame[(frame.DATE > '2015-12-31') & (frame.DATE < '2017-01-01')]
#df1['MONTH'] = df1['MONTH'].apply(lambda x: calendar.month_abbr[x])
print(df1.head())



# In[7]:

df2 = DataFrame(columns = ['Manhattan','NYC','Percentage'])
df2



# In[8]:


#df1['Month']= df['DATE'].apply(lambda x: calendar.month_abbr[int(x.split("/")[0])])
df2['Manhattan'] = df1[df1['BOROUGH']=='MANHATTAN'].groupby(['MONTH'],sort = False)['UNIQUE KEY'].count()
df2['NYC']=df1.groupby(['MONTH'])['UNIQUE KEY'].count()
df2['Percentage']= (df2['Manhattan']/df2['NYC'])
df2


# In[9]:

df1.to_csv('Q1_part1.csv')


# In[ ]:



