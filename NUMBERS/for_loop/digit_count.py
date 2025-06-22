
# here we count number of digits in a given number

def coun_digits_naive(n):
    count = 0
    for i in str(n):
        count += 1
    return count
print(coun_digits_naive(3456))

# built-in

def built_count(n):
    return len(str(n))
print(built_count(3456))

# lcom  + 1

def lcomp_count(n):

    res = sum([1 for _ in str(n)])
    res1 = len([i for i in str(n)])
 
    res3 = len(list(map(lambda x : x , str(n))))
    return res, res1,  res3
print(lcomp_count(3456))

# using gen exp

def gen_count(n):
    res = list(x for x in str(n))
    return len(res)
print(gen_count(3456))


# using log10
import math
def count_digit(n):
    res  = math.floor(math.log10(n) + 1)
    return res
print(count_digit(3456))