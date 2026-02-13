# 📊 Customer Churn Prediction App
## 📌 Problem Statement

The goal of this project is to predict whether a telecom customer will churn based on demographic details and service usage data.

Customer churn prediction helps telecom companies identify customers who are likely to leave and take proactive retention measures.

---
## 🎯 Objective

* Build classification models to predict churn

* Compare model performance

* Deploy the best model using Streamlit

---
## 🗂️ Dataset

 **Dataset used: Telco Customer Churn Dataset**

 It contains 7,043 customer records with features such as:

* Gender

* Senior Citizen status

* Tenure

* Internet Service

* Contract type

* Monthly Charges

* Payment Method

* Churn status

---
## 🛠️ Technologies Used

* Python

* Pandas

* NumPy

* Scikit-learn

* Streamlit

* Matplotlib / Seaborn

* Pickle

---
## ⚙️ Project Workflow

* Data Loading

* Data Cleaning

* Handling Missing Values

* Feature Encoding

* Train-Test Split

* Model Training

* Model Evaluation

* Pipeline Creation

* Deployment using Streamlit

---
## 🤖 Models Trained

|       Model         |  Accuracy |
| ------------------- | ---------- |
| Logistic Regression |   82.04%   |
| Random Forest       |   79.35%   |


 **✅ Best Model: Logistic Regression**

---
## 📈 Evaluation Metrics

* Accuracy Score

* Confusion Matrix

* Classification Report

---
## 🚀 Deployment

The final model is deployed using Streamlit.

### Run Locally
```
streamlit run app.py
```

---
## 📂 Project Structure
```
customer-churn-app/
│
├── app.py                  # Streamlit UI
├── churn_pipeline.pkl      # Saved ML pipeline
├── customer_churn_notebook.ipynb
├── requirements.txt
├── README.md
└── data/
```

---
## 🧠 Key Insights

* Customers with month-to-month contracts churn more

* Higher monthly charges increase churn risk

* Low tenure customers are more likely to churn

* Lack of tech support/security impacts retention

---
## 🔮 Future Improvements

* Hyperparameter tuning

* ROC-AUC optimization

* SHAP explainability

* Cloud deployment

* Real-time database integration

---
## 👩‍💻 Author

**Nivedita Shill**

Machine Learning Project

---
## Dataset Link:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn
