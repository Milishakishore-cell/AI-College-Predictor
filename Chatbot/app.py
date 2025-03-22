import speech_recognition as sr
import pyttsx3
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize text-to-speech engine


# Predefined responses
responses = {
    "hello": "Hello! Welcome to the AI College Predictor. How can I assist you today?",
    "hi": "Hi there! How can I help you with your college search or admissions?",
    "admission": "You can check your admission chances by providing your academic scores, entrance exam results, and preferred colleges.",
    "scholarship": "We offer a Scholarship Finder tool to help you discover scholarships based on your academic performance, financial need, and other criteria. Would you like to explore scholarships?",
    "placement": "Our platform provides detailed insights into college placement records, top recruiters, and average salary packages. Would you like to know more about a specific college's placements?",
    "compare": "You can compare colleges side-by-side based on factors like fees, placements, infrastructure, and faculty. Please provide the names of the colleges you'd like to compare.",
    "cutoff": "You can check the previous year's cutoff scores for various colleges and courses. Please specify the college and course you're interested in.",
    "eligibility": "Eligibility criteria vary by college and course. Please provide the name of the college and course you're interested in, and I'll give you the details.",
    "courses": "We provide information on various courses offered by colleges. Please specify the field of study or college you're interested in.",
    "fees": "You can get detailed fee structures for different colleges and courses. Please provide the name of the college and course you're interested in.",
    "rank": "You can check the ranking of colleges based on various parameters like academics, placements, and infrastructure. Would you like to know the ranking for a specific field of study?",
    "application": "The application process varies by college. Please specify the college you're interested in, and I'll guide you through the application steps.",
    "deadline": "Application deadlines vary by college and course. Please provide the name of the college and course you're interested in, and I'll give you the deadline details.",
    "thanks": "You're welcome! If you have more questions, feel free to ask.",
    "bye": "Goodbye! Have a great day, and good luck with your college search!",
    "default": "I'm not sure about that. Try asking about admissions, scholarships, placements, or comparing colleges."
}
def initialize_engine():
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Set speech rate
        return engine
    except Exception as e:
        print(f"Error initializing pyttsx3 engine: {e}")
        return None

# Singleton instance of the pyttsx3 engine
engine = initialize_engine()
engine_lock = threading.Lock()  # Lock to manage concurrent access to the engine

def speak_text(text):
    """Speak text asynchronously using a separate thread"""
    if not engine:
        print("Text-to-speech engine is not available.")
        return

    def speak():
        try:
            with engine_lock:  # Acquire lock before using the engine
                engine.say(text)
                engine.runAndWait()  # Run the speech loop
        except Exception as e:
            print(f"Error in speech synthesis: {e}")
    
    # Run speech in a background thread to avoid blocking
    threading.Thread(target=speak).start()
def get_response(user_message):
    """Fetch response based on user input"""
    if not user_message or not isinstance(user_message, str):
        return responses["default"]

    user_message = user_message.lower()

    # List of keywords in order of priority (specific to generic)
    priority_keywords = [
        "scholarship", "placement", "compare", "cutoff", "eligibility",
        "courses", "fees", "rank", "application", "deadline", "admission",
        "thanks", "bye", "hello", "hi"
    ]

    # Check for exact matches first
    if user_message in responses:
        return responses[user_message]

    # Check for specific keywords in priority order
    for keyword in priority_keywords:
        if keyword in user_message:
            return responses[keyword]

    # Fallback to default response
    return responses["default"]


def listen_speech():
    """Convert speech to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Set a timeout
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return "I couldn't understand, please try again."
        except sr.RequestError:
            return "Speech recognition service is unavailable."
        except Exception as e:
            return f"An error occurred: {e}"

@app.route("/chat", methods=["POST"])
def chat():
    """Handle text-based chat requests"""
    user_message = request.json.get("message")
    if not user_message or not isinstance(user_message, str):
        return jsonify({"error": "Invalid or missing message"}), 400

    reply = get_response(user_message)

    # Respond with text first
    response_data = {"response": reply}

    # Speak response asynchronously
    speak_text(reply)

    return jsonify(response_data)

@app.route("/voice-chat", methods=["POST"])
def voice_chat():
    """Handle voice-based chat"""
    user_message = listen_speech()
    reply = get_response(user_message)

    # Respond with text first
    response_data = {"user_message": user_message, "response": reply}

    # Speak response asynchronously
    speak_text(reply)

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
