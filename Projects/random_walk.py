"""
Name: Anthony Nguyen
Course: cs1400
Project 5 - Random Walk
Due Date: Nov 11, 2017

My roommate (Brenden Bunker) helped me with scaling because I over thought it


Create a program that is to take a user input on how many steps are taken
in a "random" direction with each step and to draw it.

I learned
1) How to scale things in a simple manner
2) A distance formula is very useful
3) As my testing design, I just made sure everything ran properly after
    creating it

My Steps:
1) Created a graphics window
2) Created my variables
3) Created my for loop
4) Print the required information
"""

from graphics import *
from math import *
from random import random
            
def main():
    #Create a scale so it looks nicer
    #scale = 1 is 100 by 100
    scale = 8
    #Create graph window
    win = GraphWin("Random Walk", 100*scale, 100*scale)
    #Set (0,0) to the middle of the graph window
    win.setCoords(-50*scale, -50*scale, 50*scale, 50*scale)
    #Amount of steps as input
 
    needUserInput  = True
    while needUserInput:
        try:
            n = eval(input("How many steps would you like to take?: "))
            if n<=0:
                print("Please input a postive Int!")
            else:
                needUserInput = False
        except:
                print("Please input a number.")
    #Create perso( who will do the walking
    person = Point(0,0)
    person.draw(win)
    oldPoint = person
    x = 0
    y = 0
    angle = 0
    #Loops the following things n amount of times where n is the user input
    for i in range(n):
        direction = Direction(scale)
        person = Line(oldPoint, Point(oldPoint.x + direction.x,
                                      oldPoint.y + direction.y))
        person.draw(win)
        oldPoint = Point(oldPoint.x + direction.x,
                                      oldPoint.y + direction.y)
    print("Total Distance from Center:", sqrt((oldPoint.x**2)+(oldPoint.y**2))/scale)
    print("Total Distance Traveled:", n)

#Class to do my direction    
class Direction():
    def __init__(self, scale):
            self.angle = random() * 2 * pi
            self.x = cos(self.angle)*scale
            self.y = sin(self.angle)*scale
        
main()
