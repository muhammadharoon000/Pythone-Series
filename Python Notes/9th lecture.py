#Example No.1 delete object and attribute.
'''
class student:
    def __init__ (self, name, marks, RollNO):
        self.name=name
        self.marks=marks
        self.RollNO=RollNO
s1=student("Muhammad Haroon", 421, 35)
del s1.marks
#The name attribute was delete now we can not access
print(s1.marks)  #give an error

del s1
#So now stusent s1 object was delete we can not access and use
print(s1.name)   #Give an error
'''

# Example 02 private attribute
'''
class Account:
    def __init__(self, CN, Password):
        self.CN=CN
        self.__Password__=Password
    def changePassword(self):
        old=str(input("Enter the old password "))
        if(old==self.__Password__):
            new=""
            new=str(input("Enter the new password "))
            self.__Password__=new
        else:
            print("Enter the correct password ")
    def getPassword(self):
        return self.__Password__
A1=Account("Muhammad Haroon", 'haroon.15')
# print(Account.__Password__) #give an error because we going to access the private attribute out of the class
A1.changePassword()
print(A1.getPassword())
'''

# Example 3 Inheritance
'''
class person:
    def __init__ (self ,name):
        self.name=name
class stusent(person):
    def __init__(self, roll,name):
        super().__init__(name)
        self.rollnumber=roll
s1=stusent(45,'Haroon')
print(s1.name)
'''
#Example #4 Multi-level inheritance
'''
class Animal:
    def __init__ (self , name):
        self.name=name
class Mammal(Animal):
    def __init__ (self, name):
        super().__init__(name)
class Cat(Mammal):
    def __init__ (self ,name, sound):
        self.sound=sound
        super().__init__(name)
c1 =Cat("Lion","Roar")
print(c1.sound)
'''

#Example #5 Multiple inheritance
'''
class A :
    def __init__(self, A):
        self.A=A
class B:
    def __init__ (self, B):
        self.B=B
class C (A,B):
    def __init__(self, A, B,C):
        super().__init__(A)
        super().__init__(B)
        self.C=C
c1=C(1,2,3)
print(c1.A)     #2
'''
#Example #05 class method
'''
class Student:
    name="Unknow"
    # def ChangeName(self ,name):
    #     Student.name=name
    @classmethod
    def ChangeName(cls,name):
        cls.name=name
s1=Student()
s1.ChangeName("haroon")
print(s1.name)
print(Student.name)
'''

# Example #06 Properties Dectorator
'''
class Student:
    def __init__(self, name, math, phy, chem):
        self.name=name
        self.math=math
        self.phy=phy
        self.chem=chem
    @property
    def percentage(self):
        return (self.math+self.phy+self.chem)/3
    
s1=Student("Haroon", 89,56,78)
print(s1.name,"\t",s1.percentage)
'''

# Example #06 operator overloading
class complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    def __add__(self,c):
        real=self.real+c.real
        img=self.img+c.img
        return complex(real, img)
    def printNum(self):
        print(self.real,"i +",self.img)
c1=complex (8,4)
c2=complex (3,4)
c3=c1+c2
c3.printNum()