#Input age from user. Display “You are an adult” if the age is greater than 18, otherwise display “You are not an adult”.
#Check if the entered age is a positive number. Display error otherwise.

age=int(input("Enter the age: "))
#condition 1
if(age<0):
    print("Enter positive number only!")
#condition 2
elif(age>18):
    print("Entered age ",age," is Adult")
else:
    print("Entered age ", age, " is NOT Adult")
