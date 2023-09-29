#list basics
# a list is a collection which is ordered and changeable
#can have duplicate values
#create a list
numbers = [1,2,3,4,5]
#print the first value
#list index starts from 0
print("First value in the list is ", numbers[0])
#print the last value
print("Last value in the list is ", numbers[-1])
#print all elements in the list
#use for loop
for element in numbers:
    print(element)

#create list with string
fruits=['apples','oranges','grapes','pears']
#display the fruits list
for fruit in fruits:
    print(fruit)
#another way to display elements with index - enumerate
for index,fruit in enumerate(fruits):
    print("Index: ",index,"Fruit: ",fruit)

#get the size/length of the list
print("Length of the list is: ",len(fruits))

#append items to list - add to the end of list
fruits.append('Mango')
for fruit in fruits:
    print(fruit)

#add items at specific index
fruits.insert(2,'strawberries')
for fruit in fruits:
    print(fruit)

#remove items based on index
fruits.pop(2)
for fruit in fruits:
    print(fruit)

#remove items based on names
fruits.remove('grapes')
for fruit in fruits:
    print(fruit)

#reverse a list
fruits.reverse()
for fruit in fruits:
    print(fruit)

#sort/arrange a list
fruits.sort()
for fruit in fruits:
    print(fruit)

#reverse sort a list
fruits.sort(reverse=True)
for fruit in fruits:
    print(fruit)