"""
Anthony Nguyen
CS1400
Farmer John
Oct 7, 11:59pm

No help
Draw the farm then compute the area of the shaded portion

1. Create a graphics surface
2. Get size of farm from user
3. Create the shaded area
4. Create the circles where their midpoints are the corners of the square
5. Recreate the outline of the square
6. Calculate the shaded area

I learned that if you forget the parenthesis in .getX(), it becomes a method(?)
    like, one of my errors said I could not mess with methods and floats.
Another thing I learned is that you have to pay close attention to where the
    center points of the circles are because if you do not they may end up
    swapped in other places.

"""

from graphics import *
from math import *

"""
    My funcation that draws a circle with givin inputs
    The variables are for x,y coordinates, the radius of the circle and where
    it is to be drawn
"""
def drawCircle(x, y, z, q):
    circle = Circle(Point(x, y), z)
    circle.setFill("white")
    circle.draw(q)

def circleArea(radius):
    circArea = pi*radius**2
    return circArea

def squareArea(length):
    squArea = length**2
    return squArea

def main():
    #Create the graphics window
    win = GraphWin("Farmer John", 800, 800)

    #Take length input from user
    try:
        length = eval(input("Input a length: "))
        midPoint = Point(400, 400)

        #Shaded rectangle
        shadedRectangle = Rectangle(Point(midPoint.getX() - length / 2,
                                          midPoint.getY() + length / 2),
                                    Point(midPoint.getX() + length / 2,
                                          midPoint.getY() - length / 2))
        shadedRectangle.setFill("grey")
        shadedRectangle.draw(win)

        #Use the drawCircle function to create Circle A
        drawCircle(midPoint.getX()-length/2, midPoint.getY()-length/2,
                   length/2, win)
        circleA = Text(Point(midPoint.getX()-length/2 - 20,
                             midPoint.getY()-length/2),
                       "A")
        circleA.draw(win)
        #Use the drawCircle function to create Circle B
        drawCircle(midPoint.getX()+length/2, midPoint.getY()-length/2,
                   length/2, win)
        circleB = Text(Point(midPoint.getX()+length/2 + 20,
                             midPoint.getY()-length/2),
                        "B")
        circleB.draw(win)
        #Use the drawCircle function to create Circle C
        drawCircle(midPoint.getX()+length/2, midPoint.getY()+length/2,
                   length/2, win)
        circleC = Text(Point(midPoint.getX()+length/2 + 20,
                             midPoint.getY()+length/2),
                        "C")
        circleC.draw(win)
        #Use the drawCircle function to create Circle D
        drawCircle(midPoint.getX()-length/2, midPoint.getY()+length/2,
                   length/2, win)
        circleD = Text(Point(midPoint.getX()-length/2 - 20,
                             midPoint.getY()+length/2),
                        "D")
        circleD.draw(win)

        #Outline rectangle, a copy of the shadedRectangle
        outlineRectangle = Rectangle(Point(midPoint.getX() - length / 2,
                                          midPoint.getY() + length / 2),
                                    Point(midPoint.getX() + length / 2,
                                          midPoint.getY() - length / 2))
        outlineRectangle.draw(win)

        print("The area of the shaded area is",
              '{:,.2f}'.format(squareArea(length) - circleArea(length/2)),
              "feet.")
    except:
        print("An invalid length was given")
        win.close()
        
main()
