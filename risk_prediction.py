import pickle
import numpy as np

# Load pre-trained model
risk_model = pickle.load(open("models/risk_model.pkl", "rb"))

def predict_risk(data):
    features = np.array([data['weather'], data['material_cost'], data['labor_availability']]).reshape(1, -1)
    risk_level = risk_model.predict(features)
    return risk_level[0]
