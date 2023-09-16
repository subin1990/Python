print('Object oriented programming with methods')

class CarData:
    Month = 0
    def __init__(self,Car_name,MFG_Date):
        self.Name= Car_name
        self.Manufacturing_Date= MFG_Date
    def Dispaly_Car_Name(self,Number):
        print(f'Car name is {self.Name} month is {self.Month} and Car reg Number is {Number}')


Car1 =CarData('Creta','2022')
Car1.Dispaly_Car_Name('HR26DA5049')
Car2= CarData('Zylo','2020')
Car2.Dispaly_Car_Name('HR26FA4918')
Car2.Month=15
print(Car2.Month)