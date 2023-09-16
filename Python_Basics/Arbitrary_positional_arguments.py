print("Arbitrary positional arguments")
def sum(*numbers, name):
    sm= 0
    for i in numbers:
        sm= sm+i
    print(f"sum is {sm}")
    print(name)

sum (15, 18,13,14, name='subin')
sum(1,15,name='Rajappan')