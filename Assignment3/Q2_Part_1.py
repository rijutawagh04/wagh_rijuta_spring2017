
# coding: utf-8

# ## Question 2 Part 1:
# ### Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.

# In[2]:

import pandas as pd


# In[4]:

df=pd.read_csv('C:/Users/mahesh/Desktop/Data analysis spring 2017/Data_Analysis_Assignments/wagh_rijuta_spring2017/Assignment 3/Data/employee_compensation.csv')
print(df.head())


# In[5]:

#Find each department and their corresponding Organization Group
newOrganizationGroup=[]
newDepartment=[]
for index,rows in df.iterrows():
    if((rows['Department'] not in newDepartment)):
        newDepartment.append(rows['Department'])
        newOrganizationGroup.append(rows['Organization Group'])


# In[6]:

#Find the total Compensation of each Department
totalCompensation=[0]*56
j=[0]*56
for index,rows in df.iterrows():
    for i in range(1,(len(newDepartment)+1)):
        if rows['Department']==newDepartment[i-1]:
            totalCompensation[i-1]=rows['Total Compensation']+totalCompensation[i-1]
            j[i-1]+=1
    


# In[7]:

#Find mean of the total Compensation of each department
meanCompensation=[0]*56
for k in range(1,(len(j)+1)):
    meanCompensation[k-1]=totalCompensation[k-1]/j[k-1]


# In[8]:

df1=pd.DataFrame({'Organization Group':newOrganizationGroup,'Department':newDepartment,'Total Compensation':meanCompensation})
df1=df1.sort_values(by='Total Compensation',ascending=False) #Sorting values from highest to lowest
df1.head()


# In[10]:

df1.to_csv('TotalCompensation.csv', sep=';', encoding='utf-8')

