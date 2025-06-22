# armstrong number is also called  narcissistic number
# sum of each digit raiseed to the power of n == original number

def is_armstrong(n):
    temp = n
    res = 0
    # we must find digits
    digits = len(str(n))

    while temp > 0:
        dig = temp % 10
        res += (dig**digits)
        temp //= 10
    if res == n:
        return True
    return False
print(is_armstrong(143))


# to count number of digits we have another way

import math

n = 9474

print(math.floor(math.log10(n)+1))