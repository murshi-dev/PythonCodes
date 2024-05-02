'''Input a number from user. Check and display
if the entered number is odd or even number.
Using logical operators check if the entered number
is positive numbers.'''
number=int(input("Enter any number: "))
if(number<0):
    print("Enter positive numbers only")
elif(number%2==0):
    print("Entered number is EVEN")
else:
    print("Entered number is ODD")