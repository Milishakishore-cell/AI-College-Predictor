import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load("college_predictor_model.pkl")

# Example input
user_input = {
    "class_10_gpa": 7.4,
    "class_12_gpa": 7.9,
    "jee_mains_rank": 4096,
    "jee_advanced_rank": 12635,
    "neet_rank": 29320,
    "sat_score": 1520,
    "extracurriculars": 2,
    "category": "General",
    "state_of_domicile": "Delhi",
    "preferred_branch": "Computer Science"
}

# Convert input to DataFrame
input_df = pd.DataFrame([user_input])

# One-hot encode categorical variables
input_df = pd.get_dummies(input_df)

# Ensure all columns are present (add missing columns with 0)
train_columns = model.feature_names_in_
for col in train_columns:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns to match training data
input_df = input_df[train_columns]

# Make a prediction
prediction = model.predict(input_df)
print(f"Predicted College: {prediction[0]}")