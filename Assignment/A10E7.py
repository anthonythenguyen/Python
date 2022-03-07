from graphics import *
from random import randrange

class Button:
	def __init__(self, win, center, width, height, label):
		""" Creates a rectanglular button eg:
		qb = Button(myWin, centerPoint, width, height, 'Quit')"""

		w,h = width/2.0, height/2.0

		x,y = center.getX(), center.getY()
		self.xmax, self.xmin = x+w, x-w
		self.ymax, self.ymin = y+h, y-h
		p1 = Point(self.xmin, self.ymin)
		p2 = Point(self.xmax, self.ymax)
		self.rect = Rectangle(p1, p2)
		self.rect.setFill('lightgrey')
		self.rect.draw(win)
		self.label = Text(center, label)
		self.label.draw(win)
		self.deactivate()
	def clicked(self, p):
		return(self.active and
		       self.xmin <= p.getX() <= self.xmax and
		       self.ymin <= p.getY() <= self.ymax)
	def getLabel(self):
		return self.label.getText()
	def activate(self):
		self.label.setFill('black')
		self.rect.setWidth(2)
		self.active = True
	def deactivate(self):
		self.label.setFill('darkgrey')
		self.rect.setWidth(1)
		self.active = False
def main():
	win = GraphWin("Button Maker", 800, 800)
	b1 = Button(win, Point(200,400), 150, 150, "Door 1")
	b2 = Button(win, Point(400,400), 150, 150, "Door 2")
	b3 = Button(win, Point(600,400), 150, 150, "Door 3")
	b1.activate()
	b2.activate()
	b3.activate()

	prompt = Text(Point(300,600), "Click on a Door")
	prompt.draw(win)
	special = randrange(1,4)
	running = True
	userInput = 0

	while userInput == 0:
		pt = win.getMouse()
		
		if b1.clicked(pt):
			#print("Door 1 was clicked")
			userInput = 1
		if b2.clicked(pt):
			#print("Door 2 was clicked")
			userInput = 2
		if b3.clicked(pt):
			#print("Door 3 was clicked")
			userInput = 3
		
	if userInput == special:
		prompt.setText("You win!")
	else:
		prompt.setText("You lose! The correct door was Door "+str(special))

main()
