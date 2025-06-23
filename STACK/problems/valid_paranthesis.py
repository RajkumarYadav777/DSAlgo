# here we find valid paranthesis problem using stack

# steps to solve
'''
1. intialize stack and  bracket_map = {')': '(', '}': '{', ']': '['}

2. traverse the string
    -> push if paranthesis is open 
    -> pop and match if char is a closing bracket

3. stack must be empty finally , 


# order is important, not just presence of pairs

'''

def is_valid_paranthesis(s):
    stack = []
    bracket_map = {')':'(', ']':'[', '}':'{'}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return len(stack) == 0
