import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load datasets
project_data = pd.read_csv("project_data.csv")
workforce_data = pd.read_csv("workforce_data.csv")
supply_data = pd.read_csv("supply_data.csv")
cost_data = pd.read_csv("cost_data.csv")

# Merge cost data with project data for cost model
cost_model_data = pd.merge(cost_data, project_data, on="Project_ID")
X_cost = cost_model_data[["Budget($)", "Progress(%)"]]
y_cost = cost_model_data["Expenditure($)"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_cost, y_cost, test_size=0.2, random_state=42)

# Train cost prediction model
cost_model = RandomForestRegressor(n_estimators=100, random_state=42)
cost_model.fit(X_train, y_train)
y_pred = cost_model.predict(X_test)

# Evaluate cost model
print("Cost Model MAE:", mean_absolute_error(y_test, y_pred))
print("Cost Model R2 Score:", r2_score(y_test, y_pred))

# Workforce efficiency model
X_workforce = workforce_data[["Hours_Worked"]]
y_workforce = workforce_data["Efficiency(%)"]
X_train, X_test, y_train, y_test = train_test_split(X_workforce, y_workforce, test_size=0.2, random_state=42)

workforce_model = LinearRegression()
workforce_model.fit(X_train, y_train)
y_pred = workforce_model.predict(X_test)

print("Workforce Model MAE:", mean_absolute_error(y_test, y_pred))
print("Workforce Model R2 Score:", r2_score(y_test, y_pred))

# Supply chain analysis
supply_data["Delayed"] = supply_data["Delivery_Status"].apply(lambda x: 1 if x == "Delayed" else 0)
X_supply = supply_data[["Cost_Per_Unit"]]
y_supply = supply_data["Delayed"]
X_train, X_test, y_train, y_test = train_test_split(X_supply, y_supply, test_size=0.2, random_state=42)

supply_model = RandomForestRegressor(n_estimators=100, random_state=42)
supply_model.fit(X_train, y_train)
y_pred = supply_model.predict(X_test)

print("Supply Chain Model MAE:", mean_absolute_error(y_test, y_pred))
print("Supply Chain Model R2 Score:", r2_score(y_test, y_pred))

# Save models
import joblib
joblib.dump(cost_model, "cost_model.pkl")
joblib.dump(workforce_model, "workforce_model.pkl")
joblib.dump(supply_model, "supply_model.pkl")
