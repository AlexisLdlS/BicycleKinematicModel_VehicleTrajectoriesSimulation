"""
trajectory_lanechange.py

Generates a Wave Square Path trajectory using the BicycleModel.
Exports trajectory data (time, v, w) and saves a trajectory plot.
"""

import numpy as np
import matplotlib.pyplot as plt
from bicycle_model import BicycleModel

# Simulation parameters
sample_time = 0.01
time_end = 60.0

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

# Define control inputs
v_data[:] = v_const
w_data[:] = 0
w_data[0:100] = 1
w_data[100:300] = -1
w_data[300:500] = 1
w_data[500:5700] = np.tile(w_data[100:500], 13)
w_data[5700:] = -1

# Run simulation
for i in range(N):
    state = model.step(v_data[i], w_data[i], sample_time)
    x_data[i], y_data[i], _, _ = state

# Save trajectory data
np.savetxt("WavePath.txt", np.column_stack((t_data, v_data, w_data)),
           header="time [s], v [m/s], w [rad/s]", comments="")

# Plot trajectory
plt.figure()
plt.axis("equal")
plt.plot(x_data, y_data, label="Wave Path Trajectory")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Bicycle Model - Wave Path Trajectory")
plt.legend()
plt.grid(True)
plt.savefig("WavePath.png", dpi=300)
plt.show()
