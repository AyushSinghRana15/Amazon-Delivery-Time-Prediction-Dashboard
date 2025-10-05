!pip install joblib
import streamlit as st
import pandas as pd
import joblib

model_pipeline = joblib.load('model_pipeline_important.pkl')

st.title("🚀 Delivery Time Prediction Dashboard")

with st.sidebar:
    st.header("Input Features")

    Agent_Age = st.slider('Agent Age', 15, 50, 30)
    distance_km = st.number_input('Distance (km)', min_value=0.0, max_value=100.0, value=5.0)
    delivery_duration_min = st.number_input('Delivery Duration (min)', min_value=0, max_value=300, value=10)

    st.subheader("Weather")
    Weather_Sunny = st.checkbox('☀️ Sunny', value=True)
    
    st.subheader("Traffic Condition")
    Traffic_High = st.checkbox('🚦 High Traffic')

    st.subheader("Vehicle Type")
    Vehicle_van = st.checkbox('🚐 Van')

    st.subheader("Category")
    Category_Electronics = st.checkbox('📱 Electronics')

if st.button('Predict Delivery Time'):
    input_df = pd.DataFrame({
        'Agent_Age': [Agent_Age],
        'distance_km': [distance_km],
        'delivery_duration_min': [delivery_duration_min],
        'Weather_Sunny': [1 if Weather_Sunny else 0],
        'Traffic_High': [1 if Traffic_High else 0],
        'Vehicle_van': [1 if Vehicle_van else 0],
        'Category_Electronics': [1 if Category_Electronics else 0]
    })

    prediction = model_pipeline.predict(input_df)
    st.markdown(f"### ⏱️ Predicted Delivery Time: **{prediction[0]:.2f} minutes**")
