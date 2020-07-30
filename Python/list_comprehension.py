'''

File: list_comprehension.py

Description: An introduction to python lists and list
comprehension methods

'''

'''
Theory: (Source : Data camp)

Other python data types available are (all "iterables"):
    tuples, dictionaries and sets

Tuples: "write-protect" data - cannot be changed
Dictonaries: Not ordered like lists, have "keys"
Sets: Stores unique and immuatable values, unordered that are hashable

Hashable: Hash value never changes
Hash Value: Unique fixed-length string (Binary value) associated with a given data.

How to check hash value of any thing on the commandline?

Ex: md5sum list_comprehension.py
8d495e23eaabdce39e2ead5e1d89f2d2  list_comprehension.py

Other alternatives to md5sum(message digest 5): sha1sum/sha224sum/sha256sum/sha512sum

Not hashable: List, Sets, Dictionaries
Hashable: Tuples, Floats/Strings/Integers

'''

# Create list using []

even = [2,4.0,6,8,10]

#print(f'all values in even list are {even} \n')

# accessing list elements: use index

#print(f'5th element of variable even is {even[4]} \n')

# using slices

#print(f'printing values after 4: {even[2:]} \n')

'''
List methods available:
    apprend()
    clear()
    copy()
    count()
    extend()
    index()
    insert()
    pop()
    remove()
    reverse()
    sort()
'''

# Using Python methods - Uncomment to check usage
'''
print(f'append(5) to even : {even.append(5)}\n')
print(f'copy() : {even.copy()}\n')
print(f'count(6) : {even.count(6)}\n')
print(f'extend() even : {even.extend([12,14])}\n')
print(f'all values in even list are {even} \n')
print(f'index(10) : {even.index(10)}\n')
print(f'insert(6,7) : {even.insert(6,7)}\n')
print(f'all values in even list are {even} \n')
print(f'pop() : {even.pop()}\n')
print(f'remove(5) : {even.remove(5)}\n')
print(f'all values in even list are {even} \n')
print(f'reverse() : {even.reverse()}\n')
print(f'all values in even list are {even} \n')
print(f'clear() even : {even.clear()}\n')
print(f'all values in even list are {even} \n')
'''

# Basic List comprehension syntax:
# list_var = [expr for item in collection]

'''
S = [x**2 for x in range(10)]
print(f'Values in List S are {S} \n')

V = [2**i for i in range(20)]
print(f'Values in List V are {V} \n')
'''

# Replacing list comprehension in place of
# map(), replace() and reduce()


