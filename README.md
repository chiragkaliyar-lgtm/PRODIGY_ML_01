#  House Price Prediction using Machine Learning

A Machine Learning web application that predicts house prices based on **Living Area**, **Number of Bedrooms**, and **Number of Bathrooms** using the **Linear Regression** algorithm. The application is built with **Python**, **Scikit-learn**, and **Streamlit**.

---

##  Project Overview

This project was developed as **Task 1** for the **Machine Learning Internship at Prodigy InfoTech**.

The objective is to build a Linear Regression model capable of predicting house prices using three important features:

-  Living Area (Square Feet)
-  Number of Bedrooms
-  Number of Bathrooms

The trained model is deployed as an interactive Streamlit web application.

---

##  Features

- Predict house prices instantly
- Interactive Streamlit web application
- Clean and modern user interface
- Real-time predictions
- Download prediction report as CSV
- Responsive layout
- Machine Learning model information
- Model performance metrics

---

##  Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Linear Regression Model Training
6. Model Evaluation
7. Prediction
8. Streamlit Deployment

---

##  Dataset

**Dataset:** Kaggle House Prices Dataset

Files used:

- train.csv
- test.csv
- data_description.txt

Target Variable:

- **SalePrice**

Features Used:

- **GrLivArea**
- **BedroomAbvGr**
- **FullBath**

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

##  Model Performance

| Metric | Value |
|---------|-------|
| Algorithm | Linear Regression |
| R² Score | **0.634** |
| Features Used | 3 |
| Training Samples | 1460 |

---

##  Project Structure

```
House-Price-Prediction/
│
├── app.py
├── house_price_pred.py
├── model.pkl
├── train.csv
├── test.csv
├── data_description.txt
├── requirements.txt
├── README.md
└── screenshots/
```

---

##  Installation

Clone the repository

```bash
git clone  https://github.com/chiragkaliyar-lgtm/PRODIGY_ML_01
```

Move into the project directory

```bash
cd House-Price-Prediction
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

##  Web Application

The application allows users to enter:

- Living Area
- Number of Bedrooms
- Number of Bathrooms

After clicking **Predict House Price**, the model estimates the selling price of the property.

---

##  Screenshots

### Home Page

> Add a screenshot here

### Prediction Result

> Add a screenshot here

---

##  What I Learned

During this project, I learned:

- Data preprocessing using Pandas
- Feature selection
- Train-Test splitting
- Linear Regression
- Model evaluation using R² Score and MSE
- Building Machine Learning web applications with Streamlit
- Saving and loading models using Joblib
- Deploying Machine Learning projects

---

##  Future Improvements

- Include more house features for better accuracy
- Support multiple regression algorithms
- Improve model performance
- Deploy the application online
- Add data visualizations and analytics dashboard

---

##  Developer

**Chirag Kaliyar**

Machine Learning Intern at **Prodigy InfoTech**

GitHub: https://github.com/chiragkaliyar-lgtm

LinkedIn: https://www.linkedin.com/in/chirag-kaliyar-837650305/

---

## 📄 License

This project is developed for educational purposes as part of the **Prodigy InfoTech Machine Learning Internship**.
