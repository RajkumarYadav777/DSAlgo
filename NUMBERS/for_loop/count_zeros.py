
# we count 0s in a given number

def zero_count(n):
    count = 0
    if n == 0:
        count = 1
        return count
    if 1 < n < 9: # single digit other than 0
        count = 0
        return count
    
    for i in str(n):
        if int(i) == 0:
            count += 1
    return count
print(zero_count(8))



# using str.count()

def str_count(n):
    return str(n).count('0')
print(str_count(23040))

# using list comp + sum

def list_count_zero(n):

    res = sum([1 for i in str(n) if int(i) == 0])
    return res
print(list_count_zero(203040))


# with filter function + sum

def filter_zero_count(n):
    res = filter(lambda x : int(x) == 0, str(n))
    return len(list(res))
print(filter_zero_count(102030))

# using generator comp

def generator_count(n):
    res = list(int(x) for x in str(n) if x == '0')
    return len(res)
print(generator_count(102030))

# using set

def set_count(n):
    st = {0}
    count = 0

    for i in str(n):
        if int(i) in st:
            count += 1

    return count
print(set_count(102030))