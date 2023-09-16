import random

print("\n****** Rock Scissor paper Game ******\n")
print("\nEnter 0 for Rock\nEnter 1 for Paper\nEnter 2 for Scissor\n")
user_number = int(input("Enter a number between 0-2 (0,1,2): \n"))
System_number = random.randint(0, 2)
print(System_number)
if user_number < 0 or user_number > 2:
    print("Wrong Number (number should be 0,1,2)")
elif user_number - System_number == -1 or user_number - System_number == 2:
    print("I am Win !!!!")
elif user_number - System_number == 1 or user_number - System_number == -2:
    print("Ohhh You Win !!!!")
else:
    print("Match Drawn")
