

# in this approach i will use string reversing and comparing them simply tail

def is_palindrome(s):
    def helper(s, i, rev):

        # base case
        if i == len(s):
            return rev
        
        return helper(s, i+1, s[i]+rev)
    
    result = helper(s, 0, '')
    return result == s

print(is_palindrome('markram'))