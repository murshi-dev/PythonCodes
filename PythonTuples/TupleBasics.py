#tuple is a data type in python
#used to store a collection of items
#tuples are not chnageable - immutable
sample_tuple=(1,2,'hi')
print(sample_tuple)
print("First element:", sample_tuple[0])
print("Second element:", sample_tuple[1])
print("Third element:", sample_tuple[2])
#print last element
print("Last element:", sample_tuple[-1])
#modify an elemnt
# sample_tuple[0]=53 - contents cannot be changed
#display elemnts in tuple using for loop
for item in sample_tuple:
    print("Data: ",item)

#find the length of tuple
print("Number of elements in tuple is",len(sample_tuple))

#tuples can concatenate - add
tuple1=(1,2,3)
tuple2=('a','b','c')
combined_tuples=tuple1+tuple2
for data in combined_tuples:
    print(data)
