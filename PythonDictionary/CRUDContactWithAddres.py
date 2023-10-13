# Initialize an empty contact dictionary
contacts = {}

# Menu-based interaction
while True:
    print("\nMenu:")
    print("1.Create Contact")
    print("2.Read Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the name of the contact: ")
        number = input("Enter the phone number: ")
        address = input("Enter the address: ")
        contacts[name] = {'Phone Number': number, 'Address': address}
        print(f"Contact '{name}' added.")
    elif choice == '2':
        name = input("Enter the name of the contact to view: ")
        if name in contacts:
            details = contacts[name]
            print(f"Name: {name}, Phone Number: {details['Phone Number']}, Address: {details['Address']}")
        else:
            print(f"Contact '{name}' not found.")
    elif choice == '3':
        name = input("Enter the name of the contact to update: ")
        if name in contacts:
            number = input("Enter the new phone number: ")
            address = input("Enter the new address: ")
            contacts[name] = {'Phone Number': number, 'Address': address}
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' not found.")
    elif choice == '4':
        name = input("Enter the name of the contact to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
