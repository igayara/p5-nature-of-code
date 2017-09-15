# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-11: Mover class

from p5 import *

class Mover(object):

	def __init__(self):
		# The mover tracks position, velocity and acceleration
		# Start at a random position
		self.position = Vector(random_uniform(width), random_uniform(height))
		self.velocity = Vector(0,0)
		# The Mover's maximum speed
		self.topspeed = 5

	def update(self):
		# Compute a vector that points from position to mouse
		self.mouse = Vector(mouse_x, mouse_y)
		self.acceleration = self.mouse - self.position

		# Set magnitude of acceleration
		#self.acceleration.magnitude = 0.2
		self.acceleration.normalize
		self.acceleration *= 0.2

		# Velocity changes according to acceleration
		self.velocity += self.acceleration

		# Limit the velocity by topspeed
		self.velocity.limit(self.topspeed)

		# Position changes by velocity
		self.position += self.velocity

	def display(self):
		stroke(0)
		#stroke_weight(2)
		fill(127, 200)
		ellipse((self.position.x, self.position.y), 48, 48)
