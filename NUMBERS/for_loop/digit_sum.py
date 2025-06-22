
# here we calculate digit sum using various way

def sum_of_digit(n):
    sum = 0

    for i in str(n):
        sum += int(i)
    return sum
print(sum_of_digit(3456))


# comp + sum

def comp_sum(n):
    res = sum([int(x) for x in str(n)])
    return res
print(comp_sum(3456))

# generator exp

def gensum(n):
    res = sum(int(x) for x in str(n))
    return res
print(gensum(3456))

# using map

def map_sum(n):
    res = list(map(lambda x : int(x), str(n)))
    return sum(res)
print(map_sum(3456))

# using reduce
from functools import reduce

def reduce_sum(n):
    res = reduce(lambda x, y: int(x) + int(y), str(n))
    return res
print(reduce_sum(3456))