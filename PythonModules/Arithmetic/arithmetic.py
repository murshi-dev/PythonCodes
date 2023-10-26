'''Create arithmetic.py and call the relevant functions to add, subtract
and multiply two numbers.'''
#use the module to do calculations
import mathOperations

#input numbers
def getInput():
    n1=int(input("Enter first number: "))
    n2=int(input("Enter second number: "))
    return n1,n2

#call the functions in mathoperations.py
#addition
n1,n2=getInput()
add_result=mathOperations.add(n1,n2)
print("Added value: ",add_result)

#subtraction
n1,n2=getInput()
sub_result=mathOperations.subtract(n1,n2)
print("Subtract value: ",sub_result)

#multiplication
n1,n2=getInput()
mul_result=mathOperations.multiply(n1,n2)
print("Multiplied value: ",mul_result)