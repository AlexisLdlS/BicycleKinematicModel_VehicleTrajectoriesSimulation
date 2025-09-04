"""
trajectory_square.py

Generates a square trajectory using the BicycleModel.
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
v_const = 4.0  # [m/s]
turn_duration = 2.0  # seconds per 90° corner

# Define control inputs
v_data[:] = v_const
w_data[670:670+100] = 0.753
w_data[670+100:670+100*2] = -0.753
w_data[2210:2210+100] = 0.753
w_data[2210+100:2210+100*2] = -0.753
w_data[3670:3670+100] = 0.753
w_data[3670+100:3670+100*2] = -0.753
w_data[5220:5220+100] = 0.753
w_data[5220+100:5220+100*2] = -0.753

# Run simulation
for i in range(N):
    state = model.step(v_data[i], w_data[i], sample_time)
    x_data[i], y_data[i], _, _ = state

# Save trajectory data
np.savetxt("square.txt", np.column_stack((t_data, v_data, w_data)),
           header="time [s], v [m/s], w [rad/s]", comments="")

# Plot trajectory
plt.figure()
plt.axis("equal")
plt.plot(x_data, y_data, label="Square Trajectory")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Bicycle Model - Square Trajectory")
plt.legend()
plt.grid(True)
plt.savefig("square.png", dpi=300)
plt.show()
