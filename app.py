from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Disable debug mode for production performance
app.config['DEBUG'] = False

# Load the trained model and scaler once at startup
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Prediction request received!")  # Debug output
        
        # Get data from form - optimize with list comprehension
        feature_names = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 
                        'ejection_fraction', 'high_blood_pressure', 'platelets', 
                        'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']
        
        input_data = [float(request.form[name]) for name in feature_names]
        print(f"Input data: {input_data}")  # Debug output

        # Scale input and predict in one pipeline
        scaled_data = scaler.transform([input_data])
        prediction = model.predict(scaled_data)[0]
        print(f"Prediction: {prediction}")  # Debug output

        result = "❌ Patient is likely to die." if prediction == 1 else "✅ Patient is likely to survive."
        print(f"Result: {result}")  # Debug output
        
        return render_template("index.html", prediction_text=result)

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debug output
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    # Production optimized settings
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
