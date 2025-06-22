

# here to find palindrome we frst reverse string and compare it with original


def is_palindrome(s):

    reverse_str = ''

    for char in s:
        reverse_str = char + reverse_str
    
    if s == reverse_str:
        print(f"{s} is valind palnindrome")
    else:
        print(f"{s} is not valid palindrome")

is_palindrome('markram')
is_palindrome('dangered')


# we can use another way using single pointer witout reversing


def is_palindrome_without_reverse(s):
    n = len(s)

    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False
    return True

print(is_palindrome_without_reverse('markram'))