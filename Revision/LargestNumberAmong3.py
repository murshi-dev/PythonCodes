'''Write a program to find the largest among 3 numbers entered'''
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
if(n1>=n2) and (n1>=n3):
    largest=n1
elif(n2>=n1) and (n2>=n3):
    largest =n2
else:
    largest=n3
print("Largest number is: ",largest)
