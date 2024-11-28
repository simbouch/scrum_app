from flask import Blueprint, request, jsonify, render_template
from app.model import predict_expenses

# Define Blueprint
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    """
    Render the home page with the input form.
    """
    return render_template('index.html', title="Medical Expenses Prediction")

@routes.route('/predict', methods=['POST'])
def predict():
    """
    Handle POST requests to predict medical expenses.
    """
    try:
        # Extract input data from the form
        data = {
            "age": int(request.form['age']),
            "bmi": float(request.form['bmi']),
            "children": int(request.form['children']),
            "smoker": request.form['smoker'],
            "region": request.form['region']
        }
        # Make prediction
        prediction = predict_expenses(data)
        if "error" in prediction:
            return render_template('error.html', error_message=prediction['error'])
        return render_template('result.html', prediction=prediction['prediction'])
    except Exception as e:
        return render_template('error.html', error_message=str(e))
