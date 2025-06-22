from collections import defaultdict
def vowels_count(s):
    vowels = set('aeiou')
    
    for vowel in vowels:
        if vowel not in s:
            return False
    return True
    
print(vowels_count('i love  u my india'))


# using all
def present_all_vowles(s):
    vowels = set('aeiou')
    
    # edgecase
    if len(vowels) > len(s):
        return False
    
    return all(vowel in s for vowel in vowels)
print(present_all_vowles('i love u my india'))


'''
NOTE:
    1- all() is best for when we use freq = dict.fromkeys(vowels, 0)
    2. {} or defaultdict(int) is best when we use freq[ch] = freq.get(ch, 0)+1 or freq[ch] +=1 for defaultdict

    when we use all for these two approaches it returns true because these methods ignore the not present char




'''


def check_all_vowels(s):
    vowels = set('aeiou')
    freq = defaultdict(int)
    # freq = {}

    for ch in s:
        if ch in vowels:
            # freq[ch] += 1
            freq[ch] = freq.get(ch, 0) + 1
    
    return len(freq)==len(vowels)
print(check_all_vowels('i love u my india'))