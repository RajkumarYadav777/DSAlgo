# happy number is 
# sum of sques of digits == 1
# if number is not a happy number it keeps on stuck in loop 
# if we found cycle we immediately return false

def is_happy_number(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        sum = 0
        while n > 0:
            dig = n % 10
            sum += (dig ** 2)
            n //= 10
        n = sum
    return True
print(is_happy_number())