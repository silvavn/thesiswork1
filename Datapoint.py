from MyUtils import *

class Datapoint:
	def __init__(self, position, label=None):
		self.position = position
		self.label = label

	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self, position):
		self.__position = position

		if self.__position[0] < 0:
			self.__position[0] = 0
		elif self.__position[0] > canvas_width:
			self.__position[0] = canvas_width
		
		if self.__position[1] < 0:
			self.__position[1] = 0
		elif self.__position[1] > canvas_height:
			self.__position[1] = canvas_height
	
	def get_fill(self):
		colors = [GREEN,BLUE,YELLOW, WHITE, CYAN, MAGENTA, GRAY]
		try:
			return colors[self.label]
		except:
			return RED

	def draw(self, canvas):
		#print(self.position)
		canvas.create_oval(int(self.position[0])-datapoint_radius, 
			self.position[1]-datapoint_radius, 
			self.position[0]+datapoint_radius, 
			self.position[1]+datapoint_radius, 
			fill=self.get_fill())