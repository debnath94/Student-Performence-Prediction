# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:13:10 2023

@author: debna
"""

import streamlit as st
import numpy as np
import pickle
from pickle import load
from sklearn import tree

lr = load(open('E:/LiveProject/Student_performence_prediction/math_score.pickle', 'rb'))

st.title("[Predict The Student exem Score]")

gender = st.radio("[Select Your Gender]", ["male", "female"])

if gender == "Male":
    gender = 1
else:
    gender = 0

race_ethnicity = st.radio("[Select Your Class Group]", ["group A", "group B","group C","group D","group E"])

if race_ethnicity == "group A":
    race_ethnicity = 0
elif race_ethnicity == "group B":
    race_ethnicity = 1
elif race_ethnicity == "group C":
    race_ethnicity = 2
elif race_ethnicity == "group D":
    race_ethnicity = 3   
elif race_ethnicity == "group E":
    race_ethnicity = 4

Education_level = st.radio("[Select Your Education Level]", ["associate's degree", "bachelor's degree","high school","master's degree","some college",
                                                             "some high school"])

if Education_level == "associate's degree":
    Education_level = 0
elif Education_level == "bachelor's degree":
    Education_level = 1
elif Education_level == "high school":
     Education_level = 2  
elif Education_level == "master's degree":
    Education_level = 3
elif Education_level == "some college":
    Education_level = 4
elif Education_level == "some high school":
    Education_level = 5

lunch = st.radio("[Select Your Lunch]", ["free/reduced", "standard"])

if lunch == "free/reduced":
    lunch = 0
else:
    lunch = 1


test_preparation_course = st.radio("[Select Course prepration]", ["completed", "none"])

if test_preparation_course == "completed":
    test_preparation_course = 0
else:
    test_preparation_course = 1

reading_score = st.slider("[Your reading score]", 0,100)
writing_score = st.slider("[Your writting score]", 0,100)


if st. button("Predict"):
    query_point = np. array([gender, race_ethnicity, Education_level, lunch, test_preparation_course, reading_score, writing_score])
    query_point = query_point. reshape(1, -1)
    prediction = lr.predict(query_point)
    st.write("The predicted score is", prediction[0])








