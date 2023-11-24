'''Create a shopping list. Add items to it from user input. Save it in a text file.
Display the contents of the file in the console.'''

#write mode
def create_shopping_list(file_name):
    with open(file_name,'w') as file:
        file.write("Shopping List\n")

#append mode
def add_item_to_shoppingList(file_name,item):
    with open(file_name, 'a') as file:
        file.write(f"{item}\n")

#read mode
def display_shoppingList(file_name):
    with open(file_name,'r') as file:
        content=file.read()
    print(content)

#call the functions one by one
#create the text file
create_shopping_list("shopping.txt")

#add items to text file from user input through while loop
while True:
    user_input=input("Enter an item (q to quit): ")
    if(user_input=='q'):
        break
    add_item_to_shoppingList("shopping.txt",user_input)

#display the contents from text file
display_shoppingList("shopping.txt")






