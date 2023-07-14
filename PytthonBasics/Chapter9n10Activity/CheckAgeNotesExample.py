'''Input age from user. Display “You are an adult” if the age is greater than 18, otherwise display “You are not an adult”
'''
#input
age=int(input("Enter the age: "))
#process
#check condition
if(age>=18):
    #if age>=18 is true next statement is executed
    print("You are an adult")
else:
    # if age>=18 is false next statement is executed
    print("You are not an adult")
