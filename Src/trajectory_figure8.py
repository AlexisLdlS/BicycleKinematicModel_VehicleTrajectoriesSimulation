"""
trajectory_figure8.py

Generates a figure-eight trajectory using the BicycleModel.
Exports trajectory data (time, v, w) and saves a trajectory plot.
"""

import numpy as np
import matplotlib.pyplot as plt
from bicycle_model import BicycleModel

# Simulation parameters
sample_time = 0.01
time_end = 30.0

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
v_const = 4.0   # constant velocity [m/s]
R = 8.0         # turning radius [m]
delta_desired = np.arctan(model.L / R)

# Ramp steering rate
t_ramp = delta_desired / model.w_max
n_ramp = max(1, int(round(t_ramp / sample_time)))
steps_half = N // 2

# Define control inputs
v_data[:] = v_const

# First circle
w_data[:n_ramp] = model.w_max
w_data[n_ramp:steps_half-n_ramp] = 0.0
w_data[steps_half:steps_half+n_ramp*2] = -model.w_max
w_data[steps_half+n_ramp*2:] = 0.0

# Run simulation
for i in range(N):
    state = model.step(v_data[i], w_data[i], sample_time)
    x_data[i], y_data[i], _, _ = state

# Save trajectory data
np.savetxt("figure8.txt", np.column_stack((t_data, v_data, w_data)),
           header="time [s], v [m/s], w [rad/s]", comments="")

# Plot trajectory
plt.figure()
plt.axis("equal")
plt.plot(x_data, y_data, label="Trajectory")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Bicycle Model - Figure 8 Trajectory")
plt.legend()
plt.grid(True)
plt.savefig("figure8.png", dpi=300)
plt.show()
