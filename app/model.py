import joblib
import os

# Define the path to the model file
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models/medical_model.pkl')

# Load the model
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please check the file path.")

def predict_expenses(data):
    """
    Predict medical expenses based on input data.
    """
    from app.utils import validate_input, preprocess_input

    # Validate input
    is_valid, message = validate_input(data)
    if not is_valid:
        return {"error": message}

    try:
        # Preprocess input
        features = preprocess_input(data)
        # Perform prediction
        prediction = model.predict([features])
        return {"prediction": prediction[0]}
    except Exception as e:
        return {"error": f"An error occurred during prediction: {e}"}
