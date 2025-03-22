from flask import Flask, request, jsonify
import random

app = Flask(__name__)

COLLEGE_DATABASE = [
    {"name": "IIT Bombay", "fees": 200000, "placement": 90, "ranking": 1, "scholarships": "Merit-based", "virtualTour": "https://iitb.ac.in"},
    {"name": "IIT Delhi", "fees": 220000, "placement": 88, "ranking": 2, "scholarships": "Need-based", "virtualTour": "https://iitd.ac.in"},
    {"name": "BITS Pilani", "fees": 350000, "placement": 85, "ranking": 5, "scholarships": "Merit & Need-based", "virtualTour": "https://bits-pilani.ac.in"},
    {"name": "NIT Trichy", "fees": 180000, "placement": 80, "ranking": 7, "scholarships": "Govt & Private", "virtualTour": "https://nitt.edu"},
    {"name": "VIT Vellore", "fees": 175000, "placement": 75, "ranking": 10, "scholarships": "Merit-based", "virtualTour": "https://vit.ac.in"}
]

def recommend_colleges():
    return random.sample(COLLEGE_DATABASE, 3)  # Randomly pick 3 colleges

@app.route("/analyze", methods=["POST"])
def analyze_marksheet():
    if "marksheet" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["marksheet"]
    file.save(f"uploads/{file.filename}")  # Save uploaded file

    recommended_colleges = recommend_colleges()

    return jsonify({"colleges": recommended_colleges})

if __name__ == "__main__":
    app.run(debug=True)
# import os
# from flask import Flask, request

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'

# # Ensure the upload folder exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/upload', methods=['POST'])
# def analyze_markSheet():
#     if 'file' not in request.files:
#         return "No file part", 400

#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file", 400

#     if file:
#         filename = file.filename
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
#         return "File uploaded successfully", 200

# if __name__ == '__main__':
#     app.run(debug=True)