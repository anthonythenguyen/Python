"""
Anthony Nguyen
CS1400
Bowling Team
Due on 12/8/2018

People who helped me:
Cory from class
My roommate who knows C#

At the end of each game, the program asks you to record the scores for each team member. You type in their first name and that person's score for the game on a single line.
When there are no more players to input, enter an empty line.
Your program should now print the following lists in columns:
the names and scores of each bowler in the order entered
the names and scores in descending order with high scorer at the top
the names and scores in alphabetical order
If anyone scores a perfect game, put an asterisk in front of their name.
Next, your program should display the following summary information:
Display a congratulatory message showing the high score and who got it.
 Display a sympathetic message showing the low score and who got it.
The team average score, rounded down to the nearest pin.
Last, your program should write each of the lists and the summary information to a text file called game_results.txt in the same format it is displayed on the screen.
You must write your own search and sort routines--do not use built-in Python sorts or libraries.

1) Create a list to hold bowler information
2) Create Bowler class to hold score and name
3) Take input from user
4) Print data as given
5) Print data in Alphabetical Order
6) Print data in Highest to Lowest
7) Print out the highest score, lowest score and average
8) Save data to a .txt file

I learned that we should be thankful for the search/sort routines because they are a pain to make
I learned that if we do a double assignment from eval input, we can split up the user inputs and store it
I learned that if we set up the code to print out a certain way, it will take a lot of work to try and change how
    it prints out
I learned that
"""


    #Create Bowler class to hold score and name
class BowlingData:
    #This class is to create bowler data, so that each bowler will be an object
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
def GetInput():
    #Function that gets user inputs for name and score for each bowler
    #Turns the names into strings and the scores into integers
    #Try and except to make sure that the inputs are valid
    #Returns the bowlers
    
    #Create the list
    bowlers = []
    
    #Input data and test to make sure it is correct
    while True:
        try:
            line = input("Enter the name and score for each player split with a space ")
            if line == "":
                break;
            
            name, score = line.split(' ')
            bowlers.append(BowlingData(name, int(score)))            
        except:
            #If incorrect catch and display invalid entry
            print("Invalid entry, try again...")

    return bowlers


def scoreSort(bowlers):
    #Sort the data numerically and output list scoreOrder to be printed
    #Returns a list with the scores in order from greatest to least

    #Create the list
    scoreOrder = []
    n = len(bowlers)
    for i in range(n):
        scoreOrder.append(bowlers[i])


    #Iterate and sort through the list numerically
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1,n):
           if scoreOrder[i].score > scoreOrder[mp].score:
               mp = 1
               if int(scoreOrder[i].score) > int(299):
                   scoreOrder[i].name = "*" + scoreOrder[i].name
        scoreOrder[bottom], scoreOrder[mp] = scoreOrder[mp], scoreOrder[bottom]
                   

    return scoreOrder


def sortName(bowlers):
    #Sort the data alphabetically and output list alphaOrder to be printed
    #Returns a list with the scores in alphabetical order

    #Create list
    alphaOrder = []
    n = len(bowlers)
    for i in range(n):
        alphaOrder.append(bowlers[i])

    #Iterate and sort through the list
    for bottom in range(n-1):
        mp = bottom
        h = 0
        for i in range(bottom+1,n):
            while int(ord(alphaOrder[i].name[h].upper())) == int(ord(alphaOrder[mp].name[h].upper())):
                h = h + 1
            if int(ord(alphaOrder[i].name[h].upper())) < int(ord(alphaOrder[mp].name[h].upper())):
                mp = i
                h = 0
        alphaOrder[bottom], alphaOrder[mp] = alphaOrder[mp], alphaOrder[bottom]

    return alphaOrder



def CalculateAverage(bowlers):
    #Calculate average from the bowling scores that were inputed and output average
    #Returns the average score

    numbers = []
    n = len(bowlers)

    for i in range(n):
        numbers.append(bowlers[i].score)
    #Calculate the average based on the informsation that has been input
    total = 0
    for i in range(n):
        total = total + int(numbers[i])
    average = total // n

    return average


def printData(average, alphaOrder, scoreOrder, bowlers):
    #Function to print data taking inputs from all the other functions and printing them out in the correct format
    #Also prints thr congratulatory and sadness messages

    n = len(bowlers)
    print()
    print("Normal Sort\talphabet sort\tnumber sort")
    print("Name\tscore\tName\tScore\tName\tScore")
    
    for i in range(n):
    #Iterate through the list and print from object
        print(bowlers[i].name,
              "\t", bowlers[i].score,
              "\t", alphaOrder[i].name,
              "\t", alphaOrder[i].score,
              "\t", scoreOrder[i].name,
              "\t", scoreOrder[i].score)
    #Print other statements
    print()
    print("Congratulations", scoreOrder[0].name, "you got the highest score")
    print("Better luck next time", scoreOrder[n-1].name, "you received the lowest score")
    print("The average of the scores is", average)


def writeData(average, alphaOrder, scoreOrder, bowlers):
    #Function that is designed to write the txt info to a .txt file

    n = len(bowlers)
    data = []
    newLine = '\n'
    tab = '\t'
    norm = 'Normal order'
    aOrder = 'Alpha order'
    sOrder = 'Score order'
    
    f = open('game_results.txt', 'w+')
    for i in range(n):
    #Iterate through the list and input the data and info into the .txt file
        data.append(
            '{:10}'.format(bowlers[i].name)+
            '{:10}'.format(bowlers[i].score))
        data.append(tab)
        data.append(
            '{:10}'.format(alphaOrder[i].name)+
            '{:10}'.format(alphaOrder[i].score))
        data.append(tab)
        data.append(
            '{:10}'.format(scoreOrder[i].name)+
            '{:10}'.format(scoreOrder[i].score))
        data.append(newLine)
    f.writelines(norm+tab+tab+aOrder+tab+tab+sOrder+newLine)
    f.writelines(data)
    f.close()
              
              


                               
        

def main():

    #Call input function and assign it to bowlers
    bowlers = GetInput()

    #Call all the other previous funcitions and assign them variable values
    scoreAverage = CalculateAverage(bowlers)
    orderName = sortName(bowlers)
    scoreOrder = scoreSort(bowlers)

    #Print the information from input data that was received into the shell and output the info to the .txt file
    printData(scoreAverage, orderName, scoreOrder, bowlers)
    writeData(scoreAverage, orderName, scoreOrder, bowlers)


              



            
            





main()
