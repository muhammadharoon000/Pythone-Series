# Example 01 function
'''
#function definition 
def sum(a,b):
    return a+b
#function call
print('the sum of two number is= ',sum(3,4))
'''

# Example 02 function with default parameter
'''
def minus(a=1, b=0):
    return a-b
print("The subtraction of two number = ", minus())  #1
'''

# Example 03 reqursive function
def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)

print('The factorial of number is = ', factorial(5))        #120