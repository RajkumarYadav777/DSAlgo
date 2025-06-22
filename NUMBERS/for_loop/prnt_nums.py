# here we print numbers from 1 to N

def print_nums(n):
    for num in range(n+1):
        print(num)

print_nums(10)




# we use list comprehension for code simplicity

def prnt_nums_lcmp(n):

    return [num for num in range(n + 1)]
print(prnt_nums_lcmp(10))


# we use map
# return map object we need consume using list/tuple containers

def map_num(n):

    res = '-'.join(map(lambda x: str(x), range(n +1)))  # return map object
    return res
print(map_num(10))


def map_print(n):

    res = map(lambda x:x , range(n +1))
    return list(res)
print(map_print(10))