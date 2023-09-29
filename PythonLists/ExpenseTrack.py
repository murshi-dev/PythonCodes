#Write a program that allows the user to enter expenses,
# which are stored in a list. Calculate and display the total expenses.
expense=[]
total=0
#use sentinel controlled loop to get input from user
while True:
    #get input until 'q' is entered
    expenses=input("Enter expense (or 'q' to quit):")
    if(expenses=='q'):
        break
    #add each entry to list and convert to 'float' data type
    expense.append(float(expenses))
#use for loop to add each entry in list
for element in expense:
    total=total+element
#print the total value
print("Sum of all expenses is: ",total)