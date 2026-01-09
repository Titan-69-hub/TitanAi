from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Titan AI Python Backend Running 🚀"
from transformers import pipeline

# Global: Load model once
generator = pipeline("text-generation", model="gpt2")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"reply": "Message missing"}), 400

    # Hugging Face GPT-2 AI RESPONSE
    response = generator(user_message, max_length=50, do_sample=True, temperature=0.7)
    ai_reply = response[0]['generated_text']

    return jsonify({"reply": ai_reply})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"reply": "Message missing"}), 400

    # DUMMY AI RESPONSE
    reply = f"Titan AI received: '{user_message}' 🤖"
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
