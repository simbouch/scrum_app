from app.model import predict_expenses

def test_model_prediction():
    input_data = {
        "age": 45,
        "bmi": 28.5,
        "children": 2,
        "smoker": 0,
        "region": "southeast"
    }
    prediction = predict_expenses(input_data)
    assert prediction is not None
    assert isinstance(prediction, float)  # Assuming the model outputs a float
