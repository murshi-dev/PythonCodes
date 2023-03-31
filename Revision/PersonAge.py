'''Write a Python program that accepts the age of 2 persons.
Count the sum of the 2 ages. If the total age is larger than 100,
show a message “you both are equal to a century creature”.
Otherwise, show a message “you both still look cool”'''
age1=int(input("Enter the first age: "))
age2=int(input("Enter the second age: "))
total=age1+age2
if(total>100):
    print ("you both are equal to a century creature")
else:
    print("you both still look cool")
