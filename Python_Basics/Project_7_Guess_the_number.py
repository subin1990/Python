import random
def Guess_the_Number(count,chance):
    print(f"You have {count} attempts remaining to guess the number:")
    for i in range(chance):
        Guess_number = int(input("Make a Guess:"))
        if Guess_number == number:
            print(f"Your Guess is right and Answer is {number}")
            break
        elif Guess_number > number:
            count = count - 1
            print("Your Guess is too large")
            print(f"You have {count} attempts remaining to guess the number:")
            if count != 0:
                print(" Guess Again...")
        elif Guess_number < number:
            count = count - 1
            print("Your Guess is too less")
            print(f"You have {count} attempts remaining to guess the number:")
            if count != 0:
                print(" Guess Again...")
    if count==0:
        print(f"You Loss !!!!!!!! The answer is {number}.")


print("Project 7 Guess the Number")
print("Let Me think of a number between 1 to 50.")
number = random.randrange(1,50)

#print(number)
User_choice= str(input("Choose Level of difficulty ..... Type 'easy' or 'hard':\n").lower())

if User_choice== 'easy':
    count= 10
    chance=10
    Guess_the_Number(count,chance)
elif User_choice== "hard":
    count= 5
    chance= 5
    Guess_the_Number(count,chance)

