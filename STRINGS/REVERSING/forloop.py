
# we do string reversing possible ways

# FOR EACH LOOP

def reverse_foreach(s):
    res = ''
    for char in s:
        res = char + res
    return res

print(reverse_foreach('rajkumar'))


# INDEX BASED

def reverse_forindex(s):
    res = ''
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

print(reverse_forindex('surendrakumar'))

# SLICING

def rev_slice(s):

    return s[::-1]
print(rev_slice('sunilkumar'))



def reverse_list(ls):
    n = len(ls)

    for i in range(n//2):
        ls[i],ls[n-1-i] = ls[n-1-i],ls[i]

    return ls
    

print(reverse_list([1,2,3,4,5]))