class Duck:
    def Swim(self):
        print('I am a duck and i can swim')
    def Speak(self):
        print('Quack Quack')
class Dog:
    def Swim(self):
        print('I am a dog and i can swim')
    def Speak(self):
        print('Bow Bow')

class Person:
    def Speak(self):
        print('Karakoo Karakooo')
def Display(obj):
    obj.Swim()
    obj.Speak()
    print('Information displayed')
D= Duck()
dog= Dog()
Display(dog)
P= Person()
Display(P)
