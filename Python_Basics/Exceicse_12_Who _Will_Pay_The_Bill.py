# Excercise 12 Who will pay the Hotel bill
import random
print("\nWho will pay your Hotel Bill ????\n")
Names = input('\nEnter the names sepperated by "," :\n\n')
Names_list = Names.split(",")

Names_Count = len(Names_list)

Name_choose = random.randint(0,(Names_Count-1))
print("\n")
print((Names_list[Name_choose])+"!! will pay the bill")
