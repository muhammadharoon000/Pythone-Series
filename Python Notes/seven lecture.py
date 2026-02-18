# Example #01 file handleing basic
'''
file=open("sample.txt", 'r')
data=file.read()
print(data)
file.close()
'''

#Example #02 Line by line reading
'''
file =open("sample.txt", 'r')
while True:
    data=file.readline()
    if not data:
        break
    print(data.strip())
file.close()
'''
#Example #04 write in the file
'''
f=open("sample.txt", 'w')
f.write("I am student of computer science \n")
f.write("I Studey in University of Ajk \nI am form muzaffarabad \n")
f.write("Pakistan")
f.close
file =open("sample.txt", 'r')
while True:
    data=file.readline()
    if not data:
        break
    print(data.strip())
file.close()
'''


#Example #03: with syntax:
"""
with open("sample.txt", 'r')as f:
    data=f.readline()
    while data:
        print(data.strip())
        data=f.readline()
        #Automatically close file 
"""

# Example #04 deleting a file
'''
import os
os.remove("sample.txt")
'''

