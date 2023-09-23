# # print(1+2)
# # print('1'+'2')
# # print(int.__add__(2,3))
# # print(str.__add__('1','2'))
# class ComplexNumber:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i
#     def __add__(self, other):
#         return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
#
# c1= ComplexNumber(1,2)
# c2= ComplexNumber(4,5)
# print(c1+c2)

class Person():
    def __init__(self,name,age):
        self.Name= name
        self.Age= age
    def __gt__(self, other):
        if self.Age> other.Age:
            return True
        else:
            return False
p1= Person('Subin',33)
p2= Person('Rajamma',34)

if p1>p2:
    print(f'{p1.Name} will pay the bill')
else:
    print(f'{p2.Name} will pay the bill')


