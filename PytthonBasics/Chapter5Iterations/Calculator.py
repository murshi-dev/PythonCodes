'''Amy needs to design a simple calculator that performs addition,
subtraction, multiplication, and division of two numbers. Let the user
 enter a single character as the desired operation, for example ‘A’, ‘a’,
 or ‘+’ for add. The user should be able to enter the uppercase initial,
  lowercase initial, or the arithmetic symbol. Based on the entered option
  (addition or subtraction or multiplication or division) the program prompts
  for numbers, calculates the relevant arithmetic operation, and displays the
   result. Validate/Check the input numbers for positive numbers.
     use sentinel controlled loop   '''

choice='y'
while(choice=='y' or choice=='Y'):
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    print("A. Addition\n S.Subtraction\n M.Multiplication\n D.Division")
    option=input("Enter the option: ")
    if(option == 'A' or option=='a' or option=='+'):
        result = n1+n2
    elif(option == 'S' or option=='s' or option=='-'):
        result = n1-n2
    elif (option == 'M' or option=='m' or option=='*'):
        result = n1 * n2
    elif (option == 'D' or option=='d' or option=='/'):
        result = n1 / n2
    print("First Number: ",n1)
    print("Second Number: ", n2)
    print("Selected Option: ",option)
    print("Result: ",result)
    choice=input("Continue(Y/N): ")