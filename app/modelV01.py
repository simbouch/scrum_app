import pickle

def get_user_input():
    data = {
        "age": None,
        "bmi": None,
        "children": None,
        "smoker": None,
        "region": None,
        "heavyCase": None
    }
    
    try:
        data["age"] = float(input("Enter age: "))
        data["bmi"] = float(input("Enter BMI: "))
        data["children"] = int(input("Enter number of children: "))
        data["smoker"] = int(input("Are you a smoker? (1 for Yes, 0 for No): "))
        data["region"] = int(input("Enter region (as an integer 1,2,3 or 4): "))
        data["heavyCase"] = int(input("Is this a heavy case? (1 for Yes, 0 for No): "))
    except ValueError as e:
        print(f"Invalid input: {e}")
    
    return data

def predict_expenses(data, coefficients):
    prediction = coefficients["Intercept"]
    for key in data:
        prediction += coefficients[key] * data[key]
    return prediction

if __name__ == "__main__":
    user_data = get_user_input()
    print("Entered data:", user_data)

    significant_coefficients = {
        "Intercept": 13041.15169847328,
        "age": 3031.133367457519,
        "bmi": 462.8933240358457,
        "children": 666.8734098322169,
        "smoker": 5165.31080344811,
        "region": -277.93606962268314,
        "heavyCase": 6057.491938649431
    }
    
    # Predict expenses
    predicted_expense = predict_expenses(user_data, significant_coefficients)
    print(f"Predicted medical expenses: {predicted_expense:.2f}")
    
    # Pickle the model
    with open('medical_model.pkl', 'wb') as file:
        pickle.dump(significant_coefficients, file)
    print("Model coefficients have been pickled to 'medical_model.pkl'")

    # Load the pickled model (for demonstration purposes)
    with open('medical_model.pkl', 'rb') as file:
        loaded_coefficients = pickle.load(file)
    print("Loaded coefficients:", loaded_coefficients)
    
    # Predict using the loaded model
    loaded_predicted_expense = predict_expenses(user_data, loaded_coefficients)
    print(f"Predicted medical expenses using loaded model: {loaded_predicted_expense:.2f}")
