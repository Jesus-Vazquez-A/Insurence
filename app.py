#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import streamlit as st
import numpy as np
import warnings


# In[2]:


warnings.filterwarnings("ignore")


# In[3]:


old_df=pd.read_csv("insurence_clear")
old_df=old_df.drop(["Unnamed: 0"],axis="columns")


# In[4]:


old_df.columns=["Age","Sex","BMI","Children","Smoker","Region","Charges"]


# In[6]:


st.write(""" # Predicted insurence price """)


# In[7]:


def input_data():
    
    age=st.sidebar.slider(label="Age",min_value=18,max_value=90,step=1),
    
    sex=st.selectbox("Sex",("Male","Female")),
    
    bmi=st.sidebar.slider(label="BMI",min_value=18,max_value=60,step=1),
    
    children=st.sidebar.slider(label="Children",min_value=0,max_value=6,step=1),
    
    smoker=st.selectbox("Smoker",("Yes","No")),
    
    region=st.selectbox("Region",('southeast', 'northeast', 'southwest', 'northwest'))
  
    return age,sex,bmi,children,smoker,region


# In[31]:


def create_dataframe():
    
    age,sex,bmi,children,smoker,region=input_data()
    
    features_dict={"Age":age,"Sex":sex,
                   "BMI":bmi,"Children":children,
                   "Smoker":smoker,"Region":region}
    
    new_data=pd.DataFrame(features_dict)
    
    return new_data


# In[32]:


def ohe(new_data):
    
    new_data["Sex"]=new_data["Sex"].apply(lambda x: 1 if x =="Male" else 0)
    
    new_data["Smoker"]=new_data["Smoker"].apply(lambda x: 1 if x =="Yes" else 0)
    
    new_data["Region_southeast"]=new_data["Region"].apply(lambda x: 1 if x == "southeast" else 0)
    
    new_data["Region_northeast"]=new_data["Region"].apply(lambda x: 1 if x == "northeast" else 0)
    
    new_data["Region_southwest"]=new_data["Region"].apply(lambda x: 1 if x == "southwest" else 0)
    
    new_data["Region_northwest"]=new_data["Region"].apply(lambda x: 1 if x == "northwest" else 0)
    
    
    
    new_data=new_data.drop(["Region"],axis="columns")
    
    return new_data


# In[33]:


def rescale(new_data,old_data):
    
    return (new_data)-(np.min(old_data))/ (np.max(old_data))-(np.min(old_data))


# In[34]:


def rescale_many(new_data,old_data,columns):
    
    for column in columns:
        
        new_data[column]=rescale(new_data=new_data[column],old_data=old_data[column])
    
    return  new_data


# In[36]:


def preporcess(new_data,old_data,columns):
  
    new_data=ohe(new_data=new_data)
    new_data=rescale_many(new_data=new_data,old_data=old_data,columns=columns)
    
    return new_data


# In[41]:


new_data=preporcess(new_data=create_dataframe(),old_data=old_df,columns=["BMI","Age","Children"]).values


# In[42]:


import joblib


# In[43]:


model=joblib.load("gbr_insurence.pkl")


# In[46]:


def predict(new_data):
    
    return model.predict(new_data)


# In[47]:


if st.button(label='Predicted'):
    
    pred=predict(new_data=new_data)
    
   
    
    
    st.write(pred)


