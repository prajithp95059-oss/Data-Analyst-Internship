'''class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()
class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()
'''
#single inhertance
'''class Parent:
    def father(self):
        print('i am father')

class Child(Parent):
    def child1(self):
        print('i am child 1')

c=Child()
c.child1()
c.father()'''
#multilevel inheritance
'''
class family:
    def father(self):
        print("DAD:i wont give my property to raghul if he weds shubisha")
class son(family):
    def raghul(self):
        print("raghul:i will marry GANGA  only")
class bro(son):
    def murugan(self):
        print("BRO:dad i will share my property to raghul beacause i support for his love")

class sis(bro):
    def aiswarya(self):
        print('this is sister')
s=sis()
s.murugan()
s.raghul()
s.father()
b=bro()
b.raghul()
'''
#multiple inheritance
'''class family:
    def father(self):
        print("DAD:i wont give my property to raghul if he weds shubisha")
class son:
    def raghul(self):
        print("raghul:i will marry GANGA  only")
class sis:
    def aiswarya(self):
        print('this is sister')
class bro(family,son,sis):
    def murugan(self):
        print("BRO:dad i will share my property to raghul beacause i support for his love")

obj=bro()
obj.father()
obj.aiswarya()
obj.raghul()
obj.murugan()'''



#hierarical 
'''
class family:
    def raghul(self):
        print("i am the father")
class mother(family):
    def ganga(self):
        print("i am the mother")
class child(family):
    def amaran(self):
        print("i am the child")
c=child()
c.amaran()
c.raghul()
'''


#hybrid
'''
class Parent:
    def father(self):
        print('i am father')

class Child(Parent):
    def child1(self):
        print('i am child 1')
class son:
    def raghul(self):
        print("raghul:i will marry GANGA  only")
class sis:
    def aiswarya(self):
        print('this is sister')
class bro(son,sis):
    def murugan(self):
        print("BRO:dad i will share my property to raghul beacause i support for his love")
c=child()
c.father()
b=bro()
b.aiswarya()
b.raghul()'''

































































































