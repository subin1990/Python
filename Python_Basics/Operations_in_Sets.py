print("Union in set")

set1= {'subin', 'karakoode', 'rajamma'}
set2= {'kandan', 'kileri', 'subin'}
set3 = {'achumma', 'vavan','subin'}
# union removing duplicate values and keep only one
# first method
#print(set1.union(set2, set3,('tomu', 'kara'))) # we can add tuples as argument
# second method
#print(set1 | set2 | set3)

# updating set
# method 1
#set1.update(set2,set3,['tamas','taman'])
# method 2

#set1 |= set3

#print(set1)

print("Intersection in set")
# keeping only common values in two or more set
# first mwthod
#print(set1.intersection(set2,set3,['subin', 'rajappan']))
# second method
#print((set1&set2&set3))

#updating intersection

#set1.intersection_update(set3,set2)
#print(set1)
