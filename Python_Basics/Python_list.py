numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names= ['Subin', 'Dasan', 'Billy', 'Achu']
Mix_list= ['subin', 100, 'Dasan', 99]
print(numbers)
print(names)
print(Mix_list)
print(names[0])
print(len(numbers))
print(names[-1]) # negatve index is also possible
print(names[:]) # list slicing
print(names[0:4]) # examples
print(names[0:]) # examples
print(names[0:2]) # 1st digit is the index and second digit is the length Simple (lenth-1 that index will print)
print(names[:2]) # starting is nil so it start from default
print(numbers[0:5:2]) # Extended slicing this will skip 2 indexes
print(numbers[::2]) # the starting and end is nill so it start and end with default.and skip 2 indexes
# sorting
names.sort()
print(names)
print(names.sort()) # this will sort nothing mix list cannot be sorted
# reversing the list
names.reverse()
print(names)
# Finding Minimum and maximum
print(min(numbers))
print(max(numbers))
# Adding data in string
# 1,Append - Adding only one value at the end
numbers.append(15)
print(numbers)
# 2 insert - Adding ony one value in a specified index number
numbers.insert(2,15)
print(numbers)
# 3 extend - Adding multiple values at the end
numbers.extend([15, 19, 28, 43, 45])
print(numbers)
# change the data
numbers[2]=10
print(numbers)
#changing more data
numbers[2:5]=[19,18,23,25,31] #chaning data from 2 nd index to length 5
print(numbers)
# Remove  the data
numbers.remove(43) # this only remove the 1st concurrent data
print(numbers)
# Pop (by default it remove the last index data)
print(numbers.pop())
print(numbers)
print(numbers.pop(0))