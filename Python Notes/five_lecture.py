# Example 01 while loop
'''
num =10
while(True):
    if(num==5):
        break
    print(num)   # 10 9 8 7 6
    num=num-1
    '''

#Example 02 for loop
'''
num=[23,45,23,67,45,32,12]
count=0
for el in num:
    print(count,":", el)
    count+=1
print("End")
'''

# Example 03 range function
'''
num=range(1,5,2)
print(num)
for el in num:
    print(el)
print('The End')
'''

# Example 04 pass statement
'''
for el in range(2):
    pass
'''

# Example 05 break and continue
num=0
while(True):
    num+=1
    if(num%2!=0):
        continue
    if(num>100):
        break
    print(num)
print("Value of num where break ", num)  #102