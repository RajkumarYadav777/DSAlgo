# here we check the given string is palindrome
# 1. build the stack using first half
# 2. find the start position of secod half
# 3. loop through second half and compare it with stacks pop 



def is_pal(s):
    n = len(s)
    stack = []
    for i in range(n//2):
        stack.append(s[i])
    
    # find n is odd or even 
    start = (n//2) if n % 2 == 0 else (n//2+1)

    for i in range(start, n):
        if not stack or stack.pop() != s[i]:
            return False
    return True
print(is_pal('markramr'))
    