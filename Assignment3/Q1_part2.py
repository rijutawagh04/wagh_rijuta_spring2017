
# coding: utf-8

# In[4]:

from pandas import Series, DataFrame 
import pandas as pd
import numpy as np
vehicle = pd.read_csv('C:/Users/mahesh/Desktop/Data analysis spring 2017/Data_Analysis_Assignments/wagh_rijuta_spring2017/Assignment 3/Data/vehicle_collisions.csv')
df = DataFrame(vehicle)
df.head()


# In[ ]:

###Distribution of each collision scale(one car involved, two car involved) for each borough from 2015 to present


# In[5]:

df1 = df.groupby(['BOROUGH'],sort = False)['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE'].count().reset_index()

df2= DataFrame() #creating an empty dataframe

df2['BOROUGH'] = df1['BOROUGH']  # copying Borough column to the new dataframe
df2['One_Vehicle_Involved'] = df1['VEHICLE 1 TYPE'] - df1['VEHICLE 2 TYPE'] #count of one Vehicle involved
df2['Two_Vehicles_Involved'] = df1['VEHICLE 2 TYPE'] - df1['VEHICLE 3 TYPE'] #count of two Vehicles involved
df2['Three_Vehicles_Involved'] = df1['VEHICLE 3 TYPE'] - df1['VEHICLE 4 TYPE'] # count of three Vehicles involved
df2['More_Vehicle_Involved'] = df1['VEHICLE 4 TYPE'] #count of more Vehicles involved
df2.set_index('BOROUGH', inplace = True)
df2


# In[6]:

df2.to_csv('Q1_part2.csv')


# In[ ]:



