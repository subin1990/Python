print("\n")
print("  ****Love calculator ****\n")
Name_1=input("Enter the name of 1st Person: ")
Name_2=input("Enter the name of second person: ")
Full_Name=(Name_1+Name_2).lower()
True_count=Full_Name.count("t")
True_count=True_count+Full_Name.count("r")
True_count=True_count+Full_Name.count("u")
True_count=True_count+Full_Name.count("e")
Love_Count=Full_Name.count("l")
Love_Count=Love_Count+Full_Name.count("o")
Love_Count=Love_Count+Full_Name.count("v")
Love_Count=Love_Count+Full_Name.count("e")



print("Your Love percetage is",str(True_count)+str(Love_Count),"%")




