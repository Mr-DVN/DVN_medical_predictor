🫀 Heart Failure Prediction using Machine Learning

This project predicts the likelihood of a heart failure event based on clinical data. It combines exploratory data analysis, machine learning, and a user-friendly web application built with Flask.

🔍 Problem Statement
Cardiovascular diseases are a leading cause of death globally. Early prediction of heart failure can save lives. This project aims to build a predictive model using patient health records and deploy it as a web application to help in early diagnosis.


📁 Dataset
Dataset name: heart_failure_clinical_records_dataset.csv

Source: Provided as part of the project

Shape: 299 rows × 13 features + 1 target

Features include:

Demographics: age, sex

Clinical factors: ejection_fraction, serum_creatinine, serum_sodium, etc.

Binary indicators: diabetes, smoking, high_blood_pressure, anaemia

Target: DEATH_EVENT (0 = survived, 1 = death)


🧪 ML Models Used
Logistic Regression

Random Forest Classifier


🏆 Final Model: Random Forest
🎯 Accuracy: ~85% on test set


🧠 Machine Learning Workflow
Data preprocessing (scaling, missing values)

Exploratory Data Analysis (EDA)

Feature scaling using StandardScaler

Model training & evaluation (classification report, confusion matrix)

Model serialization using joblib

Deployment using Flask


💻 Google Colab Notebook
All model training and export was performed in Google Colab.

Filename: model_training.ipynb

Exports:

model.pkl (trained model)

scaler.pkl (preprocessing scaler)


🌐 Web App – Flask
The web app allows users to enter clinical data and predict the risk of heart failure.

Built using:

Flask (Python)

HTML/CSS (Bootstrap-inspired custom design)

Live Demo (optional if hosted on Replit/GitHub Pages):

🔗 https://your-replit-link.repl.co/

📸 Screenshot
Include a screenshot of the working Flask app interface here:



🗂 Project Structure
project/
│
├── model_training.ipynb ← Google Colab notebook
├── model.pkl ← Trained Random Forest model
├── scaler.pkl ← Scaler used for preprocessing
├── app.py ← Flask backend
├── templates/
│ └── index.html ← Frontend form for prediction
├── static/ (optional) ← Custom CSS or image assets
└── README.md ← Project documentation



🚀 How to Run the Web App (Replit or Local)
Upload model.pkl and scaler.pkl to your working directory

Make sure templates/index.html exists

Run:

bash
Copy
Edit
python app.py
Open browser at: http://127.0.0.1:5000/

✅ Or use Replit (recommended for online users)

✅ Requirements
Install with:

pip install -r requirements.txt

Minimal libraries:

Flask

scikit-learn

joblib

numpy

pandas

📚 Learnings & Highlights
Real-world data cleaning & preprocessing

Model evaluation & comparison

Web deployment using Flask & Replit

Interpreting health data features and their impact

The HTML Showcase:
<img width="463" height="992" alt="Screenshot 2025-07-22 180757" src="https://github.com/user-attachments/assets/1bbe5dcb-a236-4c29-8be1-452ae8556b2d" />

The Final product RUN:
<img width="436" height="956" alt="Screenshot 2025-07-22 181230" src="https://github.com/user-attachments/assets/3ff6ca83-4cc4-497e-9a47-d9961d9b472c" />


🧑‍🎓 Author
👨‍💻 Name: Devanshu Nishibkar

🔗 GitHub: Mr-DVN
