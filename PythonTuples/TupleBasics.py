#tuple is a data type in python
#used to store a collection of items
#tuples are not changeable - immutable

#create a tuple
sample_tuple=(1,2,'hi')
#print all the contents of the tuple
print(sample_tuple)
#print each element using index
print("First element: ",sample_tuple[0])
print("Second element: ",sample_tuple[1])
print("Third element: ",sample_tuple[2])
#print last element
print("Last element: ",sample_tuple[-1])
#try to change an element
#sample_tuple[0]=23 --raises an error

#display elements in tuple using for loop
for item in sample_tuple:
    print("Elements: ",item)

#find the length of the tuple
print("Number of elements: ",len(sample_tuple))

#tuples can be joined together - concatenate
tuple1=(1,2,3)
tuple2=('a','b','c')
combined_tuples = tuple1 + tuple2
#print
for data in combined_tuples:
    print(data)