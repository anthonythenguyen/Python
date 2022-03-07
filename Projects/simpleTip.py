"""
Name: Anthony Nguyen
Course: cs1400
Section: 002
Project 1 - Tip Calculator

This is a console application that helps auser calculate a range of tips and
total cost for a meal. When the user enters a value in dollars and cents,
your program will calculate three possibletip amounts as described below.

1) For excellent service calculate a tip that is 20% of the cost of the meal
2) For average service calculate a tip that is 15% of the cost of the meal
3) For poor service calculate a tip that is 10% of the cost of the meal
"""
def main():
	#Get the cost of the meal
	mealPrice = eval(input("The cost of the meal was: "))

	#Calculate tips
	excellentTip = mealPrice * .20
	averageTip = mealPrice * .15
	poorTip = mealPrice * .10

	#Output results
	print("The cost of the meal is: ", '${:,.2f}'.format(mealPrice))
	print()
	print("Poor Service Tip:\t", '${:,.2f}'.format(mealPrice),
	      " for a total cost of", '${:,.2f}'.format(mealPrice + poorTip))
	print("Average Service Tip:\t", '${:,.2f}'.format(mealPrice),
	      " for a total cost of", '${:,.2f}'.format(mealPrice + averageTip))
	print("Excellent Service Tip:\t", '${:,.2f}'.format(mealPrice),
	      " for a total cost of", '${:,.2f}'.format(mealPrice + excellentTip))

"""
The hardest part about this was finding out how to format the price so that it
        shows the dollar sign and the cents.
Making the function display the correct numbers in an orderly manner was
        new and tricky at first.
Figuring out how to turn this project in on a MacBook was the hardest part.
"""
