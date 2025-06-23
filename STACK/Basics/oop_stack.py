# here we build stack using oops 
# operations to build
# push, pop, peek, is_empty, size

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('stack is empty, cannot pop')
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('stack is empty. cannot peek')
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f'Stack (top -> bottom) : {self.items[::-1]}'

st = Stack()

# we reverse string using custom stack class


def rev_string(s):
    stack = Stack() # we will get access to class attribs and methods

    for char in s:
        stack.push(char)
    
    rev_str = ''

    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

print(rev_string('rajkumar'))