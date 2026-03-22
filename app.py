from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        reading = float(request.form['reading'])
        writing = float(request.form['writing'])

        print("Reading:", reading)
        print("Writing:", writing)

        sample = [[reading, writing]]
        print("Sample:", sample)

        sample_scaled = scaler.transform(sample)
        print("Scaled:", sample_scaled)

        prediction = model.predict(sample_scaled)[0]
        print("Prediction:", prediction)

        result = "Pass" if prediction == 1 else "Fail"

        return render_template('index.html', prediction_text=f"Result: {result}")

    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)