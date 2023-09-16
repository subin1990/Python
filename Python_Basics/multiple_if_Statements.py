hight = float(input("What is your height:"))
if hight > 3:
    print("You can ride !!!")
    age = int(input("Enter yor age:"))

    if age <= 12:
        print("Ticket price is 150")
        ticket_price = 150
    elif age <= 18:
        print("Ticket price is 250")
        ticket_price = 250
    else:
        print("Ticket price is 350")
        ticket_price = 350

    choice = input("You want to take photos ?? (Y/N)")
    if choice == "N":
            print("Ticket price is ",ticket_price)
    elif choice == "Y":
            print("Ticket price is",ticket_price+50)
    else:
            print("Wrong Answer try again...")


else:
    print("Sorry you can't ride Thank you...")
print("Thank you.....")
