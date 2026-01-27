"""
In this task, we will create a particle/ball system. In the system, a particle
is a point in Cartesian space with a set of properties. We will use Pyglet to
visualise them, i.e. providing a shape to each particle.

Specifications
  - Window size: 1280x720.
  - Particles spawn with a random radius between 7.0 and 13.0 pixels.
  - All particles spawn from the same position on the screen (it's okay to move
    the spawning point with keyboard or mouse inputs during runtime).
  - Particles spawn with colors of your choice. Once a particle's color is set,
    it must persist throughout its lifetime.
  - Particles spawn with a random speed between 100 and 200 at a random angle.
  - On starting the application, 10 particles are spawned immediately.
    Thereafter, between 5 and 10 particles are spawned every second.

Bonus:
  - Kill the particles after their maximum life time has exceeded.
"""

