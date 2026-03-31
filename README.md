# 📧 Spam Email Classifier

## 📌 Project Overview
This project is a simple Machine Learning model that classifies emails as **Spam** or **Not Spam**. It uses Natural Language Processing (NLP) techniques to analyze text and predict whether an email is suspicious or safe.

---

## 🎯 Objective
The main objective of this project is to understand how machine learning can be used to detect spam messages using text data.

---

## ⚙️ Technologies Used
- Python  
- pandas  
- scikit-learn  
- TF-IDF Vectorization  
- Logistic Regression  

---

## 🧠 Working of the Model
1. **Data Collection**  
   A dataset of sample emails labeled as spam (1) or not spam (0) is used.

2. **Text Preprocessing**  
   - Convert text to lowercase  
   - Remove special characters  

3. **Feature Extraction**  
   - TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert text into numerical form  
   - Includes n-grams for better understanding of phrases  

4. **Model Training**  
   - Logistic Regression algorithm is used  
   - Data is split into training and testing sets  

5. **Prediction**  
   - Model predicts whether new emails are spam or not  

---

## 📊 Output
- Displays model accuracy  
- Predicts multiple test emails as:
  - Spam  
  - Not Spam  

---

## 🚀 How to Run
1. Install required libraries:
   ```bash
   pip install pandas scikit-learn
