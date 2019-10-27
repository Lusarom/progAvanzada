#Exercise 40: Name that Triangle

#A triangle can be classified based on the lengths of its sides as equilateral, isosceles
#or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
#triangle has two sides that are the same length, and a third side that is a different
#length. If all of the sides have different lengths then the triangle is scalene.

#Write a program that reads the lengths of 3 sides of a triangle from the user.
#Display a message indicating the type of the triang


print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print('Scalene triangle")
