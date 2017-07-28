#PONG pygame

import random
import numpy as np
import math
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()
boids = []
#colors
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
LIGHT_RED = (255,155,155)
GREEN = (0,255,0)
BLACK = (0,0,0)
YELLOW = (255,255,0)

#canvas declaration
screen_width=800
screen_height=800
window = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption('Boids')

blue_goal = [float(screen_width), 0.0]
red_goal = [0.0, float(screen_height)]

blue_base = [0,screen_height]
red_base = [screen_width,0]

#field declaration
base_size = 200
lane_width = 100

def normalize(a):
	return a / np.linalg.norm(a)

def dist(a,b):
	return np.linalg.norm(a-b)

def drawField(canvas):
	canvas.fill(GREEN)
	#lanes
	pygame.draw.line(canvas, YELLOW, [0, screen_height],[screen_width, 0], lane_width) #center
	pygame.draw.line(canvas, YELLOW, [0, 0],[screen_width, 0], lane_width)#upper
	pygame.draw.line(canvas, YELLOW, [0, 0],[0, screen_height], lane_width)#upper
	pygame.draw.line(canvas, YELLOW, [0, screen_height],[screen_width, screen_height], lane_width)#bottom
	pygame.draw.line(canvas, YELLOW, [screen_width, 0],[screen_width, screen_height], lane_width)#bottom

	#base
	pygame.draw.circle(canvas, BLUE, blue_base, base_size, 0)
	pygame.draw.circle(canvas, RED, red_base, base_size, 0)

class Boid:
	'''def __init__(self, x, y, goal, radius = 3):
		self.position = np.array([x, y])
		self.radius = radius
		self.speed = np.array([(random.random()-0.5)*10,(random.random()-0.5)])
		self.max_speed = 1 #this is arbitrary
		self.neighborhood_range = 200 #arbitrary
		self.goal = goal;'''

	def __init__(self, position, goal, radius = 3):
		self.position = position
		self.radius = radius
		self.speed = np.array([0,0])
		self.max_speed = 1 #this is arbitrary
		self.neighborhood_range = 50 #arbitrary
		self.goal = goal;

	def wrap(self):
		if(self.position[0] > screen_width): 
			self.position[0] = 0
		elif(self.position[0] < 0):
			self.position[0] = screen_width

		if(self.position[1] > screen_height):
			self.position[1] = 0
		elif self.position[1] < 0:
			self.position[1] = screen_height


	def draw(self, canvas):
		pygame.draw.circle(canvas, LIGHT_RED, [math.ceil(self.position[0]),math.ceil(self.position[1])], self.radius, 0)
		pygame.draw.circle(canvas, WHITE, [math.ceil(self.position[0]),math.ceil(self.position[1])], self.neighborhood_range, 1)
		#self.wrap()

		#target = np.array(pygame.mouse.get_pos())
		#print(pos, len(pos))
		'''target = np.array([0.0,0.0])
		for i in boids:
			if not(dist(target, i.position) > self.neighborhood_range): target += i.position
		target = target/len(target)'''

		#update position according to speed
		self.position += self.speed
		self.speed = normalize(self.goal - self.position) * self.max_speed
		#self.speed = normalize(self.goal - self.position) * self.max_speed


def draw(canvas):
	drawField(canvas)
	for x in boids:
		x.draw(canvas)
	#pygame.draw.circle(canvas, WHITE, [100,100], 70, 1)
	
	
def init():
	for x in range(1,10):
		boids.append(Boid(blue_goal, red_goal))
		print(boids[x-1].position)

init()


#game loop
while True:

	draw(window)

	for event in pygame.event.get():

		if event.type == KEYDOWN:
			keydown(event)
		elif event.type == KEYUP:
			keyup(event)
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	pygame.display.update()
	fps.tick(300000)