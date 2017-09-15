# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-10: Mover class

from p5 import *

class Mover(object):

	def __init__(self):
		# The mover tracks location, velocity and acceleration
		# Start in the center
		self.position = Vector(width/2, height/2)
		self.velocity = Vector(0,0)
		# The Mover's maximum speed
		self.topspeed = 5

	def update(self):
		# Compute a vector that points from position to mouse
		self.mouse = Vector(mouse_x, mouse_y)
		self.acceleration = self.mouse - self.position

		# Set magnitude of acceleration
		self.acceleration.magnitude = .2

		# Velocity changes according to acceleration
		self.velocity += self.acceleration

		# Limit the velocity by topspeed
		self.velocity.limit(self.topspeed)

		# Position changes by velocity
		self.position += self.velocity

	def display(self):
		stroke(0)
		#stroke_weight(2)
		fill(127)
		ellipse((self.position.x, self.position.y), 48, 48)
