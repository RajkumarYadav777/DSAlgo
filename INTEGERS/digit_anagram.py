# here we find one number is anagram of another number
# anagram = same number +same freq + maybe in different order

def anagram_digits(n1, n2):
    return anagram(n1) == anagram(n2)

def anagram(n):
    freq = [0]*9

    while n > 0:
        dig = n % 10
        freq[dig] += 1
        n //= 10
    return freq

print(anagram_digits(3456, 6345))
