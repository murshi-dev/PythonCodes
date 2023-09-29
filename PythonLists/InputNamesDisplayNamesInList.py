#create a empty list
names=[]
#set the list size
list_size=int(input("Enter the number of names in list: "))
#input the names using for loop
for i in range(list_size):
    print(i+1)
    element=input("Enter the name: ")
    names.append(element)
#display the names using for loop
for name in names:
    print(name)