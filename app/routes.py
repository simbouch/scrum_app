from flask import Blueprint, render_template, request, jsonify
from app.model import predict_expenses

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html', title="Home - Medical Expenses Prediction")

@routes.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            "age": int(request.form['age']),
            "bmi": float(request.form['bmi']),
            "children": int(request.form['children']),
            "smoker": int(request.form['smoker']),
            "region": request.form['region']
        }
        prediction = predict_expenses(data)
        return render_template('result.html', title="Prediction Result", prediction=prediction)
    except Exception as e:
        return render_template('error.html', title="Error", error_message=str(e))
