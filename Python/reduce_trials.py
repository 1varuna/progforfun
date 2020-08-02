'''
Python script exploring reduce()

reduce() - defined in C - internal looping faster than python

'''
from functools import reduce

# define a simple function to add two numbers
def my_add(a,b):
    result = a+b;
    print(f'{a} + {b} = {result}')
    return result

#print(f'my_add(2**5,2**6) is {my_add(2**5,2**6)}')

numbers = range(2,10)
print(f'chosen numbers are: {list(numbers)}')
#print(f'sum of numbers is : {reduce(my_add,numbers)}')

initializer = 0
#print(f'sum of numbers is : {reduce(my_add,numbers,0)}')


# 1 line definition of my_add using lambda functions

#final_sum = reduce(lambda a,b:a+b,numbers,0)
final_sum = reduce(lambda a,b:a+b,numbers,0)

#print(f'sum of numbers (using lambda) : {final_sum}')

from operator import add

#print(f'sum of numbers (using add) : {reduce(add,numbers,0)}')

def my_prod(v1,v2):
    print(f'{v1}*{v2} = {v1*v2}')
    return v1*v2

#print(f' products of values in numbers[] : {reduce(my_prod,numbers)}')

product = reduce(lambda a,b:a*b,numbers)
#print(f'sum of numbers (using lambda) : {product}')

# Method to check if any value is true
def check_any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False

print(f'check_any_true([1,0,1,0,1,0]) = {check_any_true([1,0,1,0,1,0])}')

# Method to check if any value is true
def check_all_true(iterable):
    for item in iterable:
        if not item:
            return False
    return True

print(f'check_all_true([1,0,1,0,1,0]) = {check_all_true([1,0,1,0,1,0])}')
