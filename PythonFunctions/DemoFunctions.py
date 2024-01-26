#to add two numbers, to subtract two numbers
#get user input using functions

#define a function
def getUserInput():
    num1=int(input("Input first number: "))
    num2=int(input("Input second number: "))
    return num1,num2

#define a function for addition
def addNumbers(x,y):
    result=x+y
    return result

#define a function for subtraction
def subNumbers(a,b):
    result=a-b
    return result

#function call to get input
num1,num2=getUserInput()
#function call to add
addedValue = addNumbers(num1,num2)
print("Added value is: ",addedValue)

#function call to get input
num1,num2=getUserInput()
#function call to subtract
subtractedValue = subNumbers(num1,num2)
print("Subtracted value is: ",subtractedValue)
