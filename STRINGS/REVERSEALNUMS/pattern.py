
# we use two pointers

# TWO POINTERS



def rev_only_alnum(s):
    l = 0
    r = len(s)-1
    lst = list(s)

    while l < r:

        if not lst[l].isalnum():
            l += 1
        
        elif not lst[r].isalnum():
            r -= 1
        
        else:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
    return ''.join(lst)

print(rev_only_alnum('rajkumar$yadav'))
            