#Create a list and fill with numbers from user input.
# Display the largest element in the list.
# Initialize an empty list
numbers = []
# Get the number of elements user wants to input
num_elements = int(input("Enter the number of elements: "))
# Use a for loop to get input and append to the list
for i in range(num_elements):
    element = input("Enter element: ")
    numbers.append(element)
# Print the resulting list
print("The list is:", numbers)
#set a max element
max_element=numbers[0]
for num in numbers:
    if(num>max_element):
        max_element=num
print("Max value is ",max_element)





