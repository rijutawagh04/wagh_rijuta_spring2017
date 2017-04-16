
# coding: utf-8

# In[2]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[3]:

emp = pd.read_csv("C:/Users/mahesh/Desktop/Data analysis spring 2017/Data_Analysis_Assignments/wagh_rijuta_spring2017/Assignment 3/Data/employee_compensation.csv")


# In[4]:

print(emp.head())


# In[5]:

cal = emp[emp['Year Type'] == 'Calendar']
cal


# In[6]:

cal1 = cal.groupby('Employee Identifier', sort = True).mean()
avg_sal = cal.drop(cal.columns[[0,1,2,3,4,5,6,7,8,10,11]], axis = 1)
avg_sal


# In[7]:

avg_sal = avg_sal[avg_sal['Overtime'] > 0.05 * avg_sal['Salaries']]
avg_sal


# In[8]:

fam_sal = avg_sal.groupby('Job Family')['Total Benefits','Total Compensation'].mean()
fam_sal


# # Top 5 Job families in terms of total benefits

# In[9]:

fam_sal['percent_benefits'] = fam_sal['Total Benefits']/fam_sal['Total Compensation'] * 100
final_benefits = fam_sal.sort_values(['percent_benefits'], ascending = False)
final_benefits.head()


# In[10]:

final_benefits.to_csv('Q2_part2.csv')

