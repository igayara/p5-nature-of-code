# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-2: Bouncing Ball, with vectors

from p5 import *

def setup():
	size(200,200)
	background(255)
	global position, velocity
	position = Vector(100,100)
	velocity = Vector(2.5, 5)

def draw():
	no_stroke()
	fill(255, 10)	
	rect((0,0), width, height)

	# Add the current speed to the position.
	global position, velocity
	
	position = position + velocity
	
	if (position.x > width) or (position.x < 0):
		velocity.x = velocity.x * -1

	if (position.y > height) or (position.y < 0):
		velocity.y = velocity.y * -1

	# Display circle at x position
	stroke(0)
	fill(175)
	ellipse((position.x, position.y), 16, 16)

run()