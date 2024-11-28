import joblib
import os

# Define the path to the model file
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models/medical_model.joblib')

# Load the model
model = joblib.load(MODEL_PATH)

def predict_expenses(data):
    try:
        features = [data['age'], data['bmi'], data['children'], data['smoker'], data['region']]
        prediction = model.predict([features])
        return prediction[0]
    except KeyError as e:
        return f"Missing key: {e}"
