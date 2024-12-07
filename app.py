# Deploying our code as an app

import streamlit as st
import numpy as np
import pandas as pd
import pickle

def run_streamlit_app():
    """Create and run the Streamlit web application"""
    st.title('Bank Account Openers Classifier App')

    # Load the saved model
    try:
        with open('C:\\Users\\HP\\Documents\\STUDY\\DATA SCIENCE AND ANALYSIS - GOMYCODE\\GMC_PYTHON\\Checkpoints\\Streamlit Checkpoint 2 - Financial Inclusions in Africa\\gradient_boosting_model.pkl', 'rb') as file:
            model = pickle.load(file)    
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    # Create input fields for features
    st.header('Enter User Information')
    col1, col2 = st.columns(2)
    with col1:
        country = st.number_input('country', min_value=0.0)
        year = st.number_input('year', min_value=2024)
        unique_id = st.number_input('uniqueid', min_value=0.0)
        location_type = st.number_input('location_type', min_value=0.0)
        cellphone_access = st.number_input('cellphone_access', min_value=0.0)
        household_size = st.number_input('household_size', min_value=0.0)
    with col2:
        age_of_respondent = st.number_input('age_of_respondent', min_value=0.0)
        gender_of_respondent = st.number_input('gender_of_respondent', min_value=0.0)
        relationship_with_head = st.number_input('relationship_with_head', min_value=0.0)
        marital_status = st.number_input('marital_status', min_value=0.0)
        education_level = st.number_input('education_level', min_value=0)
        job_type = st.number_input('job_type', min_value=0)

   
    # Create feature array
    features = np.array([country, location_type, age_of_respondent, unique_id,  year,
                            gender_of_respondent, cellphone_access, relationship_with_head,
                            marital_status, education_level, job_type]).reshape(1, -1)

    if st.button('Predict'):
        # Make prediction
        prediction = model.predict(features)
        probability = model.predict_proba(features)

        # Display results
        st.header('Prediction Results')
        if prediction[0] == 1:
            st.success('High Possibility of Account Opening')
        else:
            st.error('Low Possibility of Account Opening')
        st.write(f'Account Opening Possibility: {probability[0][1]:.2%}')

if __name__ == "__main__":
    run_streamlit_app()
