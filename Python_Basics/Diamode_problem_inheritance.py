class A:
    def display(self):
        print('Display from A class')
class B(A):
    def display(self):
        print('Display from B class')
class C(A):
    def show(self):
        print('Hi from C class')
    def display(self):
        print('Display from C class')
class D(B,C):
    pass

D1= D()
D1.display()
print(D.mro())