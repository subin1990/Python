print("Local and Global Scope")

def sum():

    a= 10 # local variable
    b = 20 # local variable
    #c = a+b # local variable
    print(c)

a = 10 # Global Variable

c= 15 # Global Variable


print(c) # not print the varibale from function
sum()

print ("Global Keyword")


num1= 1000
def display():
    global num1
    num1=  num1+100
    num2= 450
    global total
    total=num1+num2
    print(total-1550)

display()
print(total)
