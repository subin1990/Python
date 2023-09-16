class Student:
    def __init__(self,name,roll_number,Age):
        self.name= name # public instance variable
        self._rollnumber=roll_number # Protected instance variable
        self.__Age = Age
    def display(self):
        print(f'Hi my self {self.name} from student class and roll number is {self._rollnumber} and age is {self.__Age}')

S1= Student('Rajappan',15,30)
S1.name= 'Raghavan from Panineer Poove'
S1._rollnumber = 145
print(S1.name)
print(S1._rollnumber)
S1.display()