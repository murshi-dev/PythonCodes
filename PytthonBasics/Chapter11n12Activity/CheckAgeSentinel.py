'''Input age from user. Display “You are an adult” if the age is greater than 18, otherwise display “You are not an adult”.
Check if the entered age is a positive number. Display error otherwise.
Repeat the code to check age based on user option to continue.
'''
#counter controlled loop - while,for
#sentinel controlled loop - while
option='y'
while(option=='y' or option=='Y'):
    age=int(input("Enter the age: "))
    if(age<0):
        print("Enter positive numbers only!")
    elif(age>18):
        print("Entered age ",age,"is ADULT")
    else:
        print("Entered age ", age, "is NOT ADULT")
    option=input("Continue(Y/N): ")