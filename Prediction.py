import time
import pandas as pd
import streamlit as st
import joblib

# Constants for Categories
ETHNICITY_CATEGORIES = ['Hisp/Latino', 'Not Hisp/Latino', 'Unknown']
IMPUTED_CATEGORIES = ['True', 'False']
PTRACCAT_CATEGORIES = ['Asian', 'Black', 'White']
PTGENDER_CATEGORIES = ['Female', 'Male']
APOE4_CATEGORIES = ['0', '1', '2']
MODEL_FILE_PATH = 'model/alzheimer_model.pkl'

CONDITIONS = {
    "AD": "Alzheimer's Disease",
    "LMCI": "Late Mild Cognitive Impairment",
    "CN": "Cognitively Normal"
}

def predict_condition(input_data):
    try:
        loaded_model = joblib.load(MODEL_FILE_PATH)
        predictions = loaded_model.predict(input_data)
        return predictions
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return

def convert_to_one_hot(selected_category, all_categories):
    return [1 if category == selected_category else 0 for category in all_categories]

def prediction_page():
    st.title("Patient Information")

    age = st.number_input("Age", min_value=0, max_value=122, step=1, value=65)
    gender = st.selectbox("Gender", ("Male", "Female"))
    education = st.number_input("Years of Education", min_value=0, value=12)

    st.write("<br>", unsafe_allow_html=True)

    st.header("Demographics")
    ethnicity = st.radio("Ethnicity", ETHNICITY_CATEGORIES)
    race_cat = st.radio("Race Category", PTRACCAT_CATEGORIES)

    st.write("<br>", unsafe_allow_html=True)

    st.header("Genetic Information")
    apoe_allele_type = st.selectbox("APOE Allele Type", APOE4_CATEGORIES)
    apoe_genotype = st.selectbox("APOE4 Genotype", ["2,2", "2,3", "2,4", "3,3", "3,4", "4,4"])
    imputed_genotype = st.radio("Imputed Genotype", IMPUTED_CATEGORIES)

    st.header("Cognitive Assessment")
    mmse = st.number_input("MMSE Score", min_value=0, max_value=30, step=1)

    predict_button = st.button("Predict")
    st.write("")

    if predict_button:
        if not all([age, education, mmse, apoe_genotype, race_cat, gender, apoe_allele_type, imputed_genotype, ethnicity]):
            st.error("Please fill in all the fields.")
            return

        st.write("Thank you for entering the patient's information.")
        progress_text = "Please wait, we're predicting your clinical condition..."
        my_bar = st.progress(0, text=progress_text)

        user_input = [age, education, mmse]
        user_input += convert_to_one_hot(ethnicity, ETHNICITY_CATEGORIES)
        user_input += convert_to_one_hot(race_cat, PTRACCAT_CATEGORIES)
        user_input += convert_to_one_hot(apoe_allele_type, APOE4_CATEGORIES)
        user_input += convert_to_one_hot(gender, PTGENDER_CATEGORIES)
        user_input += convert_to_one_hot(imputed_genotype, IMPUTED_CATEGORIES)
        user_input += convert_to_one_hot(apoe_genotype, ["2,2", "2,3", "2,4", "3,3", "3,4", "4,4"])

        data = pd.DataFrame([user_input])
        predicted_condition = predict_condition(data)

        st.write("")
        st.write("")
        st.subheader("Predicted Clinical Condition:")
        st.write(f"**{predicted_condition[0]}** ({CONDITIONS[predicted_condition[0]]})")
        st.subheader("Condition Description:")
        # Add description here if available
