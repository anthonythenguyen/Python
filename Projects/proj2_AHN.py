"""
Anthony Nguyen
CS1400
Programming Project 2
Due September 23
No help
Create a house using 5 clicks from the user
"""
from math import *
from graphics import *
def main():
    #Inform user what to do
    print("We are going to create a house using 5 mouse clicks")
    print("First click will be the lower-left corner of the house")
    print("Second click will be the upper-right corner of the house")
    print("Third click will be the top center of the door")
    print("Fourth click will be the center of the window")
    print("Fifth click will be the roof's center")
    #Create window
    win = GraphWin("house", 400,400)
    #Take the first click's x and y coordinates, Lower-left corner of the house
    firstClick = win.getMouse()
    x1 = firstClick.getX()
    y1 = firstClick.getY()
    firstClickPoint = Point(x1,y1)

    #Take the second click's x and y coordinates, Upper-right corner of the house
    secondClick = win.getMouse()
    x2 = secondClick.getX()
    y2 = secondClick.getY()
    secondClickPoint = Point(x2,y2)

    #Take the third click's x and y coordinates, Top center of the door
    thirdClick = win.getMouse()
    x3 = thirdClick.getX()
    y3 = thirdClick.getY()
    thirdClickPoint = Point(x3,y3)

    #Take the fourth click's x and y coordinates, Center of the window
    fourthClick = win.getMouse()
    x4 = fourthClick.getX()
    y4 = fourthClick.getY()
    fourthClickPoint = Point(x4,y4)

    #Take the fifth click's x and y coordinates, Peak of the roof
    fifthClick = win.getMouse()
    x5 = fifthClick.getX()
    y5 = fifthClick.getY()
    fifthClickPoint = Point(x5,y5)

    #Use the first two point to create the main part of the house
    #Create a rectangle
    mainHouse = Rectangle(firstClickPoint, secondClickPoint)
    mainHouse.setOutline("red")
    mainHouse.setFill("red")
    mainHouse.draw(win)
    widthLine = dist = sqrt( (x2 - x1)**2)
    houseWidthDoor = 1/10*widthLine
    houseWidthWindow = 1/20*widthLine
    
    #Use the third click to create the door
    #Add 1/10 of the house's width to each side and bring it down to the y1
    houseDoorCenter1 = win.plot(x3, y3, "black")
    houseDoor = Rectangle(Point(x3-houseWidthDoor,y1), Point(x3+houseWidthDoor,y3))
    houseDoor.setFill("black")
    houseDoor.draw(win)

    #Use the fourth click to create the window
    #Create a rectangle with the center point and 1/20 of the house width to each side
    window = Rectangle(Point(x4-houseWidthWindow, y4-houseWidthWindow),
                       Point(x4+houseWidthWindow, y4+houseWidthWindow))
    window.setOutline("grey")
    window.setFill("grey")
    window.draw(win)
    
    #Use the fifth click to create the roof
    #Use Polygon
    roof = Polygon(secondClickPoint, fifthClickPoint, Point(x1, y2))
    roof.setOutline("brown")
    roof.setFill("brown")
    roof.draw(win)
    
