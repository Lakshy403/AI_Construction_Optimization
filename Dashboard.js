import React, { useState } from "react";

function Dashboard() {
  const [riskLevel, setRiskLevel] = useState("Unknown");

  const handleRiskPrediction = async () => {
    const response = await fetch("http://localhost:5000/predict_risk", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ weather: 3, material_cost: 5000, labor_availability: 80 })
    });
    const data = await response.json();
    setRiskLevel(data.risk_level);
  };

  return (
    <div>
      <h2>Risk Prediction</h2>
      <p>Current Risk Level: {riskLevel}</p>
      <button onClick={handleRiskPrediction}>Predict Risk</button>
    </div>
  );
}

export default Dashboard;
