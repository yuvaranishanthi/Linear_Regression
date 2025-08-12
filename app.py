from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model/lr_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch form data
        features = [float(request.form[f]) for f in request.form]
        final_features = scaler.transform([features])
        prediction = model.predict(final_features)
        return render_template('result.html', prediction_text=f'Predicted Price: ₹{round(prediction[0], 2)}')
    except Exception as e:
        return render_template('result.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
