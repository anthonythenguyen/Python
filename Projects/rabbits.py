"""
Anthony Nguyen
CS1400
Rabbits, Rabbits, Rabbits!
Oct 21, 11:59pm

Worked with Cory

Suppose that a scientist is doing some important research work
    that requires her to use rabbits in her experiments.
She starts out with one pair of adult rabbits (a male and a female).
At the end of each month, a pair of rabbits produces one pair of offspring
    (a male and a female).
However, these new offspring will not be able to reproduce until
    they are a month old, and won't have babies of their own until
    the following month.

1) Print a table that contains the following information for
        the beginning of each month.
    The number of months that have passed.
    The number adult rabbit pairs (those over 1 month old).
    The number of baby rabbits pairs produced this month.
    The total number of rabbit pairs in the lab.
2) Calculate how many months it will take until the number of rabbits
        exceeds the number of available cages.
3) Stop printing when you run out of cages.
4) Print a message giving how many months it will
        take to run out of cages

I learned about Fibonacci sequences, and patterns for easy math
"""

def main():
    #\t creates a tabbed-space
    print("Month\tAdult\tBabies\tTotal")
    
    month = 1
    adults = 1
    babies = 0
    total = 1

    print(month, "\t", adults, "\t", babies, "\t", total)
    
    while total <= 500:
        #Update totals for new month
        previousAdults = adults
        previousBabies = babies
        previousTotal = total
        month = month + 1
        adults = previousTotal
        babies = previousAdults
        total = babies + adults
        print(month, "\t", adults, "\t", babies, "\t", total)
        #month, babies, adults = month +1, adults, total
        #total = babies + adults
    print("Cages will urn out in month", str(month) + ".")
    
main()
