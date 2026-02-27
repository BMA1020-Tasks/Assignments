# Assignment 3

This assignment is a continuation of *assignment 3*, and we will take the simulations a step further into 3-dimensional space. Whilst the task descriptions are similar to the previous assignment, there are some minor changes. Please read them carefully to not miss important details.

- [Part 1: Particle Systems](#part-1-particle-systems)
- Part 2: TBA
- [Additional Library](#additional-library)

## Deadline
| Action | Time |
|---|---|
|Opened| 27.02.2026|
|Deadline|TBA|

## Part 1: Particle Systems
In this task, we will create a particle system in 3D space. In it, a particle is a point in Cartesian space with a set of properties. We will use Pyglet to visualise them, i.e. providing a shape to each particle.

### Specifications
  - Window size: 1280x720.
  - Particles spawn with a random size. You are free to choose a reasonable size.
  - All particles spawn from the same Cartesian coordinate (it's okay to move the spawning point with keyboard or mouse inputs during runtime).
  - Particles spawn with colors of your choice. Once an invididual particle's color is set, it must persist throughout its lifetime.
  - Particles spawn with a random velocity.
  - Particles are affected by gravitational force.
  - Particles spawn at a fixed rate.
  - There is a boundary box that particles can only live in. Once a particle steps outside the boundary, it dies.

Additional requirements:
  - To create an interactive simulation, we will introduce the camera to our the simulation.
  - Enable the camera to orbit around the simulation, so it can be viewed from different angles.

We have provided an additional library for the camera and the shapes that extend Pyglet. More about this in [Additional Library](#additional-library).

### Part 2: Geometric Optics
TBA

## Additional Library
[`lib`](./lib/) is our own internal library which extends Pyglet's capabilities. Even though Pyglet uses modern graphics technologies, it is implemented as a 2D library. `lib` extends Pyglet to support 3D. Whilst we have done most of the work, as part of the assignment you will contribute to a portion of the library [see here](#additional-library---tasks).

### Overview


### Additional Library - Tasks
To complete the library, you will do the following:

Task 1: Implement function `translate(...)` function in [lib/transformations.py](./lib/transformations.py).

Task 2: Implement function `scale(...)` in [lib/transformations.py](./lib/transformations.py).

Task 3: Implement rotation function(s). We have already provided `rotate_z(...)`, `rotate_y(...)` and `rotate_x(...)`, but you can a different function, e.g. using quaternions or rotating around an arbitrary axis.

Task 4: In [lib/Camera.py](./lib/Camera.py), complete method `get_projection()`. This returns the camera's projection matrix.

Task 5: In [lib/Camera.py](./lib/Camera.py), complete method `get_look_at()`. This returns a matrix that describes the camera's orientation, position and the up vector.


## Demo - Particle systems (Part 1)
The task description is explained in [particles.py](./particles.py). The simulation may look as follow:

![Particles recording](./videos/particles.mp4)

## Submission
As part of the submission, please upload the following files:
- [particles.py](./particles.py)
- [geometric.py](./geometric.py)
