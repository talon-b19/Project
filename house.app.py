import streamlit as st
import joblib 
import numpy as np  

model = joblib.load("grid.model.tree")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learning for prediciting house price with certain features")

st.divider()

bedrooms = st.number_input("Number of Bedrooms", min_value = 0, value = 0)
bathrooms = st.number_input("Number of Bathrooms", min_value = 0, value = 0)
livingarea = st.number_input("Living Area ", min_value = 0, value = 2000)
condition = st.number_input("Condition", min_value = 0, value = 3)
numberofschools = st.number_input("Number of schools Nearby", min_value=0, value=0)

st.divider()

X = [[bedrooms,bathrooms,livingarea,condition,numberofschools]]

predictbutton = st.button("Predict")

if predictbutton:

    st.balloons()

    X_array = np.array(X)

    prediction = model.predict(X_array)

    st.write(f"Price prediction is {prediction[0]}")

else:   
    st.write("Please enter criteria and predict with button")