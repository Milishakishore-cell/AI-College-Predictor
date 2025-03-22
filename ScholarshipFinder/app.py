from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample scholarships data
scholarships = [
    {
        "name": "National Merit Scholarship",
        "eligibility": "Class 12 Marks",
        "marks_cutoff": 90,
        "income_cutoff": 800000,
        "amount": "₹50,000",
        "deadline to apply": "30th June"
    },
    {
        "name": "JEE Rank Excellence Scholarship",
        "eligibility": "JEE Mains Rank",
        "rank_cutoff": 10000,
        "income_cutoff": 700000,
        "amount": "₹40,000",
        "deadline to apply": "15th July"
    },
    {
        "name": "Advanced Scholar Grant",
        "eligibility": "JEE Advanced Rank",
        "rank_cutoff": 5000,
        "income_cutoff": 500000,
        "amount": "₹60,000",
        "deadline to apply": "1st August"
    },
    {
        "name": "Medical Entrance Aid",
        "eligibility": "NEET Rank",
        "rank_cutoff": 5000,
        "income_cutoff": 600000,
        "amount": "₹45,000",
        "deadline to apply": "10th August"
    },
    {
        "name": "MBA Excellence Award",
        "eligibility": "CAT Percentile",
        "percentile_cutoff": 90,
        "income_cutoff": 900000,
        "amount": "₹70,000",
        "deadline to apply": "5th September"
    },
    {
        "name": "Law Entrance Support",
        "eligibility": "CLAT Rank",
        "rank_cutoff": 1000,
        "income_cutoff": 700000,
        "amount": "₹35,000",
        "deadline to apply": "20th September"
    },
    {
        "name": "SAT International Grant",
        "eligibility": "SAT Score",
        "score_cutoff": 1400,
        "income_cutoff": 900000,
        "amount": "₹80,000",
        "deadline to apply": "1st October"
    },
    {
        "name": "Global GRE Scholarship",
        "eligibility": "GRE Score",
        "score_cutoff": 320,
        "income_cutoff": 1000000,
        "amount": "₹60,000",
        "deadline to apply": "10th October"
    },
    {
        "name": "Sports Excellence Scholarship",
        "eligibility": "Sports Achievements",
        "level": "State-level",
        "amount": "₹20,000",
        "deadline to apply": "15th November"
    },
    {
        "name": "Cultural Talent Scholarship",
        "eligibility": "Arts and Culture",
        "level": "State-level",
        "amount": "₹25,000",
        "deadline to apply": "30th November"
    }
]


@app.route('/find-scholarships', methods=['POST'])
def find_scholarships():
    data = request.json

    # Extract values and ensure type conversion
    basis = data.get('basis', '')
    marks = int(data.get('marks', 0) or 0)
    rank = int(data.get('rank', 0) or 0)
    percentile = float(data.get('percentile', 0) or 0)
    score = int(data.get('score', 0) or 0)
    income = int(data.get('income', 0) or 0)
    achievements = data.get('achievements', '').lower()

    matched_scholarships = []
    for scholarship in scholarships:
        eligibility = scholarship["eligibility"]
        
        if basis == "class12" and "90%+" in eligibility and marks >= 90:
            matched_scholarships.append(scholarship)
        elif basis == "jee" and "JEE Mains" in eligibility and rank < 10000:
            matched_scholarships.append(scholarship)
        elif basis == "jee_advanced" and "JEE Advanced" in eligibility and rank < scholarship.get("rank_cutoff", float('inf')):
            matched_scholarships.append(scholarship)
        elif basis == "neet" and "NEET" in eligibility and rank < 5000:
            matched_scholarships.append(scholarship)
        elif basis == "cat" and "CAT" in eligibility and percentile > 90:
            matched_scholarships.append(scholarship)
        elif basis == "clat" and "CLAT" in eligibility and rank < 1000:
            matched_scholarships.append(scholarship)
        elif basis == "sat" and "SAT" in eligibility and score > 1400:
            matched_scholarships.append(scholarship)
        elif basis == "gre" and "GRE" in eligibility and score > 320:
            matched_scholarships.append(scholarship)
        elif basis == "sports" and "State-level sports" in eligibility and "sports" in achievements:
            matched_scholarships.append(scholarship)
        elif basis == "arts" and "State-level arts" in eligibility and "arts" in achievements:
            matched_scholarships.append(scholarship)
        elif basis == "income" and "Income-Based" in eligibility and income < scholarship.get("income_cutoff", float('inf')):
            matched_scholarships.append(scholarship)
    
    return jsonify(matched_scholarships)

if __name__ == '__main__':
    app.run(debug=True)

