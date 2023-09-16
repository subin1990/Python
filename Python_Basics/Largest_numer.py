print("this program is to find the largest number in a list")
User_input = input(" Enter numbers suppurated by space")
User_list = User_input.split()
#print(User_list)
# Range calculation
count = 0
for k in User_list:
    count = count + 1

Largest_number = 0
temp = 0
range_1 = range(0, count)
for i in range_1:
    for h in range_1:
        if int(User_list[i]) == int(User_list[h]):
            temp = int (User_list[i])
            if temp > Largest_number:
                Largest_number = temp
        elif int (User_list[i]) > int(User_list[h]):
            temp = int (User_list[i])
            if temp > Largest_number:
                Largest_number = temp
        elif int(User_list[i]) < int(User_list[h]):
            temp = int (User_list[h])
            if temp > Largest_number:
                Largest_number = temp

print("Largest Number in the user input is ", Largest_number)
