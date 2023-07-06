# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 07:34:20 2023

@author: PRAKASH R
"""
    
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app= FastAPI()

Origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=Origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

class sample_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    
model = pickle.load(open('diabetes_model.sav', 'rb'))


@app.post('/mlwebapp')
def prediction(input_parameters: sample_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    Pregnancies = input_dictionary['Pregnancies']
    Glucose = input_dictionary['Glucose']
    BloodPressure = input_dictionary['BloodPressure']
    SkinThickness = input_dictionary['SkinThickness']
    Insulin = input_dictionary['Insulin']
    BMI = input_dictionary['BMI']
    DiabetesPedigreeFunction = input_dictionary['DiabetesPedigreeFunction']
    Age = input_dictionary['Age']
    
    input_list = [Pregnancies,	Glucose,	BloodPressure,	SkinThickness,	Insulin,	BMI,	DiabetesPedigreeFunction,	Age	]
    
    prediction = model.predict([input_list])
    
    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
