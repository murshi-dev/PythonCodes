#create a list with few tuples
my_list=[(1,'apple'),(2,'berry'),(3,'orange')]
#display the list
for data in my_list:
    print("Number: ",data[0],"Name: ",data[1])

#create an empty list
userinput_list=[]
#add 5 tuples
for i in range(5):
    id=int(input("Enter the ID: "))
    address=input("Enter the address: ")
    #add/append the input as a tuple to list
    userinput_list.append((id,address))
#display the list
for data in userinput_list:
    print("ID: ",data[0],"Address: ",data[1])