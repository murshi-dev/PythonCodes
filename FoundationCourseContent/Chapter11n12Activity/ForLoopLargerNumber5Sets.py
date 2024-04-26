'''Input two numbers from user. Compare the two
 numbers and display the largest number among the both.
 Using logical operators check if the entered numbers
  are positive numbers. If the numbers are same display
  ‘same numbers entered’. Repeat the program for 5 sets
  of numbers. Write Pseudocode, draw flow chart and python
  code using for loop. '''
for counter in range(1,6):
    print("Set ",counter)
    n1=int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    if(n1<0 or n2<0):
        print("Enter positive numbers only!")
    elif(n1==n2):
        print("Entered numbers are same")
    elif(n1>n2):
        print(n1," is greater than ",n2)
    else:
        print(n2, " is greater than ", n1)