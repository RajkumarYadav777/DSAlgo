
# here we print sum of n numbers
# we have formual that, sum of n natural numbers is n*(n+1)//2


def sum_n(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
print(sum_n(10))


# using formula

def sum_formula(n):

    res = n * (n + 1)//2
    return res
print(sum_formula(10))


# using list comp

def sum_lcm(n):
    res = sum([num for num in range(n+1)])
    return res

print(sum_lcm(10))



# we can us pure functional way using reduce method

from functools import reduce

def sum_reduce(n):
    res = reduce(lambda x, y : x +y, range(n+1))
    return res
print(sum_reduce(10))




# using map

def sum_map(n):

    res  = sum(map(lambda x : x, range(n+1)))
    return res
print(sum_map(10))