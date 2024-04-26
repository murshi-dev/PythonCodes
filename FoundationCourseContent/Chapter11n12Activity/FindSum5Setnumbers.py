'''Calculate the sum of two numbers.
Repeat the code to check the sum for 5 sets of numbers.
Write Pseudocode, draw flow chart and python code using while loop.
'''
counter=1
while(counter<=5):
    print("Set ",counter)
    n1=int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    sum=n1+n2
    print("Sum of ",n1," and ",n2," is: ",sum)
    counter=counter+1
