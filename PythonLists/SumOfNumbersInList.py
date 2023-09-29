#get the numbers from user, add to a list
#find the sum of all numbers in a list
numbers=[]
#get the number of items in the list from user
num_elements=int(input("Enter the number of elements in list: "))
# get each item in the list from user
for i in range(num_elements):
    print(i+1)
    element=int(input("Enter element: "))
    #use append to add to list
    numbers.append(element)
#to accumulate and sum up every element use 'total' variable
total=0
for element in numbers:
    #total=total+element
    total+=element
print("Sum of all elements is: ",total)