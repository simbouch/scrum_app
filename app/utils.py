def validate_input(data):
    required_keys = ['age', 'bmi', 'children', 'smoker', 'region']
    for key in required_keys:
        if key not in data:
            return False, f"Missing key: {key}"
    return True, "Valid input"
