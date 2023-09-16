# Head or Tail Game
# Excercise 11
print("\n\n***Head or Tails Game***\n")
print("How to Play: \n Press 0 for Head\n Press 1 for Tail")
print("Lets start\n")

Choice = len(input('Enter your choice: \n'))
import random
choicelist = ['Head', 'Tail']
answer = random.choice(choicelist)
print(answer)

