# TekFriday Development Assignment – Yash Gaikwad

This repository contains my completed assignment for the **Development Role** at TekFriday.

---

## 🔍 Assignment Overview

### Part A – Loan Terms Chatbot (Streamlit)
A Streamlit-based chatbot that:
- Greets the user
- Accepts natural language questions
- Responds using 50+ predefined loan-related FAQs
- Cleans input (case, punctuation, spacing) for accurate matching

### Part B – Loan Risk Calculator
- Calculates a risk score using the formula:  
  `(missed_repayments * 2) + (loan_amount / collateral_value) + (interest / 2)`
- Classifies loans as `LOW`, `MEDIUM`, or `HIGH` risk
- Adds `risk_score` and `risk_level` columns

### Part C – EMI Risk Tagging
- Automates tagging using `.apply()` across the dataset
- Applies business logic to add `risk_level` for each loan

### Loan Repayment Analysis
- Merged `repayment_base.csv` with loan data
- Calculated total repaid amount, repayment ratio
- Flagged loans where <75% was repaid as `is_partially_repaid`

---
