A Python-based Credit Risk Scoring System with a web interface using Streamlit, SQLite database, and a machine learning model for predicting credit risk. This project is designed to demonstrate end-to-end data engineering, ML, and web deployment skills.

Table of Contents

Project Overview

Features

Technology Stack

Data Model

Architecture

Installation

Usage

Screenshots

Future Enhancements

License

Project Overview

The Credit Risk Scoring System allows financial institutions or simulated users to assess an applicant’s creditworthiness. The system uses historical applicant data and derived financial features to predict the probability of default and make approved/declined decisions.

The system also provides explainable outputs, highlighting why an applicant is considered high-risk.

Features

Applicant Input Form via Streamlit Web UI

Credit Risk Prediction using a trained ML model (Logistic Regression)

Risk Level Classification: Low, Medium, High

Automated Credit Decision: Approved / Declined

Database Storage: SQLite for applicants and decisions

Audit Trail: Timestamped applicant and decision records

Explainable AI Module: Flags potential risk factors in plain English

Technology Stack
Layer	Tools / Libraries
Web UI	Streamlit
Backend / ML	Python, Scikit-learn, NumPy, Pandas
Database	SQLite
Model Persistence	joblib
Environment Management	Python Virtual Environment (venv)
Data Model

The system has two main tables:

Applicants
Stores applicant details and derived financial features.

Credit Decisions
Stores model predictions, risk levels, and final decisions.

Relationship: One-to-Many (One applicant → multiple decisions).

Application Architecture

Layers & Flow:

Streamlit Web UI: Collects user inputs

ML Model & Decision Engine: Predicts risk and applies business rules

SQLite Database: Stores applicants and decisions

Reporting & Audit: Optionally view logs or analytics dashboard

Installation

Clone repository

git clone https://github.com/yourusername/credit-risk-scoring.git
cd credit-risk-scoring


Create a virtual environment

python -m venv venv


Activate the environment

venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux


Install dependencies

pip install -r requirements.txt


Create the database

python create_db.py


Run the app

python -m streamlit run credit_app.py

Usage

Open the browser when Streamlit launches (http://localhost:8501)

Fill in the applicant details

Submit to see risk probability, risk level, and credit decision

The system stores applicant and decision in the database for auditing

Screenshots

(Replace with actual screenshots of your app)

Web UI form

Credit decision results

AI explanations

Future Enhancements

SHAP-based explainable AI plots

Admin dashboard for viewing all applicants and decisions

Integration with Power BI for analytics

Docker container for deployment

Cloud deployment (AWS, Azure)

License

This project is licensed under the MIT License – see the LICENSE
 file for details.
