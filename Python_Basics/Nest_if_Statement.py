Hight=int(input("Enter Your Height: "))
if Hight>=3:
    age=int(input("Enter your age:"))
    if age<=12:
        print("Pay Rupees 150/-")
    elif age<=18:
        print("Pay Rupees 250/-")
    else:
        print("Pay Rupees 300/-")
else:
    print("You are not eligible")
print("Thank you")

