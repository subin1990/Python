# Type of Arguments
# default
# Positional
# Key word
# Arbitrary / variable length
#    Arbitrary Positional
#    Arbitrary Key word

print("Positional Arguments")


def Great(name, department):
    print(f"Hi {name} ")
    print(f"Your department is {department}")


Great("Subin", "Accounts")

print("Key Word Arguments")

Great(name="subin", department="Accounts")
Great(department="Accounts", name="Rajappan")

print("Default Arguments")


def Great1(name, department, subject="Accountancy"):
    print(f"Hi {name} ")
    print(f"Your department is {department}")
    print(f"Are you studying {subject}")

Great1("Subin", "CS")
Great1("Rajappan","Accounts","English")

print("Arbitrary Arguments")

def Sum(*numbers):
    sum=0
    for i in numbers:
        sum= sum+i
    print(f"sum is {sum}")

Sum(12,18,17,16)
Sum(1,2,3,4)




