#Example #01 basic syntax
'''
#Class Definition
class student:
    name="Haroon "
    def addsecondName(self, lastname):
        self.name+=lastname
#creating an object
s1=student()
s1.addsecondName("Rana")
print(s1.name)
'''

#Example #02 constructor
'''
class student:
    def __init__(self, name , marks, rollnumber):
        self.name=name
        self.marks=marks
        self.rollnumber=rollnumber

    def PrintInfo(self):
        print("Name \t\t\t RollNO. \t Marks")
        print(self.name,"\t" ,self.rollnumber, '\t',self.marks)
s1=student("Muhammad Haroon", [56,78,95], 35)
s1.PrintInfo()
'''
# Example #03 static_method
'''
class student:
    name="Muhammad "
    def __init__(self, name , marks, rollnumber):
        self.name+=name
        self.marks=marks
        self.rollnumber=rollnumber
    @staticmethod
    def getCollege():
        print("University Of AJK")
s1=student("Ali", 45, 90)
student.getCollege()
print(student.name)     #class attribute
print(s1.name, s1.marks)    #object attributes
'''



