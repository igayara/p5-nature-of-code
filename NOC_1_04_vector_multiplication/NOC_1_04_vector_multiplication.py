# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-4: Vector multiplication

from p5 import *

def setup():
	size(640,360)
	#smooth()

def draw():
	background(255)

	mouse = Vector(mouse_x, mouse_y)
	center = Vector(width/2, height/2)
	mouse = mouse - center

	# Multiplying a vector! 
	# The vector is now half its original size (multiplied by .5)
	mouse = mouse * 0.5

	translate(width/2, height/2)
	#stroke_weight(2)
	stroke(0)
	line((0,0),(mouse.x, mouse.y))


run()