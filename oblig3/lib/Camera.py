import numpy as np
from .transformations import *
from pyglet.math import Mat4, Vec3
import math
from .transformations import perspective, look_at


class Camera:
    def __init__(self, width, height, fov, near, far):
        self.distance = 10
        self.theta = 0
        self.phi = 0

        self.width = width
        self.height = height
        self.fov = math.radians(fov)
        self.near = near
        self.far = far
        self.perspective: np.array = object
        self.view: np.array = object

    def get_position(self) -> Vec3:
        x = self.distance * np.cos(self.phi) * np.sin(self.theta)
        y = self.distance * np.sin(self.phi)
        z = self.distance * np.cos(self.phi) * np.cos(self.theta)

        return Vec3(x, y, z)

    def get_projection(self) -> Mat4:
        """Get the camera's projection matrix. Returns a 4x4 matrix"""
        # Task 4
        # This is a placement matrix. Adjust this according to the task.
        return Mat4(
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0,
        )
        
    def get_look_at(self) -> Mat4:
        """Get a look at matrix. Returns a 4x4 matrix."""
        # Task 5
        # This is a placement matrix. Adjust this according to the task.
        return Mat4(
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0,
        )