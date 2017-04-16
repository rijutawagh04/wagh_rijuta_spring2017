
# coding: utf-8

# In[25]:

# Importing all the libraries
import pandas as pd
from pandas import DataFrame
import numpy as np
import calendar


# In[26]:

# Reading the csv file
movie=pd.read_csv('C:/Users/mahesh/Desktop/Data analysis spring 2017/Data_Analysis_Assignments/wagh_rijuta_spring2017/Assignment 3/Data/movies_awards.csv')
print(movie.head())


# ## Extracting the wins and nominations according to the awards in their respective columns

# In[27]:


movie['Awards_Won'] = movie['Awards'].str.extract('(\d+) win', expand=True)
movie['Awards_Nominated'] = movie['Awards'].str.extract('(\d+) nomination', expand=True)
movie['PrimeAwards_Won']= movie['Awards'].str.extract('Won (\d+) Primetime', expand=True)
movie['PrimeAwards_Nominations']= movie['Awards'].str.extract('Nominated for (\d+) Primetime', expand=True)
movie['BaftaAwards_Won']= movie['Awards'].str.extract('Won (\d+) BAFTA', expand=True)
movie['BaftaAwards_Nominations']= movie['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True)
movie['OscarAwards_Won']= movie['Awards'].str.extract('Won (\d+) Oscar', expand=True)
movie['OscarAwards_Nominations']= movie['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True)
movie['GoldenGlobeAwards_Won']= movie['Awards'].str.extract('Won (\d+) Golden Globe', expand=True)
movie['GoldenGlobeAwards_Nominations']= movie['Awards'].str.extract('Nominated for (\d+) Golden Globe', expand=True)
print(movie.head())


# In[28]:

#keeping only the columns needed for the result
df_1=movie[[15,21,22,23,24,25,26,27,28,29,30]]


# In[29]:

result = df_1.fillna(0)
result


# In[31]:

#converting pandas objects to int
result['Awards_Won'] = result['Awards_Won'].astype(str).astype(int)
result['PrimeAwards_Won'] = result['PrimeAwards_Won'].astype(str).astype(int)
result['BaftaAwards_Won']=result['BaftaAwards_Won'].astype(str).astype(int) 
result['OscarAwards_Won']=result['OscarAwards_Won'].astype(str).astype(int) 
result['GoldenGlobeAwards_Won']=result['GoldenGlobeAwards_Won'].astype(str).astype(int)


# In[32]:

result['Awards_Nominated'] =result['Awards_Nominated'].astype(str).astype(int) 
result['PrimeAwards_Nominations']=result['PrimeAwards_Nominations'].astype(str).astype(int)
result['BaftaAwards_Nominations']=result['BaftaAwards_Nominations'].astype(str).astype(int)
result['OscarAwards_Nominations']=result['OscarAwards_Nominations'].astype(str).astype(int)  
result['GoldenGlobeAwards_Nominations']=result['GoldenGlobeAwards_Nominations'].astype(str).astype(int)


# In[33]:

#Totalling up the awards won by each movie
result['Awards_Won'] = result['Awards_Won']+result['PrimeAwards_Won']+result['BaftaAwards_Won']+result['OscarAwards_Won']+result['GoldenGlobeAwards_Won']


# In[17]:

#Calculating the no of times the movie has been nominated for awards
result['Awards_Nominated']=result['Awards_Nominated']+result['PrimeAwards_Nominations']+result['BaftaAwards_Nominations']+result['OscarAwards_Nominations']+result['GoldenGlobeAwards_Nominations']


# In[34]:

print(result.head())


# In[35]:

result.to_csv('Question4_Part1.csv')

