

# TAIL RECURSION


def rev_alnums_tail(s):

    def helper(s, i, j):
       

        if i > j :
            return ''.join(s)
        
        if not s[i].isalnum():
            return helper(s, i+1, j)
        elif not s[j].isalnum():
            return helper(s, i, j-1)
        else:
            s[i],s[j] = s[j], s[i]
            return helper(s, i+1, j-1)
    return helper(list(s), 0, len(s)-1)
print(rev_alnums_tail('rajkumar$yadav'))




# DIFFERENT VERSION 
def reverse_alnum_only(st):
    def helper(i, j, lst):
        if i >= j:
            return  # No need to return anything, we're modifying in place

        if not lst[i].isalnum():
            helper(i + 1, j, lst)
        elif not lst[j].isalnum():
            helper(i, j - 1, lst)
        else:
            lst[i], lst[j] = lst[j], lst[i]
            helper(i + 1, j - 1, lst)

    lst = list(st)
    helper(0, len(lst) - 1, lst)
    return ''.join(lst)
