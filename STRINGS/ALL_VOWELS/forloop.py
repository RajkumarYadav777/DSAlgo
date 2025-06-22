# here we check the given string contains all the vowels

def find_all_vowels(s):
    # frst we need to build initial_vowels freq
    vowel_freq = dict.fromkeys('aeiou',0)

    for ch in s:
        if ch in vowel_freq:
            vowel_freq[ch] += 1
    
    for key in vowel_freq:
        if vowel_freq[key] == 0:
            return False
    return True

print(find_all_vowels('i love an umbrella'))



# another way is find vowel frequencies and check if all vowel keys are there or not

def find_another_way(s):
    vowels = set('aeiou')
    freq = {}
    for ch in s:
        if ch in vowels:
            freq[ch] = freq.get(ch, 0) + 1
    
    for vowel in 'aeiou':
        if vowel not in freq:
            return False
    
    return True

print(find_another_way(' i love yo india'))
