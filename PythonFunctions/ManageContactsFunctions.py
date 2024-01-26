'''1.	Create a menu-driven program using python for a managing contact.
The program must have functions that allows the user to
add contacts and view contacts. Use the following functions:
	show_menu()
	add_contact()
	view_contact()
'''

#create dictionary
contacts={}
#function to display meny
def showMenu():
    print("Menu")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Quit")

#function to add contact
def addContact():
    name=input("Enter contact name: ")
    number=input("Enter contact number: ")
    #add name and number to contacts dictionary
    contacts[name]=number
    print(f"Contact {name} is added!")

# function to view contact
def viewContact():
    for name,number in contacts.items():
        print(f"Name: {name}, Contact Number: {number}")

#main code - use loop
while True:
    showMenu()
    option = int(input("Enter the option: "))
    if(option==1):
        addContact()
    elif(option==2):
        viewContact()
    elif(option==3):
        break
    else:
        print("Invalid Choice")









