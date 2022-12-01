#!/usr/bin/env python
# coding: utf-8

# In[79]:


#NOTE FOR PROFESSOR WEINSTEIN:
#As you knew, I was excused from class on 11/10 due to me being sick with the flu/pneumonia so it meant that
#I missed the class where you taught merges and groupby aggregations so my application of it in the project
#may be weaker or subpar compared to others around me. The only reference tools that I could use were the
#Powerpoint as well as in-class code provided to me by Brianna. I'd like to ask to keep an open mind with
#my application of both because of that. I still attempted it and tried to apply it the best I could given
#the tools that I had. I really did try my best.


# In[80]:


#References for Coding (if any):
#Powerpoints
#Class 12 In-Class Code (Thanks Brianna)
#https://medium.com/mlpoint/matplotlib-for-machine-learning-6b5fcd4fbbc7
#https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
#https://pythonspot.com/matplotlib-bar-chart/


# In[81]:


#Reading in original CSV

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import cm
import math

spreadsheet = pd.read_csv(r"C:\Users\Ky-long-PC\Desktop\VCU Stuff\Senior Year\Fall 2022\Advanced Programming\Data Science Project\Data Science Jobs Salaries.csv")


# In[82]:


#Visualization 1

import plotly.express as px
fig = px.bar(spreadsheet, x = "company_location", y = "salary_in_usd")
fig.show()


# In[83]:


#Visualization 2

import plotly.express as px
fig = px.histogram(spreadsheet, x = "job_title", y = "salary_in_usd") 
fig.show()


# In[84]:


#Visualization 3

import plotly.express as px
fig = px.pie(spreadsheet, values = "salary_in_usd", names = "remote_ratio") 
fig.show()


# In[85]:


#Visualization 4

import plotly.express as px
fig = px.bar(spreadsheet, x = "employment_type", y = "salary_in_usd") 
fig.show()


# In[86]:


#Visualization 5

import plotly.express as px
fig = px.bar(spreadsheet, x = "experience_level", y = "salary_in_usd") 
fig.show()


# In[87]:


#Visualization 6

import plotly.express as px
fig = px.bar(spreadsheet, x = "company_size", y = "salary_in_usd") 
fig.show()


# In[88]:


#Data Merge 
#Method: Inner Join
#Why: Not only because it's the most common one but it'll ensure that all data within my dataframes will be appropriately matched together

#NOTE: Due to merge arrays being required to be the same length, any and all instances of 'Not Applicable' are simply placeholders and can be disregarded

