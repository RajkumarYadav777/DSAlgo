
# to revese digits we have many ways

def reverse_digits(n):
    rev = ''
    for i in str(n):
        rev = i + rev
    return int(rev)
print(reverse_digits(3456))

# built-ins

# def built_rev(n):
#     res = reversed(str(n))
#     return int(res)
# print(built_rev(3456)) 
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'reversed'

def slice_rev(n):
    res = str(n)[::-1]
    return int(res)
print(slice_rev(3456))


# using lcomp
# we can also use list.reverse()

def lcomp_rev(n):
    res = [i for i in str(n)]
    # return int(''.join(res)[::-1])
    res.reverse()
    return int(''.join(res))
print(lcomp_rev(3456))

# using gen exp
def gen_rev(n):
    # res = reversed(x for x in str(n)) is not reversible
    res = (x for x in str(n))
    res1 = list(res)
    res1.reverse()
    return int(''.join(res1))
   
print(gen_rev(3456))


# using map

def map_rev(n):
    res = list(map(lambda x : x ,str(n)))
    res.reverse()
    return int(''.join(res))
print(map_rev(3456))