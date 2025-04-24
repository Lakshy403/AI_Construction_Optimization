import matplotlib.pyplot as plt
import numpy as np

# Model names
models = ['Cost Model', 'Workforce Model', 'Supply Chain Model']

# Performance metrics
mae = [141543.69, 12.94, 0.365]
r2_scores = [-0.6949, 0.0087, 0.0]

# Plotting MAE
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(models, mae, color='skyblue')
plt.title('Mean Absolute Error (MAE) of Models')
plt.ylabel('MAE')
plt.ylim(0, max(mae) * 1.2)

# Plotting R² Scores
plt.subplot(1, 2, 2)
plt.bar(models, r2_scores, color='salmon')
plt.title('R² Score of Models')
plt.ylabel('R² Score')
plt.ylim(min(r2_scores) * 1.2, 1)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Model names
models = ['Cost Model', 'Workforce Model', 'Supply Chain Model']

# Performance metrics
mae = [141543.69, 12.94, 0.365]
r2_scores = [-0.6949, 0.0087, 0.0]

# Plotting MAE
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(models, mae, color='skyblue')
plt.title('Mean Absolute Error (MAE) of Models')
plt.ylabel('MAE')
plt.ylim(0, max(mae) * 1.2)

# Plotting R² Scores
plt.subplot(1, 2, 2)
plt.bar(models, r2_scores, color='salmon')
plt.title('R² Score of Models')
plt.ylabel('R² Score')
plt.ylim(min(r2_scores) * 1.2, 1)

plt.tight_layout()
plt.show()

# Cost distribution data
categories = ['Labor', 'Materials', 'Equipment', 'Miscellaneous']
costs = [500000, 300000, 150000, 50000]  # Example values

# Plotting pie chart
plt.figure(figsize=(8, 8))
plt.pie(costs, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Project Cost Distribution')
plt.show()

# Workforce data
roles = ['Engineers', 'Laborers', 'Supervisors', 'Technicians']
counts = [10, 50, 5, 15]  # Example values

# Plotting bar chart
plt.figure(figsize=(10, 6))
plt.bar(roles, counts, color='lightgreen')
plt.title('Workforce Allocation by Role')
plt.xlabel('Role')
plt.ylabel('Number of Workers')
plt.ylim(0, max(counts) * 1.2)
plt.show()
# Supply chain efficiency data
weeks = np.arange(1, 13)  # 12 weeks
efficiency = [80, 82, 78, 85, 88, 90, 87, 85, 89, 91, 93, 95]  # Percentage values

# Plotting line graph
plt.figure(figsize=(10, 6))
plt.plot(weeks, efficiency, marker='o', linestyle='-', color='purple')
plt.title('Supply Chain Efficiency Over Time')
plt.xlabel('Week')
plt.ylabel('Efficiency (%)')
plt.ylim(0, 100)
plt.grid(True)
plt.show()

# Project phases data
phases = ['Planning', 'Design', 'Construction', 'Testing']
progress = {
    'Week 1': [10, 0, 0, 0],
    'Week 2': [20, 10, 0, 0],
    'Week 3': [30, 20, 10, 0],
    'Week 4': [40, 30, 20, 10],
    'Week 5': [50, 40, 30, 20],
    'Week 6': [60, 50, 40, 30],
    'Week 7': [70, 60, 50, 40],
    'Week 8': [80, 70, 60, 50],
    'Week 9': [90, 80, 70, 60],
    'Week 10': [100, 90, 80, 70],
    'Week 11': [100, 100, 90, 80],
    'Week 12': [100, 100, 100, 90],
}

# Preparing data for plotting
weeks = list(progress.keys())
data = np.array(list(progress.values())).T  # Transpose for stacking

# Plotting stacked bar chart
plt.figure(figsize=(12, 7))
bottom = np.zeros(len(weeks))

for i, phase in enumerate(phases):
    plt.bar(weeks, data[i], bottom=bottom, label=phase)
    bottom += data[i]

plt.title('Project Timeline Progress')
plt.xlabel('Week')
plt.ylabel('Completion Percentage')
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


