#!/usr/bin/python3
class Person:
    id = 0
    def __init__(self):
        self.id = 1

    def say_hi(self):
        print('Hello, my name is')

p = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()
print(p.id)
print(p2.id)
print(p3.id)
print(p4.id)
print(p5.id)
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()