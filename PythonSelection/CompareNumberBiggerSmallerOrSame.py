#code to display smaller, bigger or same among two numbers
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
if(n1<n2):#first if
    print(n1,' is smaller than ',n2)
elif(n1>n2):
    print(n1, ' is greater than ', n2)
else:
    print(n1, ' is same as ', n2)
