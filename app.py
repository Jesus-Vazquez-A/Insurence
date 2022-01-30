# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:06:25 2022

@author: amado
"""

import pandas as pd
import numpy as np
import joblib
import streamlit as st
from PIL import Image




st.write("""
         
         # Predicted insurence
         ##### By Amado de Jesús Vázquez Acuña
         
         """
         
         )

img=Image.open("medico-640x360.jpg")

st.image(img)

sex_button=st.selectbox('Sex',('Male','Female'))


smoker_button=st.selectbox('Smoker',('Yes','No'))



region_button=st.selectbox('Region',
                           ('northwest', 'southeast', 
                            'southwest', 'northeast'))


def user_input():
    
    age=st.sidebar.slider(label='Age',
                          min_value=18,
                          max_value=100,
                          step=1),
    
    bmi=st.sidebar.slider(label='BMI',min_value=18.0,
                          max_value=54.0,step=0.01),
    
    children=st.sidebar.slider(label='Children',
                               min_value=0,max_value=5,step=1),
    
    features={'Age':age,
              'Sex':sex_button,'BMI':bmi,
              'Children':children,
              'Smoker':smoker_button,'Region':region_button}
    
    
    return pd.DataFrame(features)


data=user_input()




st.write(data)

data['Sex']=np.where(data['Sex']=='Male',1,0)
data['Smoker']=np.where(data['Smoker']=='Yes',1,0)


if region_button=='northwest':
    
    data['nortwest']=1
    data['southeast']=0
    data['southwest']=0
    
    
    
elif region_button=='southeast':
    
    data['nortwest']=0
    data['southeast']=1
    data['southwest']=0
    
   

  
elif region_button=='southwest':
    
    data['nortwest']=0
    data['southeast']=0
    data['southwest']=1
    
    
else:
    
    data['southwest']=0
    data['southeast']=0
    data['northwest']=0






    
model=joblib.load("insurence_model.pkl")    

data=data.drop(['Region'],axis='columns')




if st.button(label='Predicted'):
    
    pred=model.predict(data)
   
    
    
    st.write(pred)
    
