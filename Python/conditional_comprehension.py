'''

File: conditional_comprehension.py

Description: An introduction to python list
comprehension methods used with conditional statements

'''
import numpy as np

kilometer = [39.3,56.5,88.4,91.9,94.3,100]
feet = [float(3280.8399)*x for x in kilometer]
feet_int = list(map(int,feet))
#print(f'feet_int contains {feet_int}')

#uneven = [x for x in feet_int if x%2!=0]

# uneven = [x/2 for x in feet_int if x%2==0]

#print(uneven)

uneven = [x for x in range(100) if x%3==0 if x%4==0]

#print(f'numbers divisible by 12 within 100 are {uneven}\n')

#random_num = [print(f' {x} divisible by 5') if x%5==0 else print(f'{x} not diviible by 5') for x in range(2,100,17)]

list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
#flattened = [y for x in list_of_list for y in x]
#flattened = [y for x in list_of_list for y in x]
#print(f'flattened list is {flattened}')

#transpose = [[(row,i) for row in list_of_list] for i in range(3)]
transpose = [[row[i] for row in list_of_list] for i in range(3)]
print(f'transpose matrix is {transpose}\n')

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(np.size(matrix))

# using for loop
transposed = []
for i in range(3):
    transposed_row = []
    for row in matrix:
        print(f'row,i is {row,i}\n')
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
