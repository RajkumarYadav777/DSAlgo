# here we use stack to reverse string
# 1. firs build the stack 
# 2. pop and build reverse string

def string_reverse(s):
    stack = []

    # build the stack
    for char in s:
        stack.append(char)
    
    # pop and build
    rev_str = ''
    while stack:
        rev_str += stack.pop()
    return rev_str
print(string_reverse('rajkumar'))