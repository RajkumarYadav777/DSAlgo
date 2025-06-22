#  tail recursion build result along the way when it is reached base case it is ready to give result


# TAIL SLICE
def rev_tail_rec(s):
    def helper(s, rev):
        if not s:
            return rev
        
        return helper(s[1:], s[0]+ rev)
    return helper(s, '')
print(rev_tail_rec('rajkumar'))


# NOTE : here we can do like process before recursion call
'''
rev = s[0] + rev
return rev_tail_rec(s, rev)
 beacuse rev is maintaing state inside recursive call
'''


# INDEX BASED TAIL RECURSION

def rev_index_tail(s):
    def helper(s, i, rev =''):
        if i == len(s):
            return rev
        

        # pre processing
        rev = s[i]+ rev
        return helper(s,i+1, rev)
    return helper(s, 0)

print(rev_index_tail('surendrakumar'))