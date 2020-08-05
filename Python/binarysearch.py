'''

File: binarysearch.py
Description: Binary search algorithm implementation in python

'''
import random as rand

def findindex(numlist,begin,end,num):
    list_len = len(numlist)
    if end>=begin:
        center = begin + (end-begin)//2

        if(numlist[center]==num):
            return center
        elif numlist[center]>num:
            return findindex(numlist,begin,center-1,num)
        elif numlist[center]<num:
            return findindex(numlist,center+1,end,num)
    else:
            print(f'{num} not found in {numlist}\n')
            return -1


#array = [4,8,1,5,3,2,9]
array = rand.sample(range(20,50),20)
sort_list = sorted(array)

searchNum = rand.randint(min(array),max(array)+1) 
print('\tBinary Search Demo\n')
print(f'Checking if {searchNum} is present in {sort_list}\n')
ret_val = findindex(list(sort_list),0,len(array)-1,searchNum)
if(ret_val!=-1):
    print(f'{searchNum} found at Index : {ret_val}\n')
print(f'\tBinary Search...DONE\n')
