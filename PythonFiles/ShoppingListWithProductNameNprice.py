'''Create a product list. Add product names with price to it from user input.
Save it in a text file.
Display the contents of the file in the console.
Update the code such that new items can be added to the existing shopping list. '''

import os

#write mode
def create_product_list(file_name):
    with open(file_name,'w') as file:
        file.write("Product List\n")

#append mode
def add_item_to_productList(file_name,item,price):
    with open(file_name, 'a') as file:
        file.write(f"{item}: RM {price}\n")

#read mode
def display_productList(file_name):
    with open(file_name,'r') as file:
        content=file.read()
    print(content)

#call the functions one by one
#create the text file
file_name = "productlist.txt"

#check if file exist
if os.path.isfile(file_name):
    print("Product list found!")
    display_productList(file_name)
else:
    print("Product list not found!")
    #create a new one
    create_product_list(file_name)

#add items to text file from user input through while loop
while True:
    product_name=input("Enter product name (q to quit): ")
    if(product_name=='q'):
        break
    product_price = input("Enter product price: ")
    add_item_to_productList(file_name,product_name,product_price)

#display the contents from text file
display_productList(file_name)






