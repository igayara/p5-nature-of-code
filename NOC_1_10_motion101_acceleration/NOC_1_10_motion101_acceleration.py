# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-10: Motion 101 - Acceleration - Follow mouse

from p5 import *
from Mover import Mover

def setup():
	size(640,360)
	global mover
	mover = Mover()

def draw():
	background(255)

	mover.update()
	mover.display()

run()