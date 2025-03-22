from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample college dataset
college_data = {
    "IIT Delhi": {"fees": 2.5, "placement": 90, "ranking": 1},
    "IIT Bombay": {"fees": 2.3, "placement": 92, "ranking": 2},
    "NIT Trichy": {"fees": 1.5, "placement": 85, "ranking": 6},
    "BITS Pilani": {"fees": 4.5, "placement": 88, "ranking": 5},
    "Delhi University": {"fees": 0.5, "placement": 75, "ranking": 10}
}

@app.route('/compare', methods=['POST'])
def compare_colleges():
    data = request.json
    college1 = data.get("college1")
    college2 = data.get("college2")

    if college1 not in college_data or college2 not in college_data:
        return jsonify({"error": "One or both colleges not found"}), 400

    return jsonify({
        "college1": {"name": college1, **college_data[college1]},
        "college2": {"name": college2, **college_data[college2]}
    })

if __name__ == '__main__':
    app.run(debug=True)
