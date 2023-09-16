print('Excercise 26 radious of a circle')

class circle:
    pi = 3.14
    def __init__(self,Radious):
        self.radious = Radious
        self.area= circle.pi* self.radious* self.radious
    def Get_circumference(self):
        return circle.pi* self.radious

circle1= circle(40)
print(circle1.Get_circumference())
print(circle1.area)