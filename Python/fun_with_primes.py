'''
File: fun_with_primes.py

Description: 
Check, print number of primes
and find sum within a given range

Uses list comprehension to compute values
'''

num_range = input(f'Enter a range \t')
numbers = range(2,int(num_range))
print(f'chosen numbers are: {list(numbers)}\n')

# Idenify prime number
def is_prime(a):
    if(a>1):
        flag = 1
        for i in range(2,a):
            if(a%i!=0):
                flag+=1
            else:
                #print(f'{a} is not prime')
                return False
        if(flag>1 or a==2):
            #print(f'{a} is prime')
            return True
    else:
        print(f'Enter a number greater than 1')

#check_prime = [is_prime(x) for x in numbers]
#print(f'{check_prime}')    # prints return value, based on number being prime or not

prime_count = 0
num_prime = [prime_count+1 for x in numbers if is_prime(x)==True]

print(f'Total number of prime numbers from 2 to {max(numbers)} is {sum(num_prime)}\n')

yes_prime = []
sum_primes = [yes_prime.append(x) for x in numbers if is_prime(x)==True]
print(f'sum of prime numbers from 2 to {max(numbers)} is {sum(yes_prime)}\n')
