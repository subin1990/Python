import random

# randint function
print(random.randint(1, 9))

# randrange function
print(random.randrange(1, 15))

# Random. random (for float numbers by deafault it print between 0 to 1-.01

print(random.random())

# random.uniform
print(random.uniform(14, 15))
# random List
l = [1, 2, 3, 4, 5]
print(random.choice(l))

# random Shuffle
random.shuffle(l)
print(l)
