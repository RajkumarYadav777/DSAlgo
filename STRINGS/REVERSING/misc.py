# here some of the other ways to reverse string

# LIST COMP
# list comprehension is used for build list sequences
# when we use that we need to join using join method


def rev_lcomp(s):
    res = [char for char in s]
    return ''.join(res[::-1])   # l = list(s); ''.join(l[::-1])

print(rev_lcomp('rajkumar'))

# MAP
# using map it returns map object
# it is for transorming iterable, it takes function and apply it on each item in iterable
# later we need to constructor to consume it

def rev_map(s):
    res = map(lambda char:char, s)
    return ''.join(reversed(list(res)))
print(rev_map('surendrakumar'))

# NOTE : map object is not reversible, so we need use list constructor


# LIST.REVERSE()
# REVERSED() BUILT IN 

def rev_reverse(s):
    l = list(s)
    l.reverse()
    return  ''.join(l)
print(rev_reverse('sunilkumar'))



def rev_reversed(s):
    res = reversed(s)
    return ''.join(res)
print(rev_reversed('suryakumar'))


# POP()
# pop is list method that removes last item and returns it

def rev_pop(s):
    lst = list(s)
    res = ''
     
    for _ in range(len(lst)):
        res += lst.pop()
    return res

print(rev_pop('subramanyam'))

