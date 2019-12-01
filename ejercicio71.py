from math import sqrt  #Imported the square root function from math module
from math import pow     #Imported the power function from math module
 
a=int(input("Enter the measure of one side of a right angled triangle:"))    
b=int(input("Enter the measure of another side of a right angled triangle:"))    
#input function is used to take input from user and is stored as string
# which is then typecasted into an integer using the int() function.
c=sqrt(pow(a,2)+pow(b,2))       #we have implemented the formula c=√(a2+b2)
print(f"The measure of the hypotenuse is: {c} based on the measures of the other two sides {a} & {b}")      
