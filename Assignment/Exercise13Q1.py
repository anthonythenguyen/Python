from random import *

def search(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            # item found, return the index value
            return i
        else:
            # loop finished, item was not in list
            return -1
def main():
    fixedPrecision = 2
    numList = []
    number = randint(0,500)
    for a in range(250000):
        numList.append(randint(0,500))
    find = search(number, numList)
    if find == -1:
        print("I did not find the number", number)
    else:
        print("I found the number", number)

main()
