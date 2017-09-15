# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-3: Vector subtraction

from p5 import *

def setup():
	size(640,360)

def draw():
	background(255)

	mouse = Vector(mouse_x, mouse_y)
	center = Vector(width/2, height/2)
	
	mouse = mouse - center

	translate(width/2, height/2)
	#stroke_weight(2)
	stroke(0)
	line((0,0),(mouse.x, mouse.y))

run()