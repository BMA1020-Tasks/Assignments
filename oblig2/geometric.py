"""
Here we will simulate light passing through a lens in 2D.

1. On program start, create a lens and a light source
2. Draw the lens
3. Draw rays of light emanating from the light source
4. Rays incident on the lens should be reflected/refracted 
   according to Snell's law
   
The lens is to be a simple, spherical (circular, as it is 2D) lens, 
specified by the centres and radius of curvature of the bounding circles, and
the height of the lens.

The light source should be a point source, i.e. sending rays in all directions
from a given point. This point can be "at infinity", in which case the rays
fill the screen and are all parallel. 

You should store parameters sufficient to describe the rays (lines) in a numpy
array (e.g. position and direction vectors, two points on the line, etc).

In this assignment you can draw the rays using pyglet.shapes.Line, but in the
next assignment (in 3D) you will make use of a library we provide with similar
functionality.

It is recommended to use vector methods to find, e.g. the intersection of rays
and the lens. This is because you will then be able to reuse the code for the
3d case without substantial changes.

Bonus: interactivity!
    - move the lens (including rotation)
    - move the light source
    - change the lens parameters
"""
