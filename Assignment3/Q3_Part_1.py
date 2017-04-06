
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
from pandas import DataFrame


# In[5]:

cricket = pd.read_csv('C:/Users/mahesh/Desktop/Data analysis spring 2017/Data_Analysis_Assignments/wagh_rijuta_spring2017/Assignment 3/Data/cricket_matches.csv')
df = DataFrame(cricket)
print(df.head())


# ## Average Score of team which hosts and runs the game

# In[6]:

df1 = DataFrame(df, columns = ['home','winner','innings1_runs','innings2_runs','innings1','innings2','score','avg_score'])
df2 = DataFrame(columns = ['avg_score',])
#df1['avg'] = (df1['innings1_runs']+df1['innings2_runs'])/2
df1 = df1[df1['home']==(df1['winner'])]
df1['score'] = df1['innings1_runs'].where(df1['home'] == df1['innings1'], df1['innings2_runs'])
df2['avg_score'] = df1.groupby('home')['score'].mean()
df2
#df1['score'] =(df1['innings1_runs'] + df1['innings2_runs'])/2



# In[7]:

df2.to_csv('Q3_part1.csv')

