# here we find a fatorial of a number
# 0 and 1 factorial is always 1

def fact_num(n):
    if n <= 1:
        return 1
    fact = 1
    for num in range(1, n+1):
        fact *= num
    return fact
print(fact_num(5))

# we use built in math module

import math

def facto(n):
    return math.factorial(n)
print(facto(5))