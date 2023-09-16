def Prime_number(Number):
    if Number<1:
        print("Entered Number is error Please try again")
    elif Number<=2:
        print(f" {Number} Not a prime number Number should be greater than 2")
    elif Number%2==0:
        print(f"{Number} is not a prime number")
    elif Number>+3:

        for i in range(3, Number):
            if Number%i==0:
                print(f"{Number} is not a prime number")
                break
            elif Number%i>0:
                print(f"{Number} is a prime number")
                break










print("Prime number function")
Number=int(input("Enter a number"))
Prime_number(Number)

