# in this we find a number is prime or not using different approaches
# 2 is the smallest even prime

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(0))

# using upto sqrt
# int(n**0.5)+1

def is_prime_num(n):

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# range of prime numbers

def prime_range(x, y):
    if x <= 1:
        return 'x must be greater than 2'
    primes = []

    for i in range(x , y+1):

        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
print(prime_range(4, 100))

# for-else
# else block will only run if for not broken