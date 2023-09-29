# Create a list and fill with numbers from user input.
# Display the list. Use for loop.

# Initialize an empty list
my_list = []
# Get the number of elements user wants to input
num_elements = int(input("Enter the number of elements: "))
# Use a for loop to get input and append to the list
for i in range(num_elements):
    element = input("Enter element: ")
    my_list.append(element)
# Print the resulting list
print("The list is:", my_list)
