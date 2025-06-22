# check if any substring is valid palindrome


def check_pal_substr(s, k):
    if k > len(s):
        return False
    
    for i in range(len(s)-k+1):
        window = s[i:i+k]

        if window == window[::-1]:
            return True, window
        
    return False

print(check_pal_substr('abcdefdfs', 3))


# using helper function

def is_pal(s):
    left = 0, right = len(s)-1

    while left < right:

        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def any_pal_substr(s, k):

    if k > len(s):
        return False
    
    for i in range(len(s)-k+1):
        window = s[i:i+k]

        if is_pal(window):
            return True
    return False
