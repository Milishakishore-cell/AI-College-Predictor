from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Sample user database (replace with a real database in production)
users = {
    "bhoomi123": "bg1921",
    "user2": "password2"
}

# Route to serve the login page
@app.route('/')
def login_page():
    return render_template('login.html')

# Endpoint to handle login requests
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if username exists and password matches
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful!", "success": True})
    else:
        return jsonify({"message": "Invalid username or password.", "success": False}), 401

if __name__ == '__main__':
    app.run(debug=True)