# Bicycle Kinematic Model – Vehicle Trajectory Simulation

This repository implements the **kinematic bicycle model** in Python, widely used in vehicle dynamics and autonomous driving for trajectory tracking and control validation, and demonstrates its application by generating different trajectories.  
It is a compact project designed to showcase fundamental concepts in **vehicle dynamics, trajectory generation, and control inputs**.

## 🚗 Model equations
The **kinematic bicycle model** is a simplified representation of a vehicle’s motion, often used in autonomous driving, robotics, and vehicle dynamics research.  
It captures the relationship between velocity, steering inputs, and vehicle trajectory.

<img width="734" height="356" alt="image" src="https://github.com/user-attachments/assets/fc092ec0-99bd-4364-9c3c-af0983251ee2" />

The bicycle kinematics are given by:

<img width="183" height="155" alt="image" src="https://github.com/user-attachments/assets/b7b77d9e-afe4-461d-8b74-b1403919063c" />


where:
- v: vehicle speed [m/s]
- θ (theta): heading [rad]
- δ (delta): steering angle [rad]
- ω (omega): steering angle rate [rad/s]
- L: wheelbase [m]
- l_r: distance from rear axle to CoG [m]

## 📊 Features
This project includes:
- Python class `BicycleModel`  implementing the kinematic bicycle equations with both **steering rate input** and **steering angle input**.
- A script to Simulate of different trajectories:
  - Figure 8
  - Lane change
  - Wave Path
  - Square
- Export of trajectory data (`*.txt`) and trajectory plot (`*.png`).


## ▶️ Usage
1. Clone this repository:

2. Install requirements (only NumPy & Matplotlib needed):
pip install numpy matplotlib

3. Run the trajectory script:
ej. python trajectory_figure8.py

4. Outputs:
figure8.png → trajectory plot /
figure8.txt → exported time, velocity, and steering inputs

