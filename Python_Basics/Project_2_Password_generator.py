import random
print("*****Password Generator*****")
Ch_count = int(input("Enter the number of Characters"))
No_count = int(input("Enter the number of Numbers"))
Sy_count = int(input("Enter the number of Symbols"))
Ch_list =['A','a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J','j','K', 'k', 'L'
,'l', 'M','m', 'N', 'n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']


random.shuffle(Ch_list)
Random_Charactors = Ch_list
Ch_password = []
for i in range(Ch_count):
    Ch_password.append(Random_Charactors[i])

No_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(No_list)
Random_Numbers= No_list
Number_Password = []
for i in range(No_count):
    Number_Password.append(Random_Numbers[i])


Symbol_List =['~', '`','!', '@', '#', '$', '%', '^', '&', '*', '(',')','_', '-', '+', '=', '{', '[', '}', ']', '|', "/",
':', ';', '<','>', '.', '?', '/']

random.shuffle(Symbol_List)
Random_Symbols = Symbol_List
Symbol_Password = []
for i in range(Sy_count):
    Symbol_Password.append(Random_Symbols[i])
Password_List=[]
Password_List.append(Ch_password+Number_Password+Symbol_Password)
random.shuffle(Password_List[0])
password_lenght = len(Password_List[0])
Password= ''
for i in range(password_lenght):
    Password= Password+str(Password_List[0][i])
print("Your Password is :  ",Password)
