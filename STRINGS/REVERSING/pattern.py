

# here we use two pointer technique to reverse a string
# we use left and right pointers and move inwards until they met/cross

# TWO POINTERS


# string does not support item assignment so we need to convert it list and join the result
# in-place reversing

def rev_twopointers(s):

    left = 0
    right = len(s) - 1
    l = list(s)

    while left  < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1

    return ''.join(l)

print(rev_twopointers('rajkumar'))


