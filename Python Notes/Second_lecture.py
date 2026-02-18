# Example #02.1 string basic
"""
name="haroon"
print(name)
"""


#Example #02.2 Basic operation
"""
first_name="muhammad"
last_name="Haroon"
full_name=first_name+" "+last_name
print(full_name)
print(len(full_name))
"""


#Example #02.3 index and immutable  characters
"""
name="haroon1"
print(name[3])  #o

name+="rana"
print(name)  #haroon1rana

name[2]='h'
print(name[2])    #generate an error
"""

#Example #02.4 String Slicing
"""
Name="haroon1"
print(Name[0:6])    #haroon

onlyName=Name[0:6]
print(onlyName)     #haroon

print(Name[-7:-1])   #haroon
"""


# Example #02.5 function or operation of string
"""
string_name="we are study python form univeristy of azad jammu and kashmir, Pakistan"
print(string_name.endswith("tan"))      #Ture

string_intro=string_name.replace(string_name, "I am a student of CS")   #return new string 
print(string_intro)
print(string_name.find("python"))      #starting index of the find word

print(string_name.count('j'))       #count the occurrence of a particular word or character.
"""

# Example #02.6 conditional statement
"""
age =int(input("Enter your age "))
if(age>=18):
    print("Apply for ID cart", "and Can vote")
else:
    print("Does not eligible for ID cart")
    print("Can not vote")
print("The End")
"""

# Example #02.7 multiple if-else statement
"""
marks =int(input("Enter your marks "))
if(marks>100):
    print("Enter the valid marks ")
elif(marks>=90 and marks<=100):
    print("Supper")
elif(marks>=80 and marks<90):
    print("veryGood")
elif(marks>=70 and marks<80):
    print("Good")
elif(marks>=50 and marks<70):
    print("Fair")
else:
    print("Fail")

"""

#Example #02.6 check give number is positive or negative than check is they even or odd
num=int(input("Enter a number "))
if(num>=0):
    if(num%2==0):
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
else:
    if(num%2==0):
        print("The number is negative and even")
    else:
        print("The number is negative and odd")