import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
model = joblib.load("college_predictor_model.pkl")

@app.route("/predict-college", methods=["POST"])
def predict_college():
    """
    Endpoint to handle college prediction requests.
    """
    user_input = request.json
    if not user_input:
        return jsonify({"error": "Input data is required"}), 400

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
    try:
        prediction = model.predict(input_df)
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)