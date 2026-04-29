# 📰 Fake News Detection using TF-IDF and Machine Learning

## 📌 Overview
This project focuses on detecting fake news articles using Natural Language Processing (NLP) techniques and Machine Learning models. The system uses **TF-IDF vectorization** combined with multiple classifiers to identify whether a news article is **REAL or FAKE**.

The project also includes:
- Model comparison
- Hyperparameter tuning
- Explainable predictions
- REST API deployment using Flask
- Docker containerization

---

## 🚀 Features
- Text preprocessing and feature extraction using TF-IDF
- Multiple ML models:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Random Forest
  - Naive Bayes
  - Multi-layer Perceptron (MLP)
- Hyperparameter tuning using GridSearchCV
- Model performance comparison
- Confusion matrix visualization
- Rule-based explanation generator
- REST API using Flask
- Dockerized deployment

---

## 🧠 Model Performance

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | 0.935    |
| SVM                 | 0.932    |
| Random Forest       | 0.920    |
| Naive Bayes         | 0.900    |
| MLP                 | 0.940    |

✅ **Best Model: MLP (94%)**

---

## 📊 Sample Output

Input:

Breaking shocking news revealed today

Output:

Prediction: FAKE
Explanation: Sensational language detected, likely fake news.


---

## ⚙️ Tech Stack

- Python
- Scikit-learn
- Pandas / NumPy
- Matplotlib / Seaborn
- Flask
- Docker

---

## 📁 Project Structure

├── app.py # Flask API
├── Dockerfile # Container configuration
├── requirements.txt # Dependencies
├── models/ # Trained models (ignored in Git)
├── notebooks/ # Jupyter notebooks
├── sentiment.py # Sentiment analysis module
└── README.md


---

## ▶️ Running Locally

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run Flask app

python app.py

### 3. Test API

curl -X POST http://127.0.0.1:5000/predict

-H "Content-Type: application/json"
-d '{"text": "Breaking shocking news revealed today"}'

---

## 🐳 Docker Deployment

### Build image

docker build -t fake-news-app .

### Run container

docker run -p 5001:5000 fake-news-app

---

## 📌 API Endpoint

**POST /predict**

Request:
```json
{
  "text": "your news text"
}
```
Response:
```
{
  "prediction": "FAKE",
  "explanation": "Sensational language detected..."
}
```
⚠️ Limitations

* Model depends on dataset quality
* Rule-based explanation is simplistic
* Version mismatch warnings in sklearn (non-critical)

📈 Future Improvements

* Use deep learning models (BERT, LSTM)
* Improve explainability (LIME/SHAP)
* Deploy on cloud (AWS/GCP)
* Build frontend UI

👤 Author

Josephine Sherly 

