# here we solve prefix expression
# it is exactly same as postfix but evaluates from right to left


def prefixexpression(expression):
    stack = []
    operators = set('+-*/')

    for char in reversed(expression):
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            if len(stack) < 2:
                raise ValueError('stack must contain two operands to perform')
            
            left = stack.pop()
            right = stack.pop()

            if char == '+':
                result = left + right
            elif char == '-':
                result = left - right
            
            elif char == '*':
                result = left * right
            elif char == '/':
                result = int(left / right)
            
            stack.append(result)
    if len(stack)  > 1:
        raise ValueError('stack must contain one item, multiple operands are left over')
    
    return stack.pop()