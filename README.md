# AI Workout Recommendation System

A simple Streamlit web application that recommends personalized workout routines and estimates the time required to reach a weight goal.  
This project is rule-based (no machine learning) and is designed for learning, portfolio use, and demonstration.

---

## 🚀 Features
- Calculates BMI based on height & weight  
- Categorizes body type (Underweight, Normal, Overweight, Obese)  
- Generates a workout plan based on the user's BMI  
- Estimates the number of weeks required to reach a target weight  
- Simple and easy-to-use Streamlit interface  

---

## 📊 BMI Formula Used
BMI is calculated using the standard formula:
BMI = weight (kg) / (height_in_meters²)
Example:  
 If height = 1.65 m and weight = 70 kg:  
 BMI = 70 / (1.65²)

---

## 🏋 Workout Recommendation Logic  
Workout suggestions are based on the BMI range:

- Underweight (BMI < 18.5)  
  - Strength training  
  - High-calorie meal plans  

- Normal Weight (BMI 18.5–24.9)  
  - Balanced workouts (strength + cardio)  
  - Maintenance routine  

- Overweight (BMI 25–29.9)  
  - More cardio  
  - Calorie-deficit diet guidance  

- Obese (BMI ≥ 30)  
  - Low-impact exercises  
  - Progressive cardio  
  - Beginner strength training  

---

## 📅 Weight Goal Estimation  
The app estimates how long it will take to reach a target weight using a simple rule:
1 kg of healthy weight change ≈ 1 week
So, if the user wants to lose 5 kg → estimated 5 weeks.  
If the user wants to gain 3 kg → estimated 3 weeks.

---

## 🛠 How to Run the Project Locally

### 1. Install Streamlit
pip install streamlit
### 2. Run the app
streamlit run app.py
The web app will open in your browser.

---

## 📂 Tech Stack
- Python
- Streamlit

---

## 📌 Note
This is a rule-based demo project created for learning, internships, and portfolio showcasing.  
It does not use machine learning.

---

## ✨ Author
Prema R  
Aspiring AI developer
