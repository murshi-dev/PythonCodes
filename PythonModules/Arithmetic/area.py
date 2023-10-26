'''Create area.py and call the relevant functions to calculate
the area of a rectangle.'''
import mathOperations
#get inputs
length=float(input("Enter the length of rectangle: "))
width=float(input("Enter the width of rectangle: "))
#call the functions in mathoperations.py to calculate area
areaRect = mathOperations.multiply(length,width)
#print result
print("Area of Rectangle: ",areaRect)
