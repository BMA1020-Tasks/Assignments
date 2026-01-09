"""
In this tutorial, we will explain how to execute a Python script.

You are free to use any tools to execute the script. For the purpose of this
tutorial, we will use Visual Studio Code as it is used for many other purposes
(mobile, web and games programming, note taking, saving code to PDF, etc.). Most
importantly, the Python extension makes debugging code easy.

Topics covered:
    - Executing code from the CLI and with the GUI
    - Debugging code.
    - Useful habits to make writing code easier.

Topics NOT covered:
    - While we cover features necessary or nice-to-know, this is not a
      programming course. Therefore, we will not cover Python and programming
      features that we don't particularly need.
    - Debugging features beyond just "variables". You are free to and encouraged
      to explore these on your own.

Please note that code in this file are suggestive. There are endless ways to
structure and write code.
"""

# 1. We important libraries our code needs.
from time import sleep

# Try to discover what other library we need for this script.

# 2. If we have any global variables, we can declare them here
PI = 3.14158

# 3. Declare classes. Keep in mind that order matters. If a class A needs B,
#    then B must be declared first.
class Circle:
    def __init__(self):
        """
        Initialise useful properties for the Circle.
        """
        # Position
        self.x = 0.0
        self.y = 0.0

        self.radius = 5
        
        # Colour
        self.r = 1.0
        self.g = 1.0
        self.b = 1.0

        # Properties to draw a fancy loading bar
        self.bars = 0
        self.max_bars = 10
    
    def draw(self):
        """
        Draw the circle.
        """
        self.bars = self.bars % (self.max_bars+1)

        print(f'\rProgress {self.bars * 100/self.max_bars}% [', end='')

        for i in range(self.bars):
            print('=', end='')
        
        for i in range(self.max_bars - self.bars):
            print('.', end='')
        
        print(']', end='', flush=True)

        self.bars += 1

# 4. Declare functions. Order also matters here.
def compute_radius(circle: Circle) -> float:
    """Implement this function."""

# 5. There is no main function in Python. You can decide to write one, but
#    for the purpose of this tutorial we will leave it out.
#
# When we draw something on the screen, we put it in a while-loop so the
# application does not after the first frame.
my_circle = Circle()
print(f'The radius of a circle with radius {my_circle.radius} = {compute_radius(my_circle)}')

# Draw the circle
print('Placeholder for drawing a circle. We create a fancy loading bar.')
print('Press CTRL+C to cancel.')

is_closing = False
try:
    while(not is_closing):
        my_circle.draw()

        sleep(0.5)
except KeyboardInterrupt:
    print("\n\nLoading animation was cancelled\n")
    pass

# 6. Execute the code
"""
To execute the code on the CLI, use the following command (make sure you are in
a virtual environment):

python 02_python_script.py

If this does not work, then make sure you are in the directory where this script
is in

cd path/to/parent_directory

To execute the code in Visual Studio Code's GUI, hit the play button in the top
right corner of the window. It has the shape of a triangle. You can press the
menu button next to the play button to see other available options.
"""

# 7. Debug the code
"""
Debugging in Visual Studio Code is very easy. Let us first create a breakpoint
on the line below by hovering the mouse cursor to the left side of the line number.
A red circle appears. Click on it to set a breakpoint. Then, open the menu next
to the play button and select 'Python Debugger: Debug Python File'.

The debugger will execute the code as normal.
"""

# Cancel the animation with Ctrl+C.
area = my_circle.radius**2 * PI

"""
You have hit the breakpoint! On the left side of the window, you will see the
debugging panel. You will not see the variable 'area' unless the interpreter
has evaluated the expression, so press 'Step Over' in the top middle of the
window. This will go to the next line of code in the current file.

What is the value of the variable `area`?

You will encounter situations where you try to compute some expressions, but
there are some logic errors in your code. We hope the debugger will help you
solve these errors. The code may also throw exceptions. When this happens,
the debugger will pinpoint exactly where the code crashes.
"""

# Feel free to play around with the values in this file, or even better write
# your very own script! At this point, the basics are covered. We will use more
# features and techniques in the course, and you will learn more about these
# as they are required.

# If you are ready for the next step, head over to 03_numpy.py.
