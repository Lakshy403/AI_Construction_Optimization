import pickle
import numpy as np

cost_model = pickle.load(open("models/cost_model.pkl", "rb"))

def forecast_cost(data):
    features = np.array([data['project_size'], data['material_cost'], data['labor_cost']]).reshape(1, -1)
    predicted_cost = cost_model.predict(features)
    return predicted_cost[0]
