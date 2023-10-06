#set operations
#create two sets
set1={1,2,3,4,5}
set2={4,5,6,7,8}
#union - combine all the values from set1 and set2
#dulicates removed
union_set=set1 | set2
#display the union set
print("Union of Sets: ",union_set)
#intersection - displays the common element in both the sets
intersection_set = set1 & set2
#display the intersection set
print("Intersection of Sets: ",intersection_set )
#difference  - displays from set 1 but not in set 2
difference_set = set1 - set2
#display the difference set
print("Difference of Sets: ",difference_set )
#symmetric difference  - displays from set 1 or
# in set 2 but not in both
symmetric_difference_set = set1 ^ set2
#display the difference set
print("SymmetricDifference of Sets: ",symmetric_difference_set)
#sample - mutual friends
friends1={"alice","bob","charlie","david"}
friends2={"charlie","david","frank"}
#display mutual friends
#mutual_friends=friends1 & friends2
mutual_friends=friends1.intersection(friends2)
print("Mutual Friends are: ",mutual_friends)
