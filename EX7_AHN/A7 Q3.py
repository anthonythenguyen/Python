def main():
	age = eval(input("Enter your age: "))
	citizenYrs = eval(input("Enter how many years you were a citizen: "))
	if age >= 30 and citizenYrs >= 9:
		print("You can run for Senate and House")
	elif age >= 25 and citizenYrs >= 7:
		print("You can run for House but not Senate")


main()
