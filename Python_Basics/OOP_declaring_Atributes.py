print('Object oriented programming-Adding attributes')


class CarData:
    def __init__(self, Car_name, MFG_Date):
        self.name = Car_name
        self.Manufacturing_year = MFG_Date
        self.month = 0


car1 = CarData('Creta', 2022)
car2 = CarData('Ecospot', 2020)
car3 = CarData('Balero', 2019)
print(car1.name)
print(car1.Manufacturing_year)
print(car1.month)
print(car2.name)
print(car2.Manufacturing_year)
print(car2.month)
print(car3.name)
print(car3.Manufacturing_year)
print(car3.month)
