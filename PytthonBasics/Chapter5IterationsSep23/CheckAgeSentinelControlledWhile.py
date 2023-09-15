'''Input age from user. Display “You are an adult” if the age is greater than 18, otherwise display “You are not an adult”.
Check if the entered age is a positive number. Display error otherwise.
Repeat until the user wishes to exit.
'''
#1.initial value
option='y'
#2.condition
while(option == 'y'):
    age = int(input("Enter the age: "))
    if (age < 0):
        print("Enter positive number only!")
    elif (age > 18):
        print("Adult")
    else:
        print("Not Adult")
    #3.get option from user
    option=input("Continue (y/n): ")
