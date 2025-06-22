# i use normal recursion

def is_palindrome(s):

    def helper(s, i):

        # base case
        if i == len(s):
            return ''
        
        return helper(s, i+1) + s[i]
    
    result = helper(s, 0)
    return s == result

print(is_palindrome('markram'))
print(is_palindrome('madam'))
print(is_palindrome('madams'))