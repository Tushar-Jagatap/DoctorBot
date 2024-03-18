import streamlit as st
from Prediction import Prediction

# Set page configuration
st.set_page_config(
    page_title="Health Condition Predictors",
    page_icon=":heart:",
)

# Hide Streamlit default menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Sidebar content
st.sidebar.image("assets/side_banner.png")
st.sidebar.title("Navigation")

# Sidebar navigation
app_mode = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Alzheimer's", "Heart Disease", "Diabetes", "Breast Cancer", "Epilepsy"],
)

# About and contact information in sidebar
st.sidebar.write("""
# Disclaimer
The predictions provided by this system are for informational purposes only. Consult a healthcare professional for accurate diagnosis and advice.
""")

# Main application logic
if __name__ == "__main__":

    # Home page
    if app_mode == "Home":
        st.title("Welcome to the Health Condition Predictors")

        # Banner image
        st.image("assets/banner.png")

        # Introduction and purpose
        st.write("""
            ## About the System
            This system provides prediction tools for various health conditions including Alzheimer's disease, heart disease, diabetes, breast cancer, and epilepsy. Each predictor leverages machine learning techniques to analyze relevant data and predict the likelihood of the respective condition.

            ## Purpose of the Project
            The purpose of this project is to empower individuals to assess their risk of certain health conditions and take proactive measures for prevention or early intervention. Early detection and management are key to improving health outcomes and quality of life.
            """)

    # Prediction pages
    elif app_mode == "Alzheimer's":
        Prediction("Alzheimer's Disease")

    elif app_mode == "Heart Disease":
        Prediction("Heart Disease")

    elif app_mode == "Diabetes":
        Prediction("Diabetes")

    elif app_mode == "Breast Cancer":
        Prediction("Breast Cancer")

    elif app_mode == "Epilepsy":
        Prediction("Epilepsy")
