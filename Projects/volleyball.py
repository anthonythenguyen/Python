#rball.py

from random import *

def printIntro():
    print("this program simulates a game of volleyball between two players called a and b. The ability of each player is indicated by a probability( a number between")
    print("0 and1) that the player wins the point when serving.  Player A always has the first serve")

def getInputs():
    #returnes the 3 simulation parameters
    a = float(input("what is the probability player a wins the serve "))
    b = float(input("what is the probability that player b wins the serve "))
    n = int(input("How many games to simulate? "))
    return a,b,n

def simNGames(n, probA, probB):
    #simulates n games of raquetball between two players whose abilities are represented by the probability of winning a serve returns wins for a and b
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA+1
        else:
            winsB = winsB +1
    return winsA, winsB
"""
We commented out all the items from raquetball that we did not need in the volleyball code.
Because you do not need to check if serving matters, you can just say if A doesn't win the rally, B does.
"""
def simOneGame(probA, probB):
    #simulates one game of raquetball between two players whose abilities are represented by probability of winning a serve returns final score a and b
    serving = "A"
    scoreA = 0
    scoreB = 0

    while not gameOver(scoreA, scoreB):
        #if serving == "A":
            if random() < probA:
                scoreA = scoreA +1
            else:
                    #serving = "B"
                #if random() < probB:
                    scoreB = scoreB +1
                #else:
                    #serving = "A"
    return scoreA, scoreB

def gameOver(a,b):
    #a and b represent scores for a raquetball game.  return true if game is over, false otherwise.
    return a == 25 or b == 25

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("wins for A: {0} ({1:0.1%})". format(winsA, winsA/n))
    print("wins for B: {0} ({1:0.1%})". format(winsB, winsB/n))


              

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()
