
# here we find first non repeating chracter from a sti=ring

def frst_non_repeating(s):
    freq = {} # use OrderedDict() for order preserving

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for key, val in freq.items():
        if val == 1:
            return key
    return 'no non repeating char is in the string'
print(frst_non_repeating("aabbcde"))


# we can use s.count(char)==1 ; return char ; but slow for larger strings

from collections import Counter
def first_non_repeat(st):
    freq = Counter(st)

    for char in st:
        if freq[char] == 1:
            return char
    
    return 'no non-repeating char'



