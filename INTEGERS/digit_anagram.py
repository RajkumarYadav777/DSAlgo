# here we find one number is anagram of another number
# anagram = same number +same freq + maybe in different order

def anagram_digits(n1, n2):
    return anagram(n1) == anagram(n2)

def anagram(n):
    freq = [0]*10
    # You're creating a list with indexes 0 through 8 only using [0]*9. That means:
    # Index 9 is not available
    # So, if your number contains the digit 9, this line will fail: freq[9] += 1  # ❌ IndexError: list index out of range
    while n > 0:
        dig = n % 10
        freq[dig] += 1
        n //= 10
    return freq

print(anagram_digits(3456, 6345))
