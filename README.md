# Group Member
Somkamon Mettawiharee - st125881
Meta Puspa Maulida - st126320
# Project Overview
This project focuses on predicting student performance using a Machine Learning model. The goal is to provide a deployed solution where users can input student data and receive a performance prediction in real-time.

## Live Deployment Link
http://192.41.170.112:5881/

# Data Summary
The project uses the StudentsPerformance.csv dataset to predict academic outcomes.
Target Variables: The model focuses on predicting scores (Math, Reading, and Writing).
Features (Predictors):
Gender: Male/Female.
Race/Ethnicity: Categorized into Groups A through E.
Parental Level of Education: Ranging from high school to master's degrees.
Lunch: Standard or free/reduced (often used as a proxy for socio-economic status).
Test Preparation Course: Whether the student completed a prep course or not.

# Model & Technical Details
The document outlines a complete machine learning pipeline:

1. Data Cleaning: Handled missing values and encoded categorical text into numbers using One-Hot Encoding or Label Encoding.
2. Feature Scaling: Used scaler.pkl to normalize numerical data so that all features have an equal impact on the prediction.
3. The Model: A trained regression model (stored in model.pkl) that takes student attributes as input and outputs a predicted score.

# Student Performance Prediction Deployment
## Project Architecture
project/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html


## Tech Stack & Files
- **Python**: Core programming language.
- **Flask/FastAPI**: Web framework used in `app.py`.
- **Scikit-Learn**: Used for the model (`model.pkl`) and data scaling (`scaler.pkl`).
- **Docker**: Containerization using the provided `Dockerfile`.
- **Dataset**: `StudentsPerformance.csv`.

## Deployment Screenshort
<img width="422" height="307" alt="Screenshot 2026-03-20 154704" src="https://github.com/user-attachments/assets/f80574b4-b0b6-43e9-ad93-f880ab61de8a" />

