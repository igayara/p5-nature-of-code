# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-1: Bouncing Ball, no vectors

from p5 import *

x = 100
y = 100
xspeed = 2
yspeed = 2.5

def setup():
	size(800, 200)
	#smooth()

def draw():
	background(255)

	# Add the current speed to the position.
	global x, y, xspeed, yspeed
	x = x + xspeed
	y = y + yspeed

	if (x > width) or (x < 0):
		xspeed = xspeed * -1

	if (y > height)	or (y < 0):
		yspeed = yspeed * -1

	#Display circle at x position
	stroke(0)
	#stroke_weight(2)
	fill(127)
	circle((x, y), 48)

run()