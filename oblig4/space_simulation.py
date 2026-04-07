"""
In this program, we simulate the space. We introduce particles, a planet and a
spaceship to the simulation.
"""

# Import libraries
# ---------------
import pyglet
from pyglet.gl import glEnable, GL_DEPTH_TEST
import lib
import numpy as np

# Window
# ------
window = pyglet.window.Window()
window.width = 1280
window.height = 720

# Depth testing enables occlusion culling.
glEnable(GL_DEPTH_TEST)

batch = pyglet.graphics.Batch()

# Global State
# ------------
# The global state ensures that the correct parameters and values are uploaded
# to the shader/GPU. We update the state in the draw function.
global_state = lib.GlobalState()

# Objects
# -------
sphere = lib.Sphere(0, 5, 0, 5, (255, 0, 0, 255), batch)
world_grid = lib.WorldGrid(pyglet.graphics.Batch())

# Camera
# ------
camera = lib.Camera(width=window.width, height=window.height,
                    fov=60,
                    near=0.01, far=1000.0)

camera.x = 20
camera.y = 10
camera.z = 20

@window.event
def on_draw():
    window.clear()
    
    # The global state needs the camera and the light position
    global_state.update(camera.get_position(), np.zeros(3))
    
    # Update the camera matrices
    window.projection = camera.get_projection()
    window.view = camera.get_look_at()
    
    # Draw objects
    batch.draw()
    world_grid.draw()
    
pyglet.app.run()