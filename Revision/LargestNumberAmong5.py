'''You are required to get 5 integer input number from the user.
Find out what is the largest number given by the user.
Hint: you need to use variables to store the current largest number.'''
largest=0
count=1
while(count<=5):
    num=int(input("Enter the number"))
    if(num>largest):
        largest=num
    count=count+1
print("Largest number is: ",largest)

