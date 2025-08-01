# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_input = np.array([features])
    prediction = model.predict(final_input)[0]
    return render_template("index.html", prediction_text=f"Iris class predicted: {prediction}")

if __name__ == "__main__":
    app.run(debug=True)
