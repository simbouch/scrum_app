from flask import Blueprint, request, jsonify
from app.model import predict_expenses

routes = Blueprint('routes', __name__)

@routes.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = predict_expenses(data)
    return jsonify({"prediction": prediction})
