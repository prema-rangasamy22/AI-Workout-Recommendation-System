import streamlit as st

st.title("AI Workout Recommendation System")

# --- User Inputs ---
name = st.text_input("Enter your name")
age = st.number_input("Age", min_value=10, max_value=80)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
height = st.number_input("Height (cm)", min_value=100, max_value=250)
weight = st.number_input("Current Weight (kg)", min_value=20, max_value=200)
target_weight = st.number_input("Target Weight (kg)", min_value=20, max_value=200)

# Auto BMI calculation
if height > 0:
    bmi = weight / ((height / 100) ** 2)
else:
    bmi = 0

st.write(f"*Your BMI:* {bmi:.2f}")

goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Strength", "Endurance"])
activity = st.selectbox("Activity Level", ["Sedentary", "Moderate", "Active"])
equipment = st.multiselect("Available Equipment",
                           ["Dumbbells", "Cable Machine", "Bodyweight", "Treadmill", "Free Weights"])

# --- Generate Recommendation ---
if st.button("Generate Plan"):

    st.subheader("Recommended Workout Plan:")

    st.write("### 🔥 Warm-up")
    st.write("- Jumping Jacks (2 mins)")
    st.write("- Arm Circles (1 min)")

    st.write("### 💪 Main Workout")

    if goal == "Weight Loss":
        st.write("- Squats (3×15)")
        st.write("- Push-ups (3×12)")
        st.write("- Mountain Climbers (2 mins)")
        st.write("- Skipping (5–10 mins)")

    elif goal == "Muscle Gain":
        st.write("- Dumbbell Bench Press (4×10)")
        st.write("- Dumbbell Rows (4×12)")
        st.write("- Bicep Curls (3×12)")
        st.write("- Lunges (3×10 each leg)")

    elif goal == "Strength":
        st.write("- Deadlift (3×5)")
        st.write("- Push Press (3×5)")
        st.write("- Plank (60 sec × 3)")

    elif goal == "Endurance":
        st.write("- Slow Jogging (10 mins)")
        st.write("- Burpees (3×10)")
        st.write("- Cycling (15 mins)")

    st.write("### 🧘 Cooldown")
    st.write("- Stretching (5 mins)")

    # ---- Predictive Analysis ----
    st.subheader("Goal Achievement Prediction")

    if goal == "Weight Loss":
        weeks = abs(weight - target_weight) * 0.8
    elif goal == "Muscle Gain":
        weeks = abs(weight - target_weight) * 1.2
    else:
        weeks = 8

    st.success(f"⏳ You may achieve your goal in approximately *{int(weeks)} weeks*.")