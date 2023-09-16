# this is the updated version of Excercise 2 and 7
print("**BMI Calculator**\n\n")
Wheight=float(input("Enter your Weight in Kg: "))
height=input("Enter your Height in CM: ")
height=int(height)/100
BMI=round((Wheight)/(height*height),2)
if BMI<=18.49:
    print(f"Your BMI is {BMI} and you are Under weight")
elif BMI<=24.99:
    print(f"Your BMI is {BMI} and you have normal weight")
else:
    print(f"Your BMI is {BMI} and you are Over weight")

print("Thanks for using the program")


#print("\nBMI=",(BMI))



#print("\nResult interpretation")
#print("Underweight = <18.5")
#print("Normal weight = 18.5–24.9")
#print("Overweight = 25–29.9")
#print("Obesity = BMI of 30 or greater")

