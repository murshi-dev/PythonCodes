#create an empty set
sample_set=set()
#ask user how many elemets in set
num=int(input("Enter the number of elements to be added: "))
#use for loop to add elements to set
for i in range(num):
    element=input(f"Enter Element {i+1}: ")
    #use add method to add elements
    sample_set.add(element)
#display all elements
print("All Elements in the set are: ",sample_set)
#more operations
#create a new set
sample2_set={3,5,7,9}
#remove an element
sample2_set.remove(3)
#display the set
print(sample2_set)
#sample2_set.remove(3)#raises error since 3 does not
#exist at this point
#pop
sample2_set.pop() #remove random element from set
print(sample2_set)
#clear
sample2_set.clear() #deleted all elements from set
print(sample2_set)