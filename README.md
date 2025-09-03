# Bicycle Kinematic Model – Vehicle Trajectory Simulation

This repository implements the **kinematic bicycle model**, widely used in vehicle dynamics and autonomous driving for trajectory tracking and control validation.

## 🚗 Model equations

<img width="734" height="356" alt="image" src="https://github.com/user-attachments/assets/fc092ec0-99bd-4364-9c3c-af0983251ee2" />

The bicycle kinematics are given by:

<img width="183" height="155" alt="image" src="https://github.com/user-attachments/assets/b7b77d9e-afe4-461d-8b74-b1403919063c" />


where:
- \(v\): vehicle speed [m/s]
- \(\theta\): heading [rad]
- \(\delta\): steering angle [rad]
- \(\omega\): steering angle rate [rad/s]
- \(L\): wheelbase [m]
- \(l_r\): distance from rear axle to CoM [m]

## 📊 Features
- Python class `BicycleModel` with both **steering rate input** and **steering angle input**.
- Simulation of different trajectories:
  - Circle
  - Figure 8
  - Lane change
- Example plots included.

## ▶️ Usage
```python
from bicycle_model import BicycleModel
import numpy as np

# Initialize model
model = BicycleModel(L=2.0, lr=1.2, w_max=1.22)

# Run a simple trajectory
t, x, y = model.simulate_circle(v=4.0, R=8.0, T=20.0)

# Plot trajectory
import matplotlib.pyplot as plt
plt.axis("equal")
plt.plot(x, y)
plt.show()

