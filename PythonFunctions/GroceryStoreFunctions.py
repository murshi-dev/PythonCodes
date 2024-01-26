'''Consider a grocery store that requires a system to keep track
of the product names, category, price, and  number of products available.
Create a menu based python code to manage the
product names, category, price, and  number of products
using relevant data structures. The program must have a
function add_product() to add new products and a function
view_products() to view existing products.'''

#create a list for products
products=[]
#create a set for category
category={"fruits","veggies","dairy","bakery"}
#create a dictionary for stock
product_stock={
    "apple":10,
    "tomato":20,
    "milk":30,
    "bread":40
}
#create a dictionary for price
product_price={
    "apple":3.5,
    "tomato":4.5,
    "milk":5.5,
    "bread":6.5
}
#function to display meny
def showMenu():
    print("Menu")
    print("1. Add Product")
    print("2. View Product")
    print("3. Quit")

#function to add products
def addProducts():
    #get user input
    name=input("Enter product name: ")
    category = input("Enter product category: ")
    stock = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))

    #add name and category to list
    products.append((name,category))
    #add stock and price to dictionary
    product_stock[name]=stock
    product_price[name]=price

#function to view products
def viewProducts():
    print("Available Products:")
    for name,category in products:
        print(f"Product Name: {name},Product Category: {category},"
              f"Quantity Available: {product_stock[name]}, Price: RM {product_price[name]}")

#main loop
#main code - use loop
while True:
    showMenu()
    option = int(input("Enter the option: "))
    if(option==1):
        addProducts()
    elif(option==2):
        viewProducts()
    elif(option==3):
        break
    else:
        print("Invalid Choice")








