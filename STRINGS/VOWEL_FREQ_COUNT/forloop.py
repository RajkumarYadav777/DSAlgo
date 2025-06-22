

# in this file we do both vowels frequency and vowels count
# freq pattern
def vowel_freq(s):
    vowels = set('aeiouAEIOU')
    freq = {}

    for ch in s:
        if ch in vowels:
            freq[ch] = freq.get(ch, 0) + 1
    return freq
print(vowel_freq('i love my india'))

# manual freq

def vowel_freq_manual(s):
    vowels = set('aeiouAEIOU')
    freq = dict.fromkeys(vowels,0)

    for ch in s:
        if ch in vowels:
            freq[ch] += 1  # it gives vowels that is 0 occurrence
        
        
    return {k:v for k, v in freq.items() if v>0}
print(vowel_freq_manual('i love you india'))


# the manuala way
def maual_vowel_freq(s):
    vowels = set('aeoiuAEIOU')
    freq = {}

    for ch in s:
        if ch in vowels:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    return freq
print(vowel_freq_manual('i love you india'))




# COUNTING
def counting_vowels(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    
    return count
print(counting_vowels('i love you india'))

