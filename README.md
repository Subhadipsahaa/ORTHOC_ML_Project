# 🦴 Osteoporosis Prediction System using Machine Learning

This project is a **Machine Learning based web application** developed to predict the risk of **osteoporosis** using patient health and lifestyle data.  
The application integrates a **Random Forest ML model** with a **Flask web framework** and is deployed on **PythonAnywhere**.

---

## 📌 Project Overview

Osteoporosis is a medical condition where bones become weak and fragile, increasing the risk of fractures.  
Early prediction can help in prevention and timely treatment.

This system allows users to:
- Enter health parameters through a web interface
- Predict whether osteoporosis is **Detected** or **Not Detected**
- View model accuracy and project information

---

## 🧠 Machine Learning Details

- **Problem Type**: Binary Classification  
- **Algorithm Used**: Random Forest Classifier  
- **Accuracy**: ~83%  
- **Libraries Used**:
  - pandas
  - numpy
  - scikit-learn
  - joblib

The model was trained using real-world inspired patient data including:
- Age
- Gender
- Hormone level
- Calcium intake
- Physical activity
- Smoking habits
- Medical history
- Fracture history

---

## 🌐 Web Application Features

- Responsive UI using **Bootstrap 4**
- Flask-based backend
- ML model integration using `joblib`
- Mobile-friendly navigation
- Hosted on **PythonAnywhere**

---

## 📂 Project Structure
orthodic/ <br>
    │── app.py <br>
    │── requirements.txt <br>
    │── osteoporosis_trained_model.pkl <br>
    │ ├── templates/ <br>
    │ &nbsp;├── index.html<br>
    │   ├── Prediction.html<br>
    │   ├── accuracy.html<br>
    │   ├── ourteam.html <br>
    │   ├── navbar.html<br>
    │   ├── footer.html<br>
    │ ├── static/ <br>
    │   └── Assets/ <br>
    │       └── (images and icons)<br>

---

## Installation and Setup (Local Machine)

### Step 1: Clone Repository
bash
git clone <repository-url>
cd orthodic

### Step 2: Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Run Application
python app.py

___

### Open your browser and visit:
http://127.0.0.1:5000

___

### requirements.txt
Flask==3.0.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.4.2
joblib==1.4.2

___

### Deployment

The application is deployed on PythonAnywhere using:

 - Python 3.10

 - Virtual environment

 - WSGI configuration

Application URL format:

https://<username>.pythonanywhere.com

---

### Sample Input for Testing

Parameter	Value

Age	72
Gender	Female
Hormone Level	Normal
Calcium Intake	Low
Physical Activity	Low
Smoking	Yes
Fractures	Yes


### Predicted Output:

Osteoporosis Detected


---

### Academic Use

This project is suitable for:

MCA minor projects

Machine Learning coursework

Flask–ML integration demonstrations



---

### Viva Explanation (Short)

> This system predicts osteoporosis risk using a Random Forest machine learning model integrated with a Flask web application.




---

### Team

Subhadip Saha

Team Members (as shown in the application)



---

### License

This project is created for educational purposes only.

---