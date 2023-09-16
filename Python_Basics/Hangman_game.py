import random
print("Hangman Game")
print("Welcome to Hangman Game")
Fruits_list = ['apple','banana', 'orange','grapes']
Fruit_name=random.choice(Fruits_list)
print(Fruit_name)
Name_len = len(Fruit_name)
print("You have only 6 lives. So try the word within 6 attempts. Best of Luck")
Display = []
lives = 6
for i in range(Name_len):
    Display+= '-'
print(Display)
Game_over= False
while not Game_over:
    Guess_letter = input("Guess a Letter:").lower()
    for j in range(Name_len): #0 1 2 3 4
        Letter = Fruit_name[j]# a, p, p,l,e
        if Letter == Guess_letter: # a
            Display[j] = Guess_letter
    print(Display)
    if Guess_letter not in Fruit_name:#a apple
        lives-=1
        if lives==0:
            Game_over =True
            print("You Loss")
    if '-' not in Display:
        Game_over= True
        print("You Win")