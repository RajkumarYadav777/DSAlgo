
# here we will find a factoial of a number using different ways

# basic for loop

def fact(n):
    if n ==0 or n ==1 :
        return 1
    fact_of_n = 1
    
    for i in range(1, n+1):
        fact_of_n *= i

    return fact_of_n
print(fact(5))


# using list comprehension
# we have math module it contains some builtind
import math

def fact_math(n):
    res = math.factorial(n)
    return res
print(fact_math(5))

# using math.prod + lcomp

def fact_lcomp(n):
    res = math.prod([num for num in range(1,n+1)])
    res1 = math.prod(map(lambda x: x, range(1, n+1)))
    return res, res1
print(fact_lcomp(5))


# listcomp + without built-ins

def facto_lcomp(n):
    nums = [i for i in range(1, n + 1)]
    result = 1
    for num in nums:
        result *= num
    return result

print(facto_lcomp(5))  # Output: 120



from functools import reduce
# using reduce

def fact_reduce(n):
    res = reduce(lambda x, y : x * y, range(1, n+1))
    return res
print(fact_reduce(5))

                    

