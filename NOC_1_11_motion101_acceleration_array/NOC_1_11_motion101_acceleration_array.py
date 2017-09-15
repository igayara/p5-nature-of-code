# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-11: Motion 101 - Acceleration - Array

# Demonstration of the basics of motion with vector.
# A "Mover" object stores position, velocity and acceleration as vectors.
# The motion is controlled by affecting the acceleration (in this case towards the mouse)

from p5 import *
from Mover import Mover

movers = []
mover_count = 20


def setup():
	size(640,360)
	for i in range(mover_count):
		movers.append(Mover()) 

def draw():
	background(255)
	for mover in movers:
		mover.update()
		mover.display()

run()