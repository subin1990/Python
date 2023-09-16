# list, tuples and sets
# to store multiple itesm in a single variable
# 1 list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
print(type(list1))
list1[0] = -10
print(list1)
list1.clear()

tuples1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuples1)
print(type(tuples1))
# tuples1[0] = -10 error
#print(tuples1)
#tuples1.clear

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set1)
print(type(set1))
# set1[0] = -10 error
set1.clear()