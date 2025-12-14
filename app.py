from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("osteoporosis_trained_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    result = None

    if request.method == "POST":
        data = {
            "Age": int(request.form["Age"]),
            "Gender": "Male" if request.form["Gender"] == "0" else "Female",
            "Hormone": "Normal" if request.form["Hormone"] == "1" else "Low",
            "FHistory": "Yes" if request.form["FHistory"] == "1" else "No",
            "Race": "Asian",
            "Weight": "Underweight" if request.form["Weight"] == "1" else "Normal",
            "CalciumIn": "Adequate" if request.form["CalciumIn"] == "1" else "Low",
            "Activity": "Active" if request.form["Activity"] == "2" else "Sedentary",
            "Smoking": "Yes" if request.form["Smoking"] == "1" else "No",
            "MedCondition": "None",
            "Medications": "None",
            "Fractures": "Yes" if request.form["Fractures"] == "1" else "No"
        }

        df = pd.DataFrame([data])
        pred = model.predict(df)[0]
        result = "Osteoporosis Detected" if pred == 1 else "No Osteoporosis"

    return render_template("Prediction.html", result=result)

@app.route("/accuracy")
def accuracy():
    return render_template("accuracy.html")

@app.route("/ourteam")
def ourteam():
    return render_template("ourteam.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
