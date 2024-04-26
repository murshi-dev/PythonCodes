'''Amy needs to design a simple calculator that performs addition
and subtraction of two numbers. Based on the entered option (addition or subtraction)
the program prompts for numbers, calculates the relevant arithmetic operation,
and displays the result. '''
#input the numbers
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
#display the option
print("Options:\n A. Addition\tS. Subtraction")
#input the option
option=input("Enter the option: ")
#check the option
if(option=='A'):
    sum=num1+num2
    print("Sum of ",num1," and ",num2," is:",sum)
else:
    difference=num1-num2
    print("Difference of ", num1, " and ", num2, " is:", difference)