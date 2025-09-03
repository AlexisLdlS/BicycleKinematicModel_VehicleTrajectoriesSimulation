"""
bicycle_model.py

This module implements a simple Kinematic Bicycle Model in Python.
It can be used to simulate vehicle trajectories given velocity and steering inputs.
"""

import numpy as np

class BicycleModel:
    """
    Kinematic Bicycle Model.

    Attributes
    ----------
    L : float
        Wheelbase length [m].
    lr : float
        Distance from rear axle to center of mass [m].
    w_max : float
        Maximum steering rate [rad/s].
    state : np.ndarray
        State vector [x, y, theta, delta] where:
            x     : position in x [m]
            y     : position in y [m]
            theta : heading angle [rad]
            delta : steering angle [rad]
    """

    def __init__(self, L=2.0, lr=1.2, w_max=1.22):
        self.L = L
        self.lr = lr
        self.w_max = w_max
        self.reset()

    def reset(self):
        """Reset the state to the origin with zero angles."""
        self.state = np.zeros(4)

    def step(self, v, w, dt):
        """
        Advance the model one time step using Euler integration.

        Parameters
        ----------
        v : float
            Longitudinal velocity [m/s].
        w : float
            Steering rate input [rad/s].
        dt : float
            Time step [s].
        """
        x, y, theta, delta = self.state

        # Limit steering rate
        w = np.clip(w, -self.w_max, self.w_max)

        # Update steering angle
        delta += w * dt

        # Slip angle (bicycle kinematics)
        beta = np.arctan((self.lr / self.L) * np.tan(delta))

        # State derivatives
        x_dot = v * np.cos(theta + beta)
        y_dot = v * np.sin(theta + beta)
        theta_dot = (v / self.L) * np.cos(beta) * np.tan(delta)

        # Integrate
        x += x_dot * dt
        y += y_dot * dt
        theta += theta_dot * dt

        self.state = np.array([x, y, theta, delta])
        return self.state
