class Student:
    def __init__(self,name,roll_number,Age):
        self.name= name # public instance variable
        self._rollnumber=roll_number # Protected instance variable
        self.__Age = Age # Private instance variable
    def get_Age(self):
        return self.__Age
    def set_Age(self,userage):
        if userage >35:
            print("Age should be less than 35 ")
        else:
            self.__Age= userage

#     def __display(self):
#         print(f'Hi my self {self.name} from student class and roll number is {self._rollnumber} and age is {self.__Age}')
#     def private_display(self):
#         self.__display()
#
# class Branch(Student):
#     def show(self):
#         print(f'my roll number is {self._rollnumber}.')


S1= Student('Rajappan',15,30)
print(S1.get_Age())
S1.set_Age(34)
print(S1.get_Age())
