'''Calculate the sum of two numbers.
Repeat the code to check sum based on user option to continue.
Write Pseudocode, draw flow chart and python code using while loop.
'''
option='y'
while(option == 'y' or option == 'Y'):
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    sum=n1+n2
    print("Sum of ",n1," and ",n2," is: ",sum)
    option=input("Continue(Y/N): ")