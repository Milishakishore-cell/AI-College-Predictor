from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("college_predictor_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from the request
        input_data = request.json
        print("Received input data:", input_data)  # Log input data

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

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

        # Return the prediction as JSON
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        print("Error:", str(e))  # Log the error
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)