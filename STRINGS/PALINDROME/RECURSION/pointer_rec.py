
# here we use two pointers tchnique using recursion


def is_palindrome(s):

    def helper(s, left, right):
        
        # base case
        if left > right:
            return True
        
        if s[left] != s[right]:
            return False
        
        return helper(s, left+1, right-1)
    return helper(s, 0, len(s)-1)
print(is_palindrome('markram'))