def main():
	speedLimit = eval(input("Enter the speed limit: "))
	speed = eval(input("Enter a speed: "))
	if speed > speedLimit:
		speedingFine = 50 + (speed - speedLimit) * 5
		if speed > 90:
			speedingFine = speedingFine + 200
		print(speedingFine)
	else:
		print("Was not speeding!")


main()