left = pd.DataFrame(
    {
        "job_title": ["Data Scientist", "Applied Machine Learning Scientist", "Finance Data Analyst", "Principal Data Engineer", "Product Data Analyst", "Computer Vision Engineer", "Principal Data Scientist", "Business Data Analyst", "Data Science Manager", "Staff Data Scientist", "Big Data Engineer", "Data Architect", "Lead Data Scientist", "Big Data Architect", "Principal Data Analyst", "Cloud Data Engineer", "Financial Data Analyst", "Computer Vision Software Engineer", "Director of Data Engineering", "Lead Data Engineer", "Marketing Data Analyst", "Machine Learning Infrastructure Engineer", "Machine Learning Scientist", "BI Data Analyst", "Lead Data Analyst", "Data Analytics Engineer", "Director of Data Science", "Applied Data Scientist", "ML Engineer", "3D Computer Vision Researcher", "AI Scientist", "Data Engineering Manager", "Manager Data Science", "Data Science Engineer", "Data Engineer", "Data Analyst", "Research Scientist", "Data Analytics Manager", "Machine Learning Engineer", "Head of Data", "Head of Data Science", "Data Scientist", "Data Science Consultant"],
        "experience_level": ["EN", "MI", "SE", "EX", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable"],
    }
)

right = pd.DataFrame(
    {
        "employment_type": ["PT", "FT", "CT", "FL", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable"],
        "company_location": ["AE", "AS", "AT", "BE", "BR", "CA", "CH", "CL", "CN", "CO", "DE", "DK", "ES", "FR", "GB", "GR", "HR", "HU", "IL", "IN", "IR", "IT", "JP", "KE", "LU", "MD", "MT", "MX", "NG", "NL", "NZ", "PK", "PL", "PT", "RU", "SG", "SI", "TR", "UA", "US", "VN", "Not Applicable", "Not Applicable"],
    }
)

result = pd.merge(left, right, how = "inner", left_on = ["job_title", "experience_level"], right_on = ["employment_type", "company_location"])


# In[89]:


#Groupby Aggregation 1

#NOTE 1: Values in salariesUSD is pulled from the dataset with respect to company_location
#NOTE 2: Due to the arrays being required to be the same length, any and all instances of 'Not Applicable'/0s beyond 'VN' and the last value for 'US' are simply placeholders and can be disregarded
#NOTE 3: Due to the amount of characters and brackets, I only coded/shown the first 3 brackets. The full groupby would have 108 brackets and for 108 values per bracket.

#Fun fact: If I did copy and paste all of the values, it can freeze Jupyter. Also, I did this all by hand. I maybe have carpal tunnel now.

salariesUSD_sum = [[115000,18102,74130,89402,13000,127543,5898,40798,100000,21844,64369,89402,47681,46759,83000,47899,45618,35735,119353,5423,4000,21669,260000,9272,59601,18000,28608,33511,50000,42000,125000,8000,154963,50180,85000,89514,25032,13105,13400,68428,4000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,61985,0,19052,75966,0,0,43331,0,79866,28850,79833,59601,103750,40529,0,0,0,30509,0,0,41689,0,62726,0,0,2876,10000,70329,0,12000,28801,61270,230000,0,0,21843,0,125000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,91237,0,0,54376,0,0,0,0,77481,45896,55000,53641,114125,0,0,0,0,29831,0,0,74000,0,0,0,0,0,0,45773,0,0,47129,0,0,0,0,30337,0,120000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
df = pd.DataFrame(salariesUSD_sum, columns = ["AE", "AS", "AT", "BE", "BR", "CA", "CH", "CL", "CN", "CO", "DE", "DK", "ES", "FR", "GB", "GR", "HR", "HU", "IL", "IN", "IR", "IT", "JP", "KE", "LU", "MD", "MT", "MX", "NG", "NL", "NZ", "PK", "PL", "PT", "RU", "SG", "SI", "TR", "UA", "US", "VN", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable"])

df.groupby(by = ["US"]).sum()


# In[90]:


#Groupby Aggregation 2

#NOTE 1: Values in salariesUSD is pulled from the dataset with respect to company_location
#NOTE 2: Due to the arrays being required to be the same length, any and all instances of 'Not Applicable'/0s beyond 'VN' and the last value for 'US' are simply placeholders and can be disregarded
#NOTE 3: Due to the amount of characters and brackets, I only coded/shown the first 3 brackets. The full groupby would have 108 brackets and for 108 values per bracket.

#Fun fact: If I did copy and paste all of the values, it can freeze Jupyter. Also, I did this all by hand. I maybe have carpal tunnel now.

salariesUSD_avg = [[115000,18102,74130,89402,13000,127543,5898,40798,100000,21844,64369,89402,47681,46759,83000,47899,45618,35735,119353,5423,4000,21669,260000,9272,59601,18000,28608,33511,50000,42000,125000,8000,154963,50180,85000,89514,25032,13105,13400,68428,4000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,61985,0,19052,75966,0,0,43331,0,79866,28850,79833,59601,103750,40529,0,0,0,30509,0,0,41689,0,62726,0,0,2876,10000,70329,0,12000,28801,61270,230000,0,0,21843,0,125000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,91237,0,0,54376,0,0,0,0,77481,45896,55000,53641,114125,0,0,0,0,29831,0,0,74000,0,0,0,0,0,0,45773,0,0,47129,0,0,0,0,30337,0,120000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
df = pd.DataFrame(salariesUSD_avg, columns = ["AE", "AS", "AT", "BE", "BR", "CA", "CH", "CL", "CN", "CO", "DE", "DK", "ES", "FR", "GB", "GR", "HR", "HU", "IL", "IN", "IR", "IT", "JP", "KE", "LU", "MD", "MT", "MX", "NG", "NL", "NZ", "PK", "PL", "PT", "RU", "SG", "SI", "TR", "UA", "US", "VN", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable", "Not Applicable", "Not Applicable","Not Applicable", "Not Applicable","Not Applicable", "Not Applicable"])

df.groupby(by = ["US"]).mean()


# In[91]:


#Machine Learning Model 1: Total Composition of Employment Types in the US (2021)

#NOTE: For easier visualization, this model will focus on the US in 2021 only

#MODEL METRICS:
#Employment Type: Part-Time, Full-Time, Contract, Freelance

labels = "Part-Time", "Full-Time", "Contract", "Freelance"
sizes = [2, 73, 3, 1]
explode = (0, 0.1, 0, 0)

model1, ax1 = plt.subplots(figsize = (20, 19))
ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%', shadow = False, startangle = 90)
ax1.axis('equal')

plt.show()


# In[92]:


#Machine Learning Model 2: Total Average Salary by Employment Type in the US

#MODEL METRICS
#Employment Type: Part-Time, Full-Time, Contract, Freelance
#Salary (Average Salary is precalculated outside of the code)

objects = ("Part-Time", "Full-Time", "Contract", "Freelance")
y_pos = np.arange(len(objects))
avg_salary = [12000, 145258, 263667, 20000]

plt.bar(y_pos, avg_salary, align = 'center', alpha = 0.5)
plt.xticks(y_pos, objects)
plt.xlabel("Employment Type")
plt.ylabel("Average Salary ($)")
plt.title("Total Average Salary by Employment Type")

plt.show()


# In[ ]:




