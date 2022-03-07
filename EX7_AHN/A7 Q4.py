from graphics import *
from math import *
def main():
	# Create the window
	win = GraphWin("Intersecting", 500, 500)
	
	# Get inputs for the first circle
	firstXCircle = eval(input("Center point x1: "))
	firstYCircle = eval(input("Center point y1: "))
	firstCircleRadius = eval(input("Radius1: "))
	
	# Get inputs for the second circle
	secondXCircle = eval(input("Center point x2: "))
	secondYCircle = eval(input("Center point y2: "))
	secondCircleRadius = eval(input("Radius2: "))
	
	# Use the inputs to create the circles:)
	firstCircle = Circle(Point(firstXCircle, firstYCircle), firstCircleRadius)
	secondCircle = Circle(Point(secondXCircle, secondYCircle), secondCircleRadius)
	firstCircle.setOutline("black")
	secondCircle.setOutline("black")
	firstCircle.draw(win)
	secondCircle.draw(win)
	
	# Do the thing for the collide dectection
	centerPointOne = firstCircle.getCenter()
	centerPointTwo = secondCircle.getCenter()
	# connectingLine = Line(centerPointOne, centerPointTwo)
	# connectingLine.draw(win)
	minDistanceLine = firstCircleRadius + secondCircleRadius
	connectingLineMidpoints = sqrt(((centerPointOne.x - centerPointTwo.x) * (centerPointOne.x - centerPointTwo.x))
				       + ((centerPointOne.y - centerPointTwo.y) * (centerPointOne.y - centerPointTwo.y)))
	if connectingLineMidpoints > minDistanceLine :
		print("No Collision")
	else:
		print("Yes Collision")


main()
