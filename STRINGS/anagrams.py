

def str_anagram(s1, s2):
    return anagram(s1) == anagram(s2)

def anagram (s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0)+1
    return freq

print(str_anagram('rajkumar', 'ramukjar'))