#create empty dictionary
contacts={}
#create a menu for CRUD contacts
while True:
    print("\nMenu")
    print("1.Create Contact")
    print("2.Read Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Exit")
    #input choice
    choice=input("Enter the choice: ")
    if choice == '1':#add new contact to dictionary
        name=input("Enter the name of the contact: ")#key
        number=input("Enter the contact number: ")#value
        #add key value to dictionary
        contacts[name]=number
        print(f'Contact {name} is added!')
    elif choice == '2':  #view contact from dictionary
        name=input("Enter the contact name to view: ")
        if name in contacts:
            number=contacts[name]
            print(f'Name: {name}, Contact: {number}')
        else:
            print(f"Contact {name} does not exist!")
    elif choice == '3': #update existing contact
        name=input("Enter the contact name to update: ")
        if name in contacts:
            number=input("Enter the new contact number: ")
            contacts[name]=number
            print(f'Contact {name} is updated!')
        else:
            print(f"Contact {name} does not exist!")
    elif choice == '4': #delete existing contact
        name=input("Enter the contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f'Contact {name} is deleted!')
        else:
            print(f"Contact {name} does not exist!")
    elif choice == '5':#exit
        break
    else:
        print("Invalid choice. Try Again!")
