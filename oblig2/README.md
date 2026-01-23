# Assignment 2

In assignment 2, we will explore the following:
- Part 1: Particle systems
- Part 2: TBA

You may find *Part 1: Particle systems* in [particles.py](./particles.py).

## Details
Opened: 23.01.2025

Deadline:

## Part 1: Particle systems
In this task, we will create a particle/ball system. Here is a summary of how it
works:

1. On starting the program, we create an emitter. The emitter should initially
   spawn some particles to begin with.
2. A particle is an entity that has a shape, i.e. pyglet.shapes.Circle, that is
   expanded with velocity.
3. The program has an update method. When the particle updates, its position is
   updated based on its velocity, and lifetime is updated.


[ Program start ] -> [ Program update loop ] -> [ All particle updates, one by one ]

Specifications
  - Window size: 1280x720.
  - Particles spawn with a random radius between 7.0 and 13.0 pixels.
  - All particles spawn from the same position on the screen (it's okay to move
    them with the keyboard or mouse inputs during runtime).
  - Particles spawn with a color of your choice. Once its color is set, it
    must remain the same throughout its lifetime.
  - Particles spawn with a random speed between 100 and 200 at a random angle.
  - On starting the application, 10 particles are spawned immediately.
    Thereafter, between 5 and 10 particles are spawned every second.

Bonus:
  - Kill the particles after their maximum life time has exceeded.

## Submission
As part of the submission, please upload the following files:
- [particles.py](./particles.py)
- TBA
