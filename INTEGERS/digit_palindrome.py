 # here we find a number is palindrome
# if we reverse number it modifies original
# so we keep it in temp for reversing

def is_digit_palindrome(n):
    temp = n
    rev = 0

    while temp > 0:
        dig = temp % 10
        rev = dig + rev*10
        temp = temp // 10
    if rev == n:
        return True
    
    return False
print(is_digit_palindrome(345463))
    