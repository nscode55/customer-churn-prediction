import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Saved Pipeline
# -------------------------------
model = pickle.load(open("churn_pipeline.pkl", "rb"))

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction App")
st.write(
    "Predict whether a telecom customer will churn."
)

# -------------------------------
# User Inputs
# -------------------------------

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

SeniorCitizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

Partner = st.selectbox(
    "Has Partner?",
    ["Yes", "No"]
)

Dependents = st.selectbox(
    "Has Dependents?",
    ["Yes", "No"]
)

tenure = st.slider(
    "Tenure (Months)",
    0, 72, 12
)

PhoneService = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

MultipleLines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

Contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    0.0, 200.0, 70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    0.0, 10000.0, 1000.0
)

# -------------------------------
# Prediction Button
# -------------------------------

if st.button("Predict Churn"):

    input_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # ---------------------------
    # Output
    # ---------------------------

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(
            f"⚠️ Customer is likely to CHURN\n\nProbability: {probability:.2%}"
        )
    else:
        st.success(
            f"✅ Customer is NOT likely to churn\n\nProbability: {probability:.2%}"
        )
