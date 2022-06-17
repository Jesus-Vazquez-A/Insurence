# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 14:22:52 2022

@author: PC SWAN PLUS
"""

import pandas as pd
import streamlit as st
import joblib


st.write(""" # Predicted Insurence Price """)
st.write(""" ### Author Amado de Jesus Vazquez Acuña """)


class Preprocessing_OHE():
    
    def __init__(self,new_data):
        self.new_data=new_data
    
    
    def binary(self):
        
        self.new_data["Sex"]=self.new_data["Sex"].apply(lambda x: 1 if x == "male"  else 0)
        self.new_data["Smoker"]=self.new_data["Smoker"].apply(lambda x: 1 if x == "yes"  else 0)
        
        return self.new_data
    
    def multinomial(self):
        
        
        self.new_data["Region_southeast"]=self.new_data["Region"].apply(lambda x: 1 if x == "southeast" else 0)
        
        self.new_data["Region_northeast"]=self.new_data["Region"].apply(lambda x: 1 if x == "northeast" else 0)
        
        self.new_data["Region_southwest"]=self.new_data["Region"].apply(lambda x: 1 if x == "southwest" else 0)
        
        self.new_data["Region_northwest"]=self.new_data["Region"].apply(lambda x: 1 if x == "northwest" else 0)
        
        
        return   self.new_data.drop(["Region"],axis="columns")
    
        


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


def preprocess(new_data):
    
    ohe_preproccesing=Preprocessing_OHE(new_data)

    new_data=ohe_preproccesing.binary()
    new_data=ohe_preproccesing.multinomial()
    
    return new_data
    

def predict(new_data):
    
    model=joblib.load("xgb_insurence.pkl") 
    
    return  model.predict(new_data)
    

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

if __name__ == "__main__":
    
    main()

