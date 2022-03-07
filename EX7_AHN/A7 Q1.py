def main():
	a, b, c = eval(input("Enter three numbers: "))
	if a > b:
		if b > c:
			print("Spawm Please!")
		else:
			print("It's a late parrot!")
	elif b > c:
		print("Cheese SHoppe")
		if a >= c:
			print("Cheddar")
		elif a < b:
			print("Gouda")
		elif a == b:
			print("Swiss")
	else:
		print("Trees")
		if a == b:
			print("Chestnut")
		else:
			print("Larch")
	print("Done")


main()
