
# here we use while loop

# slicing based 
# it is less memoery efficient because each time we slice it creates new fresh string

# use index based for memory efficient

def rev_while_slice(s):
    res = ''
    
    while s:
        res = s[0] + res
        s = s[1::]
    return res
print(rev_while_slice('rajkumar'))

# INDEX BASED

def rev_while_index(s):
    i = 0
    res = ''

    while i < len(s):  # i = len(s)-1 ; while i >= 0
        res = s[i] + res
        i += 1

    return res
print(rev_while_index('surendrakumar'))



# checking

def reverse_str(s):
    i = len(s)-1
    res = ''

    while i >= 0:
        res += s[i]
        i -= 1

    return res
print(reverse_str('sunilkumar'))