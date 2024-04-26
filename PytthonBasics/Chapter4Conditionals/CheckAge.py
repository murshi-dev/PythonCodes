#Input age from user. Display “You are an adult” if the age is greater than 18, otherwise display “You are not an adult”
age=int(input("Enter the age: "))
if(age>18):
    print("Entered age ",age," is adult")
else:
    print("Entered age ",age," is NOT adult")