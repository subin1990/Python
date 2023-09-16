class Human:
    def eat(self):
        print(' I can eat')
    def __init__(self,num_heart):
        self.number_heart= num_heart
        self.eyes= 2
    def work(self):
        print('I can work')
class Male(Human):
    def sleep(self):
        print("I can sleep whole day")
    def __init__(self,name):
        self.name= name

class Boy(Male):
    def work(self):
        #super().work() # Calling work method from Human class method 1
        Human.work(self) # Calling work method from Human class method 1
        print('i can code')

    def __init__(self,numheart,name,can_dance):
        Human.__init__(self,numheart)
        Male.__init__(self,name)
        self.can_dance= can_dance

Boy1= Boy(2,'Subin',True)
Boy1.eat()
Boy1.work()
print(Boy1.eyes)
print(Boy1.name)
print(Boy1.can_dance)
