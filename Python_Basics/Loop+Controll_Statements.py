print("Break")

count = 1
while count<=10:
    print(count)
    count=count+1
    if count == 7:
        break
    print("Hi")
print("out from Loop")

list1= ["hi","hello","welcome"]
list2 = ['subin', 'rajappan', 'acha']
for i in list1:
    for name in list2:
        print(i,name)
        if i =='welcome' and name == 'rajappan':
            break
    print("Out from the inner loop")
print("out from the outer loop")

print("Continue")

for i in range(1,11):
    if i ==7:
        continue
    else:
        print(i)

print("Pass")
for i in range(11):
    pass