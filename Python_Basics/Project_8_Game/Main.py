import Database
import random
import os
Point= []
Compare1 = random.randrange(50)
Answer_is_right = True
while Answer_is_right:
    Compare2= random.randrange(50)
    while Compare2== Compare1:
        Compare2 = random.randrange(50)
    print(Database.logo)
    print(f"Compare 1: {Database.database[Compare1]['name']},  {Database.database[Compare1]['Content']} from {Database.database[Compare1]['Country']} ")
    print(Database.vs)
    print(f"Compare 2: {Database.database[Compare2]['name']},  {Database.database[Compare2]['Content']} from {Database.database[Compare2]['Country']} ")
    Userchoice= int(input("Who has more Followers in Youtube Type 1 or 2: "))
    if Userchoice==1:
        if Compare1<Compare2:

            Compare1= Compare1
            Point.append(1)
            os.system('cls')
            print(f"You Won and Your Point is {sum(Point)}")
            Answer_is_right = True
        else:
            print(f"You Loss and Your Point is {sum(Point)}")
            Answer_is_right = False

    if Userchoice==2:
        if Compare2<Compare1:
            Compare1= Compare2
            Point.append(1)
            os.system('cls')
            print(f"You Won and Your Point is {sum(Point)}")
            Answer_is_right = True
        else:
            print(f"You Loss and Your Point is {sum(Point)}")
            Answer_is_right = False
