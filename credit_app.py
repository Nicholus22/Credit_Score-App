import streamlit as st
import sqlite3
import joblib
import numpy as np

# ---------------------
# Load Model
# ---------------------
@st.cache_resource
def load_model():
    return joblib.load("credit_risk_model.pkl")

model = load_model()

# ---------------------
# Connect to Database
# ---------------------
def get_db_connection():
    conn = sqlite3.connect("credit_risk.db", check_same_thread=False)
    return conn

conn = get_db_connection()
cursor = conn.cursor()

# ---------------------
# Page Config
# ---------------------
st.set_page_config(
    page_title="Credit Risk Scoring System",
    page_icon="💳",
    layout="centered"
)

st.title("Khangwelo Credit Score App")
st.write("Loan Application")

# ---------------------
# Input Form
# ---------------------
with st.form("credit_form"):
    st.subheader("Applicant Information")
    age = st.number_input("Age", min_value=21, max_value=70, value=30)
    income = st.number_input("Monthly Income (ZAR)", min_value=3000, value=15000)
    employment = st.number_input("Employment Years", min_value=0, value=5)
    history = st.number_input("Credit History (Years)", min_value=0, value=4)
    loans = st.number_input("Existing Loans", min_value=0, value=1)
    debt = st.number_input("Total Debt (ZAR)", min_value=0, value=50000)
    late = st.number_input("Late Payments", min_value=0, value=0)
    util = st.slider("Credit Utilization", 0.0, 1.0, 0.3)
    submitted = st.form_submit_button("Access the Applicant")

# ---------------------
# Helper Functions
# ---------------------
def prepare_features():
    debt_to_income = debt / (income * 12)
    loan_per_income = loans / (income + 1)
    return np.array([[
        age, income, employment, history, loans,
        debt, late, util, debt_to_income, loan_per_income
    ]])

def risk_level(prob):
    if prob < 0.3:
        return "Low"
    elif prob < 0.6:
        return "Medium"
    else:
        return "High"

def credit_decision(prob):
    return "Approved" if prob < 0.5 else "Declined"

# ---------------------
# Prediction & Storage
# ---------------------
if submitted:
    X = prepare_features()
    probability = model.predict_proba(X)[0][1]

    level = risk_level(probability)
    decision = credit_decision(probability)

    # Store applicant
    cursor.execute("""
        INSERT INTO applicants (
            age, monthly_income, employment_years,
            credit_history_years, existing_loans,
            total_debt, late_payments,
            credit_utilization, debt_to_income
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (age, income, employment, history, loans, debt, late, util, debt / (income*12)))
    applicant_id = cursor.lastrowid

    # Store decision
    cursor.execute("""
        INSERT INTO credit_decisions (
            applicant_id, risk_probability, risk_level, decision
        ) VALUES (?, ?, ?, ?)
    """, (applicant_id, probability, level, decision))

    conn.commit()

    # ---------------------
    # Display Results
    # ---------------------
    st.divider()
    st.subheader("Application Outcome")
    if decision == "Approved":
        st.success(f"Decision: {decision}")
    else:
        st.error(f"Decision: {decision}")
    st.metric("Risk Probability", f"{probability:.2f}")
    st.metric("Risk Level", level)

    # ---------------------
    # Explainable AI
    # ---------------------
    st.subheader("Explanation")
    reasons = []
    if late >= 4:
        reasons.append("Multiple late payments detected")
    if util > 0.85:
        reasons.append("High credit utilization")
    if debt > income * 12:
        reasons.append("Debt exceeds annual income")
    if employment < 1:
        reasons.append("Short employment history")
    if reasons:
        for r in reasons:
            st.write("•", r)
    else:
        st.write("No significant risk factors detected")
