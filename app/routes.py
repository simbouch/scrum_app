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
    Always return 300 euros as the prediction.
    """
    try:
        # Extract input data from the form (optional, kept for validation purposes)
        data = {
            "age": int(request.form['age']),
            "bmi": float(request.form['bmi']),
            "children": int(request.form['children']),
            "smoker": request.form['smoker'],
            "region": request.form['region']
        }

        # Return a fixed prediction value
        prediction = "3000 euros"
        return render_template('result.html', prediction=prediction)
    except Exception as e:
        return render_template('error.html', error_message=str(e))

