# Sets
# A set is a collection which is unordered and unindexed. No duplicate members.
# Sets are written with curly brackets.
'''
my_set = {1, 2, 3, 4, 5}
print(my_set)  #printing the set

my_set.add(6)  #adding an element to the set
print(my_set)

my_set.remove(2)  #removing an element from the set
print(my_set)
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)  #combining two sets
print(union_set)  #printing the union of the sets

# Intersection
intersection_set = set1.intersection(set2)  #finding common elements in both sets
print(intersection_set)  #printing the intersection of the sets
# Difference
difference_set = set1.difference(set2)  #finding elements in set1 that are not in set2
print(difference_set)  #printing the difference of the sets
