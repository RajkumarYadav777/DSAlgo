

# normal recursion is  something , goes to base case and process from bottom up and return res


# NORMAL(SLICING)

def rev_norm_rec(s):

    def helper(s):
        if not s:
            return ''
        
        return helper(s[1:]) + s[0]
    return helper(s)

print(rev_norm_rec('rajkumar'))


# USING LAST ITEM THROUGH SLICING

def rev_last_norm_rec(s):

    def helper(s):

        if not s:  # if s == '':
            return ''
        
        return s[-1] + helper(s[:-1])
    return helper(s)

print(rev_last_norm_rec('surendrakumar'))


# INDEX BASED

def rev_index_rec(s):

    def helper(s,i):
        if i == len(s):
            return ''
        
        return helper(s, i+1) + s[i]
    return helper(s, 0)

print(rev_index_rec('sunilkumar'))

