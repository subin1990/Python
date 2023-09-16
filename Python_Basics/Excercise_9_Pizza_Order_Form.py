print("\n***Pizza Order Form*** \n\n")
print("*Price List*\n")
print("1 Small Pizza Rs. 100/-")
print("1 Medium Pizza Rs. 200/-")
print("1 Large Pizza Rs. 300/-")
print("\n Choose Quantity\n")
Small_Pizza=int(input("Small Pizza :"))
Medium_Pizza=int(input("Medium Pizza :"))
Large_Pizza=int(input("Large Pizza :"))
S_price=0
if Small_Pizza!=0:
    print("Pepperoni for Small Pizza Rs. 30/-\n")
    Pepperoni=input("Do You Want Pepperoni ?? (Y/N)\n")
    if Pepperoni=="Y" or Pepperoni=="y":
        S_price=(Small_Pizza*100)+30
    elif Pepperoni=="N" or Pepperoni=="n":
        S_price=Small_Pizza*100
    else:
        print("Something went wrong!!")
print("\n")
M_price=0
if Medium_Pizza!=0:
    M_price=Medium_Pizza*200
L_price=0
if Large_Pizza!=0:
    L_price=Large_Pizza*300
Pepperoni_price=0
if Medium_Pizza!=0 or Large_Pizza!=0:
    print("Pepperoni for Medium or Large Pizza Rs. 30/-\n")
    Pepperoni = input("Do You Want Pepperoni ?? (Y/N)\n")
    if Pepperoni=="Y" or Pepperoni=="y":
        Pepperoni_price= 30
    elif Pepperoni=="N" or Pepperoni=="n":
        Pepperoni_price=0
    else:
        print("Something Went wrong")
Cheese= input("Extra cheese for any Size Pizza Rs. 20/-"
              "Do you want it (Y/N)\n")
Cheese_price=0
if Cheese=="Y" or Cheese=="y":
    Cheese_price=20
elif Cheese=="N" or Cheese=="n":
    Cheese_price=0
else:
    print("Something went wrong")

Final_Price=Cheese_price+Pepperoni_price+S_price+L_price+M_price


#else:
print("\n\nFinal Price is Rs:  ",float(Final_Price),"/-")