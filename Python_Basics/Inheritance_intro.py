print("inheritance intro")
class Human:
    def eat(self):
        print("I Can Eat")
    def work(self):
        print('I can Work')
    name='subin'

    def __init__(self,num_hart):
            self.No_of_eyes= 2
            self.No_of_nose=1
            self.No_of_hart= num_hart
class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart) # this is mandatory for accessing base class attributes when we have an init function in child class
        self.name = name        # in case base class has some arguments that should be mentioned in calling function and same will be in child method argument
    def flirt(self):
        print('I can flirt')
    def work(self):
        super().work()
        print('I can code') # overriding concept
    def display(self):
        print(f'Hi i am {self.name} and i have {self.No_of_hart}  heart') # Overriding concept

Male_1 =Male('Subin',1)
Male_1.eat()
Male_1.work()
Male_1.flirt()
print(Male_1.name)
Male_1.work()
print(Male_1.No_of_eyes)
print(Male_1.No_of_nose)
print(Male_1.No_of_hart)
Male_1.display()