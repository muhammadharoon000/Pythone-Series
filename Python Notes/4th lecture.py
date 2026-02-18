# Example #01 Dictionary
'''
student={
    "name":"muhammd haroon",
    "Roll_num":35,
    "marks":431
}
print(student)
'''

# Example #02 value accessing in Dictionary
'''
student={
    "name":"muhammd haroon",
    "Roll_num":35,
    "marks":431
}
print(student["name"])
'''
# Example #03 Dictionary operation
'''
student={
    "name":"muhammd haroon",
    "Roll_num":35,
    "marks":431
}
print(student.keys())  #Return all the key

print(student.values())     #Return all the value

student["ph#"]="0312834078"   #add new key:value pair

student.update({"name" :'Aqeel'})   #udate the value of specific key

print(student.items())      #Return or print the key-value pair of the dictionary

print(student.get("name"))      #Return the value of key that pass in function call
print(student)
'''

# Example 04 set
'''
num={1,2,1,3,4,5}
print(num)      #duplicate value are ignored
'''

# Example 05 set method
num={1,7,1,2,4,5}
num.add(6)      #add new element
print(num)  

num.remove(1)       #remove the element
print(num)  

# num.clear()     #delete all element of set
print(num)  

print(num.pop())
print(num)  

num2={2,6,7,5,9}
num3=num.union(num2)
print(num3) 

num4=num.intersection(num2)
print(num4)