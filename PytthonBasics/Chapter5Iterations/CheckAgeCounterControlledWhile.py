'''Input age from user. Display “You are an adult” if the age is greater than 18, otherwise display “You are not an adult”.
Check if the entered age is a positive number. Display error otherwise.
Repeat the code to check age of three people.
'''

#1.initial value
counter=1
#2. condition
while(counter<=3):
    age=int(input("Enter the age: "))
    if(age<0):
        print("Enter positive number only!")
    elif(age>18):
        print("Adult")
    else:
        print("Not Adult")
    #3.update/increment counter
    counter=counter + 1