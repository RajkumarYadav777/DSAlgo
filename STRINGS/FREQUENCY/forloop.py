
from collections import Counter
# using for each loop

def freq_chars(s):
    # freq = dict.fromkeys(s,0)
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq
print(freq_chars('rajkumaryadav'))


# using string.count + dict comprehesnsion

def freq_comp(s):
    return {char: s.count(char) for char in s}
print(freq_comp('rajkumaryadav'))


# using counter

def freq_counter(s):
    return Counter(s)
print(freq_counter('rajkumaryadav'))