'''Input age from user. Display “You are an adult” if the age is greater than 18, otherwise display “You are not an adult”.
Check if the entered age is a positive number. Display error otherwise.
Repeat the code to check age of three people.
'''
#1.set the initial value
counter=1
#2.check the condition, specify the end value
while(counter<=3):
    print("Entry ",counter)
    age=int(input("Enter the age: "))
    if(age<0):
        print("Enter positive numbers only! ")
    elif(age>18):
        print("Entered age ",age," is categorised ADULT")
    else:
        print("Entered age ", age, " is categorised NOT ADULT")
    #3.update the counter
    counter=counter+1

