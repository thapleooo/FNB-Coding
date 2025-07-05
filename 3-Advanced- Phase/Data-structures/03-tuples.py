# Tuples 
# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are written with round brackets.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  #printing the tuple
print(my_tuple[2])  #accessing the third element
print(my_tuple[-1])  #accessing the last element

my_tuple1 = ("apple", "banana", "cherry")
my_tuple2 = (1, 2, 3, 4, 5)

conc = my_tuple1 + my_tuple2  #concatenating two tuples
print(conc)  #printing the concatenated tuple

rep_tuple = my_tuple1 * 2  #repeating the tuple
print(rep_tuple)  #printing the repeated tuple