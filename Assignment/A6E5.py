from math import *
def main():
	#Area of a sphere
	def sphereArea(radius):
		A = 4*pi*radius**2
		return A
	#Volume of a sphere
	def sphereVolume(radius):
		V = (4/3)*pi*radius**3
		return V
	#Use the functios with user inputs
	radius = eval(input("Input the radius of the sphere: "))
	print("The area of a sphere with a radius of", radius, "is",
	      sphereArea(radius))
	print("The volume of a sphere with a radius of", radius, "is",
	      sphereVolume(radius))


