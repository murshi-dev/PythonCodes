#compare two numbers - display bigger number
#get user input using functions
#write compare logic using functions

#define a function to get user input
def getUserInput():
    num1=int(input("Input first number: "))
    num2=int(input("Input second number: "))
    return num1,num2

#define a function for comparison
def compareNumbers(x,y):
    if(x>y):
        return x
    else:
        return y

#function call to get input
num1,num2=getUserInput()
#function call to compare numbers
biggerValue = compareNumbers(num1,num2)
print("Bigger value is: ",biggerValue)

