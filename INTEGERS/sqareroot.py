#  perfect squre root means n*n==x ; n is the squre root of a number
# sometimes there could non-perfect squres exisits so where we return floor values of them
# n*n < x , we store it in result as res = n
# because thee could be higher value tha still n*n < x so we keep update it


# we have some builtins 

import math

def sq_root(n):
    return math.sqrt(n) #math.pow(n, 0.5)

# using ** operator ; as sqrt means ; squre of a number with ** 0.5

def sq_pow(n):
    # we can use 
    return n ** 0.5


# using divide and conquer
# negatives no squre root
# 0 and 1 number itself

def sqrt_dc(n):
    if n < 0:
        return None 
    if n == 0 or n == 1:
        return n
    low = 0
    high = n
    result = 0 # to store non perfect 

    while low <= high:
        mid = (low+high)//2

        if mid * mid == n:
            return mid
        elif  mid * mid <= n:
            result = mid
            low = mid+1
        else:
            high = mid-1
    return result
print(sqrt_dc(35))