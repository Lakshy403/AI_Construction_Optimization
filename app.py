from flask import Flask, request, jsonify
from risk_prediction import predict_risk
from workforce_optimization import optimize_schedule
from supply_chain import supply_chain_analysis
from site_monitoring import detect_anomalies
from cost_forecasting import forecast_cost

app = Flask(__name__)

@app.route('/predict_risk', methods=['POST'])
def risk_prediction():
    data = request.json
    prediction = predict_risk(data)
    return jsonify({'risk_level': prediction})

@app.route('/optimize_workforce', methods=['POST'])
def workforce_optimization():
    data = request.json
    schedule = optimize_schedule(data)
    return jsonify({'optimized_schedule': schedule})

@app.route('/supply_chain', methods=['POST'])
def supply_chain():
    data = request.json
    response = supply_chain_analysis(data)
    return jsonify(response)

@app.route('/monitor_site', methods=['POST'])
def site_monitoring():
    image_data = request.files['image']
    anomalies = detect_anomalies(image_data)
    return jsonify({'anomalies': anomalies})

@app.route('/forecast_cost', methods=['POST'])
def cost_forecasting():
    data = request.json
    forecast = forecast_cost(data)
    return jsonify({'predicted_cost': forecast})

if __name__ == '__main__':
    app.run(debug=True)
