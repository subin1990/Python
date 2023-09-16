print(" This program is to print patterns in Python")
print("Rectangle")
n = 5

for i  in range(n):
    for h in range(n):
        print("*",end=" ")
    print()
print("increasing triangle")

for i in range(n):
    for h in range(i):
        print("*", end=" ")
    print()

print("Decreasing triangle")
for i in range(n):
    for h in range(n-i):
        print("*",end=" ")
    print()
