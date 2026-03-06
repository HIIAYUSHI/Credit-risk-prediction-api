# Credit Risk Prediction API

A machine learning API that predicts the likelihood of credit default using financial attributes.

## Overview

Credit risk assessment is critical for financial institutions. This project builds a machine learning model and exposes it through an API for real-time prediction.

## Features

- Machine learning model for credit risk prediction
- REST API for prediction
- Lightweight and deployable system

## Tech Stack

Python  
Scikit-learn  
FastAPI  
Pandas  

## Project Structure

credit-risk-prediction-api

app.py – API endpoint  
model.pkl – trained machine learning model  
feature_names.pkl – input feature structure  
requirements.txt – dependencies  

## Example Prediction

Input:

{
 "income": 50000,
 "loan_amount": 10000,
 "credit_history": 1
}

Output:

{
 "risk": "Low"
}

## Future Improvements

- Add model explainability
- Deploy on cloud
- Add web interface