
# here we use Counter for vowels= freq

from collections import Counter

def vowels_freq(s):
    vowels  = set('aeiouAEIOU')
    vowel_list = [i for i in s if i in vowels]
    return Counter(vowel_list)
print(vowels_freq(' i love you india'))

# using dict comprehension

def dict_comprehension(s):
    vowels = set('aeiouAEIOU')
    vowel_freq = {key:s.count(key) for key in s if key in vowels}
    return vowel_freq
print(dict_comprehension(' i love you india'))


# COUNTING

def vowels_count(s):
    vowels = set('aeiouEIOU')
    res = sum(1 for i in s if i in vowels)
    # sum(s.count(i) for i in s if i in vowels)
    return res
print(vowels_count('i love you india'))