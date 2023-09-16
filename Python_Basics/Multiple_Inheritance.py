print("Multiple Inheritance")
class Human:
    #Adding attributes
    def __init__(self,Number_heart):
        self.num_of_eyes=2
        self.num_of_nose=1
        self.num_heart= Number_heart
    def eat(self):
        print('I Can Eat')
     # Same method in second parent calss
    def work(self):
        print('I Can Work')
class Male:
    def flirt(self):
        print('I can flirt')
    def __init__(self,name):
        self.name= name
    # Same method in second parent calss
    def work(self):
        print('I Can Code')
class Boy(Human,Male):
    def __init__(self,name,heart,Language):
        self.name = name
        self.Lang= Language
        Human.__init__(self,heart)
    def dispaly(self):
        print(f'hi i am {self.name} and i am working in {self.Lang}')


    def work(self):
        # Same method in parent calss
        print('I Can test')

Boy1= Boy('Subin','1','Python')
Boy1.eat()
Boy1.flirt()
# Same method in all class it will access on the basis of MRO 'Method Resolution Order' for accessing MRO we can use MRO Function
# Same method in second parent calss  this time its only access based on the order of parent classes in child class
# this case order of child class is Human and Male so the method only access the Human class method first
#print(Boy.mro()) # Accessing MRO
# Solution
# We need to mention which parent class accessing and which method is accessing then pass the object name
Male.work(Boy1)
print(Boy1.num_of_eyes)
Boy1.dispaly()
