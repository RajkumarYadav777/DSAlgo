
# we use index based reversing 

def is_palindrome(st):
    i = 0
    rev = ''
    while i < len(st):
        rev = st[i] + rev
        i += 1

    return f'{rev == st}'

print(is_palindrome('markram'))