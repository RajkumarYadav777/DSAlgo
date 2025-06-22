# here we find fib seqence

# tuple unpacking way

def fib_seq(n):
    # if n <= 1:
    #     print(0)
    #     return
   
    a,b = 0, 1

    for _ in range( n):
        print(a)
        a,b=b, a+b
fib_seq(10)

# return as a list

def fib_list(n):
    a,b = 0,1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq
print(fib_list(10))


# efficient way

def fib_sequence(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    fib = [0,1]
    for _ in range(2,n):

        fib.append(fib[-1]+fib[-2]) # we add last two values fom a list

    return fib
print(fib_sequence(10))