import os


def Pr():
    print("*** Project 6- Simple Calculator **")
    Number1 = int(input("Enter First Number: "))

    continue_flag = True
    while continue_flag:
        print("**Operation list**\n")
        print("For Addition press +")
        print("For Subtraction  press -")
        print("For Multiplication   press *")
        print("For Division   press /")
        op = input("Pick an Operation: ")
        Number2 = int(input("Enter Next Number: "))
        result= 0
        if op == '+':
            result = Number1 + Number2
        elif op == '-':
            result = Number1 - Number2
        elif op == '*':
            result = Number1 * Number2
        elif op == '/':
            result = Number1 / Number2

        print(f'{Number1} {op} {Number2} = {result}')
        User_choice = str(input(
            f"Enter 'Y' to continue with Calculation {result} or enter 'N' to start new Calculation or enter 'X' to exit the "
            "program: ")).upper()
        if User_choice == "N":
            os.system('cls')
            Pr()
        elif User_choice == 'Y':
            Number1 = result
        elif User_choice== 'X':
            print("Your are exiting thank you for using the program")
            continue_flag = False


Pr()
