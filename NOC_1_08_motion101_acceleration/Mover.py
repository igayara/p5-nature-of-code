# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Example 1-8: Mover class

from p5 import *

class Mover(object):

	def __init__(self):
		self.position = Vector(width/2, height/2)
		self.velocity = Vector(0,0)
		self.acceleration = Vector(-0.001, 0.01)
		self.topspeed = 10

	def update(self):
		self.velocity += self.acceleration
		self.velocity.limit(self.topspeed)
		self.position += self.velocity

	def display(self):
		stroke(0)
		#stroke_weight(2)
		fill(127)
		ellipse((self.position.x, self.position.y), 48, 48)

	def check_edges(self):
		if self.position.x > width :
			self.position.x = 0
		elif self.position.x < 0 :
			self.position.x = width

		if self.position.y > height :
			self.position.y = 0
		elif self.position.y < 0 :
			self.position.y = height
