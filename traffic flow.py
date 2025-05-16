import pandas as pd
import numpy as np
import networkx as nx
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Simulated Traffic Data
data = {
    'road_id': [1, 2, 3, 4, 5],
    'vehicle_count': [50, 120, 30, 200, 90],
    'avg_speed': [45, 20, 60, 10, 35],
    'accidents_reported': [0, 1, 0, 2, 0],
    'congestion_level': [0.3, 0.9, 0.1, 0.95, 0.6]  # Target
}

df = pd.DataFrame(data)

# Train Model to Predict Congestion
X = df[['vehicle_count', 'avg_speed', 'accidents_reported']]
y = df['congestion_level']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict Congestion on New Data
test_data = pd.DataFrame({
    'vehicle_count': [80, 150],
    'avg_speed': [30, 15],
    'accidents_reported': [0, 1]
})

predictions = model.predict(test_data)
print("Predicted Congestion Levels:", predictions)

# Create Road Network Graph
G = nx.DiGraph()
edges = [
    ('A', 'B', 0.3),
    ('B', 'C', 0.9),
    ('A', 'D', 0.1),
    ('D', 'C', 0.95),
    ('B', 'D', 0.6)
]

for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)

# Find Best Path from A to C (least congestion)
best_path = nx.shortest_path(G, source='A', target='C', weight='weight')
print("Optimized Route from A to C:", best_path)
