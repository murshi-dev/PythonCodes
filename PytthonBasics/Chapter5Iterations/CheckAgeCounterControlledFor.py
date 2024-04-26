'''Input age from user. Display “You are an adult” if the age is greater than 18, otherwise display “You are not an adult”.
Check if the entered age is a positive number. Display error otherwise.
Repeat the code to check age of three people.
'''
for counter in range(1, 4):
    # values from 1 to 4 but not including 4
    age = int(input("Enter the age: "))
    if (age < 0):
        print("Enter positive number only!")
    elif (age > 18):
        print("Adult")
    else:
        print("Not Adult")
