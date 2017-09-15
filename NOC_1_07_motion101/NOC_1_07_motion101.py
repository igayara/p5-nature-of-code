# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-7: Motion 101

from p5 import *
from Mover import Mover

def setup():
	size(640, 360)
	global mover
	mover = Mover()

def draw():
	background(255)

	mover.update()
	mover.check_edges()
	mover.display()

run()