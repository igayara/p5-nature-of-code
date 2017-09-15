# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-6: Vector normalize

from p5 import *

def setup():
	size(640,360)

def draw():
	background(255)

	# A vector that points to the mouse position
	mouse = Vector(mouse_x, mouse_y)

	# A vector that points to the center of the window
	center = Vector(width/2, height/2)

	# Subtract center from mouse which results in a vector that points from center to mouse
	mouse = mouse - center

	# Normalize the vector 
	mouse.normalize()

	# Multiply its length by 50
	mouse = mouse * 50

	# Draw the resulting vector
	translate(width/2, height/2)
	stroke(0)
	#stroke_weight(2)
	line((0,0), (mouse.x, mouse.y))

run()