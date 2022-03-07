import math
from graphics import *
#Create a function to calculate perimeter
def square(x):
        return x**2

def distance(p1,p2):
        dist = math.sqrt(square*(p2.getX() - p1.getX())
                    + square*(p2.getY() - p1.getY()))
        return dist

#Create a function to calculate area
def triangleArea(a, b, c):
	s = (a + b + c)/2
	A = math.sqrt(s*(s - a)*(s - b)*(s - c))
	return A

def main():
        win = GraphWin("Draw a Triangle")
        win.setCoords(0.0, 0.0, 10.0, 10.0)
        message = Text(Point(5, .05), "Click on three points")
        message.draw(win)
        message2 = Text(Point(10, .05))
        message2.draw(win)
        #Get and draw three verticies of triangle
        p1 = win.getMouse()
        p1.draw(win)
        p2 = win.getMouse()
        p2.draw(win)
        p3 = win.getMouse()
        p3.draw(win)
	
	#Use Polygon object to draw the triangle
	triangle = Polygon(p1,p2,p3)
	triangle.setFill("peachpuff")
	triangle.setOutline("cyan")
	triangle.draw(win)
	
	#Calculate the perimeter of the triangle
	perim = distance(p1,p2) + distance(p2,p3) + distance(p3, p1)
	message.setText("The perimeter is: {0:0.2f}".format(perim))
	
	#Calculate the area of the triangle
	triangleArea(distance(p1,p2), distance(p2,p3), distance(p3,p1))
	message2.setText("The area is: {0:0.2f}".format(A))
