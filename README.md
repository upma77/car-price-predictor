# 🚗 Car Price Predictor

A machine learning web application that predicts the selling price of a used car based on:
- Company  
- Car Model  
- Year of Purchase  
- Kilometres Driven  
- Fuel Type  

This project uses **Linear Regression**, Flask for backend, and HTML/CSS/Bootstrap for frontend.

---

## 📌 Features

✔ Predicts used car price based on real Quikr dataset  
✔ Cleaned + preprocessed dataset  
✔ Machine Learning model trained with 92% accuracy  
✔ Flask backend with AJAX request handling  
✔ Attractive & responsive frontend UI  
✔ Deployed-ready project structure  

---

## 🧠 Machine Learning Model

The model is trained using:
- Linear Regression  
- OneHotEncoding for categorical features  
- ColumnTransformer + Pipeline  
- Train/test split tuning (best R² = **0.92**)  

Dataset cleaned:
- Removed missing values  
- Removed `"Ask For Price"` entries  
- Extracted numeric kms  
- Trimmed model names  
- Removed outliers  

Model file:  

---

## 🛠 Technologies Used

### **Frontend**
- HTML  
- CSS  
- Bootstrap  
- JavaScript (AJAX)

### **Backend**
- Python  
- Flask  
- Flask-CORS  

### **ML & Data Processing**
- Pandas  
- NumPy  
- Scikit-learn  

---
## 📁 Project Structure

```plaintext
car_price_predictor/
│
├── application.py
├── requirements.txt
├── Cleaned_Car_data.csv
├── LinearRegressionModel.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css

