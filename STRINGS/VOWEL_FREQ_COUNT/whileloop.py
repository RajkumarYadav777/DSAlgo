
# vowels freq
# freq.get() is the KeyError safe

def vowels_freq(s):
    freq = {}
    vowels = set('aeiouAEIOU')
    i = 0
    while i<len(s):
        if s[i] in vowels:
            freq[s[i]] = freq.get(s[i], 0) + 1
        i += 1
    return freq
print(vowels_freq(' i love you inida'))



# COUNTING

def vowels_count(s):
    vowels = set('aeiouAEIOU')
    count = 0
    i = 0

    while i < len(s):
        ch = s[i]
        if ch in vowels:
            count += 1
        i += 1
    return count
print(vowels_count(' i love you india'))
    
