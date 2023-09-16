print('Hierarchical inheritance')

class Human():
    def eat(self):
        print('I can eat')
    def __init__(self,name, age):
        print('init method is calling from Human class')
        self.name= name
        self.age =age
    def showdetails(self):
        print(f'name is {self.name} and age is {self.age}')
class Male(Human):
    def sleep(self):
        print('I can sleep whole day')
    def __init__(self,m_name,m_age, location):
        print('init method is calling from male class')
        Human.__init__(self,m_name,m_age)
        self.location= location

class female(Human):
    def work(self):
        print('I can code')
    def __init__(self,name,age,can_dance):
        print('init method is calling from female class')
        super().__init__(name,age)
        self.can_dance = can_dance
    def showdetails_f(self):
        Human.showdetails(self)
        print(f'know dancing {self.can_dance}')
Female_1= female('Achu',30,True)
Female_1.eat()
print(Female_1.name)
Female_1.showdetails_f()
#
# Male_1= Male('Subin',33,'Gurgaon')
# print(Male.mro())
# print(Male_1.name,Male_1.age, Male_1.location)