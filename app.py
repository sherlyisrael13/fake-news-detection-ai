from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load('models/logreg_best_model.pkl')

# Explanation function (same as your notebook)
def generate_explanation(text, prediction):
    text = text.lower()

    fake_keywords = ['shocking', 'breaking', 'unbelievable', 'secret', 'exposed']
    real_keywords = ['report', 'official', 'confirmed', 'according to', 'data']

    if prediction == 1:
        for word in fake_keywords:
            if word in text:
                return "Sensational language detected, likely fake news."
        return "Lacks factual indicators."

    else:
        for word in real_keywords:
            if word in text:
                return "Contains factual indicators, likely real news."
        return "Neutral informative tone."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    prediction = model.predict([text])[0]
    label = "FAKE" if prediction == 1 else "REAL"
    explanation = generate_explanation(text, prediction)

    return jsonify({
        'prediction': label,
        'explanation': explanation
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
