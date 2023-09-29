#Write a program that lets a user manage an inventory by entering items and their quantities. It displays the current inventory after input.
inventory=[]
#use sentinel controlled loop to get input from user
while True:
    #get input until 'q' is entered
    item=input("Enter the item (or 'q' to quit):")
    if(item=='q'):
        break
    #get the quantity
    quantity=int(input("Enter quantity: "))
    #add each item and quantity to list
    inventory.append((item,quantity))
#use for loop to add display each entry in list
print("Current Inventory:")
#use enumerate to display list item with index
for item,quantity in inventory:
    print(item," , ",quantity,"units")

