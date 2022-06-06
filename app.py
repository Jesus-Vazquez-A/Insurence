#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import joblib




# In[7]:

  
st.write(""" # Predicted insurence price """)
st.write(""" ### Author Amado de Jesus Vazquez Acuña """)

def input_data():
    
    age=st.sidebar.slider(label="Age",min_value=18,max_value=64,step=1),
    
    sex=st.selectbox("Sex",("Male","Female")),
    
    bmi=st.sidebar.slider(label="BMI",min_value=18.0,max_value=47.0,step=0.0001),
    
    children=st.sidebar.slider(label="Children",min_value=0,max_value=5,step=1),
    
    smoker=st.selectbox("Smoker",("Yes","No")),
    
    region=st.selectbox("Region",('southeast', 'northeast', 'southwest', 'northwest'))
  
    return age,sex,bmi,children,smoker,region


def create_dataframe():
    
    age,sex,bmi,children,smoker,region=input_data()
    
    features_dict={"Age":age,"Sex":sex,
                   "BMI":bmi,"Children":children,
                   "Smoker":smoker,"Region":region}
    
    new_data=pd.DataFrame(features_dict)
    
    return new_data


def old_data():
    
    # Cargamos el dataframe viejo. Para poder rescalar los nuevos datos ingresados por el usuario.
    
    old_data=pd.read_csv("insurence_clear")
    old_data=old_data.drop(["Unnamed: 0"],axis="columns")

    
    drops=['sex','smoker','region',"charges"]
    old_data=old_data.drop(drops,axis="columns")
    old_data.columns=["Age","BMI","Children"]
    
    # Sólo seleccionamos variables continuas.
    
    return old_data


old_data=old_data() # Datos viejos usados en el entrenamiento y validación del modelo.




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

## Rescalado para varaibles continuas
def rescale(new_data):
    
    min_max_scaler=MinMaxScaler()
    min_max_scaler.fit(old_data)
    new_data[["Age","BMI","Children"]]=min_max_scaler.transform(new_data[["Age","BMI","Children"]])
    
    return new_data



# In[36]:

# Preprocesamiento de los datos
def preprocess(new_data):

    new_data=ohe(new_data)
    new_data=rescale(new_data)
    
    return new_data
    

# Realizar predicciones
def predict(new_data):
    
    model=joblib.load("gbr_insurence.pkl") #  Importamos el modelo que habíamos entrenado.
    
    return  model.predict(new_data)
    


# In[41]:

def main():
    
      
    new_data=create_dataframe() # Datos nuevos

  
    st.subheader("User Input")
    st.write(new_data)
    
    
 
    
    new_data=preprocess(new_data) # Preprocesamiento de los datos
    
    st.subheader("Data preprocessing")
    st.write(new_data)

    
    # Realizamos las predicciones
    if st.button(label='Predicted'):
        
        pred=predict(new_data)
        
        
       
        
        
        st.write(" Predicted : {}".format(pred))





# In[46]:

if __name__ == '__main__':
    main()

