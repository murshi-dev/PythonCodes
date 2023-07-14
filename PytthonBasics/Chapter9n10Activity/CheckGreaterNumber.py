'''Input two numbers from user.
Compare the two numbers and display
the largest number among the both.
Using logical operators check if the
 entered numbers are positive numbers. if the
 entered numbers are same display the same'''
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
#if either of the numbers entered are negative
#display an error message - use logical operator here
if(n1<0 or n2<0):
    print("Enter positive numbers only")
elif(n1==n2):#use double equal sign here
    print("Entered numbers are same")
elif(n1>n2):
    print(n1," is larger than ",n2)
else:
    print(n2, " is larger than ", n1)





