def validate_input(data):
    """
    Validate the input data to ensure all required keys are present.
    """
    required_keys = ['age', 'bmi', 'children', 'smoker', 'region']
    for key in required_keys:
        if key not in data:
            return False, f"Missing key: {key}"
    return True, "Valid input"

def preprocess_input(data):
    """
    Preprocess input data to convert categorical features into numerical format.
    """
    smoker_map = {'yes': 1, 'no': 0}
    region_map = {'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3}

    return [
        data['age'],
        data['bmi'],
        data['children'],
        smoker_map.get(data['smoker'].lower(), 0),  # Default to 0 if key is missing
        region_map.get(data['region'].lower(), 0)  # Default to 0 if key is missing
    ]
