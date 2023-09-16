from Abstract_class import Vehicle

class Bike(Vehicle):

    def start(self):
        print('Start with click')
    def __init__(self,n,color):
        super().__init__(n)
        self.color = color
class Scooty(Vehicle):
    def start(self):
        print('Selft start')
    def __init__(self,n):
        self.number_of_tyres = n
class Car(Vehicle):
    def start(self):
        print('Start with key')
    def __init__(self,n,No_of_Gears):
        self.number_of_tyres = n
        self.gear= No_of_Gears