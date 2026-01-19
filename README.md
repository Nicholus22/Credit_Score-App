# 💳 Credit Risk Scoring System

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.28.1-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A Python-based **Credit Risk Scoring System** with web interface, ML model, and SQLite database. Designed to predict credit risk and provide explainable credit decisions.

---

## **Table of Contents**

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Data Model](#data-model)  
- [Architecture](#architecture)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Screenshots](#screenshots)  
- [Future Enhancements](#future-enhancements)  
- [License](#license)  

---

## **Project Overview**

This project allows financial institutions to **assess applicant creditworthiness**. Users enter applicant details, the ML model predicts default probability, applies business rules, and stores results in a **SQLite database**. The system also provides **plain-language explanations** for regulatory compliance.

---

## **Features**

- Web UI via Streamlit  
- Credit risk prediction (ML model)  
- Risk level classification (Low/Medium/High)  
- Credit decision: Approved / Declined  
- Database storage for applicants and decisions  
- Audit trail with timestamps  
- Explainable AI for decision transparency  

---

## **Technology Stack**

| Layer                  | Tool / Library                       |
|------------------------|-------------------------------------|
| Web UI                 | Streamlit                           |
| Backend / ML           | Python, scikit-learn, Pandas, NumPy |
| Database               | SQLite                              |
| Model Persistence      | joblib                               |
| Environment Management | Python virtual environment (venv)   |

---

## **Data Model**

Two main tables:

1. **Applicants** – Stores applicant info and derived features  
2. **Credit Decisions** – Stores predictions, risk levels, and final decisions  

**Relationship:** One-to-Many (One applicant → multiple decisions)  

![Data Model](./A_black_and_white_Entity-Relationship_Diagram_(ERD.png))

---

## **Application Architecture**

**Layers & Flow:**

1. Streamlit Web UI → Collects user inputs  
2. ML Model & Decision Engine → Predicts risk  
3. SQLite Database → Stores applicants and decisions  
4. Reporting & Audit → Optional dashboard  

![Architecture](./An_application_architecture_diagram_of_a_"Credit_R.png)

---

## **Installation**

1. Clone the repo:

```bash
git clone https://github.com/yourusername/credit-risk-scoring.git
cd credit-risk-scoring
