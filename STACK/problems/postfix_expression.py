# postfix evaluation(Reverse polish notation)
# in this operators comes after operands
# evaluates left to right


# steps to solve
'''
1. initialize stack
2. loop through expression
   -> if char is digit push 
   -> if operand pop two values ; first is right and second is left 
   -> operate and push result back to stack


'''

def postfixexpression(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))

        elif char in '+-*/':
            if len(stack) < 2:
                raise ValueError(f"Invalid expression: not enough operands before '{char}'")
            
            right = stack.pop()
            left = stack.pop()

            if char == '+':
                result = left + right
            elif char == '-':
                result = left - right
            elif char == '*':
                result = left * right
            elif char == '/':
                result = int(left / right)
            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid expression: leftover operands or no result")
    # stack contains only one item at the end
    return stack.pop()