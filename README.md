## 🏦 Bank Loan Approval Data Exploration

### team byte bankers 

An interactive data analytics project that explores loan application patterns, approval outcomes, applicant profiles, credit scores, and financial indicators using Python and Streamlit.

## 📌 Project Overview

The project analyses loan applicant data to understand the factors associated with loan approval and rejection. It uses data cleaning, exploratory data analysis (EDA), and interactive visualizations to identify patterns in applicant profiles.

## 🎯 Project Objectives

- Analyse loan approval and rejection patterns.
- Explore the relationship between CIBIL scores and loan status.
- Study applicant income and loan amounts.
- Compare loan outcomes by education and employment status.
- Present insights through an interactive dashboard.

## 📊 Dataset

**Primary dataset:** Loan Approval Dataset

The dataset contains 4,269 applicant records and includes:

- Number of dependents
- Education and employment status
- Annual income
- Loan amount and loan term
- CIBIL score
- Residential and commercial assets
- Loan approval status

*Note: This is a sample loan application dataset. It is not verified as official RBI data or nationally representative Indian banking data.*

## 🛠️ Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Plotly
- Streamlit
- Google Colab
- GitHub

## 📈 Key Analysis

1. Loan Approval vs Rejection
2. CIBIL Score Analysis
3. Annual Income vs Loan Amount
4. Education-wise Loan Status
5. Employment-wise Loan Status

## 🌐 Live Dashboard

[Open Byte Bankers Loan Analysis Dashboard](https://bank-loan-approval-data-exploration.streamlit.app/)

## 👥 Team Members

1. Aryan Gole
2. Shreya Saxena
3. Abhinav
4. Shahajad Ahmad
5. Ashu Gangwar
6. Farman Saifi
7. Saksham Chauhan
8. Dev Dutt
9. Shivam
10. Sajal Sharma

## 📁 Project Structure

```text
Bank-Loan-Approval-Data-Exploration/
│
├── dashboard/
│   └── app.py
├── data/
│   └── india/
│       ├── cleaned_loan_dataset.csv
│       └── cleaned_secondary_dataset.csv
├── notebooks/
├── presentation/
├── reports/
├── src/
├── visuals/
├── requirements.txt
└── README.md
```

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## 🎓 Project Purpose

Developed as an academic data exploration project by Team Byte Bankers to demonstrate practical skills in data analytics, visualization, and dashboard development.
