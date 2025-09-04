"""
trajectory_lanechange.py

Generates a lane change trajectory using the BicycleModel.
Exports trajectory data (time, v, w) and saves a trajectory plot.
"""

import numpy as np
import matplotlib.pyplot as plt
from bicycle_model import BicycleModel

# Simulation parameters
sample_time = 0.01
time_end = 20.0

# Initialize model
model = BicycleModel()
model.reset()

# Time vector
t_data = np.arange(0, time_end, sample_time)
N = len(t_data)

# Storage
x_data = np.zeros(N)
y_data = np.zeros(N)
v_data = np.zeros(N)
w_data = np.zeros(N)

# Vehicle parameters
v_const = 6.0  # [m/s]
lanechange_start = 4.0   # [s]
lanechange_duration = 2.0  # [s]
lanechange_end = lanechange_start + lanechange_duration
delta_max = 0.25             # rad  (~14.3°) ajustable

# Define control inputs
v_data[:] = v_const
W0 = (2*np.pi*delta_max) / lanechange_duration
W0 = np.clip(W0, -model.w_max, model.w_max)  

for i, t in enumerate(t_data):
    if lanechange_start <= t <= lanechange_end:
        tau = (t - lanechange_start) / lanechange_duration  # 0..1
        delta = delta_max * np.sin(2*np.pi*tau)  # steering angle
        # w = (delta - delta_prev)/dt
        if i == 0:
            w_data[i] = 0.0
        else:
            w_data[i] = (delta - delta_prev) / sample_time
        delta_prev = delta
    else:
        w_data[i] = 0.0
        delta_prev = 0.0



# Run simulation
for i in range(N):
    state = model.step(v_data[i], w_data[i], sample_time)
    x_data[i], y_data[i], _, _ = state

# Save trajectory data
np.savetxt("lanechange.txt", np.column_stack((t_data, v_data, w_data)),
           header="time [s], v [m/s], w [rad/s]", comments="")

# Plot trajectory
plt.figure()
plt.axis("equal")
plt.plot(x_data, y_data, label="Lane Change Trajectory")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Bicycle Model - Lane Change Trajectory")
plt.legend()
plt.grid(True)
plt.savefig("lanechange.png", dpi=300)
plt.show()