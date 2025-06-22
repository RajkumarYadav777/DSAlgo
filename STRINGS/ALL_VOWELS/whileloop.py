
# we use while loop

def find_all_vowels(s):
    vowels = dict.fromkeys('aeiou', 0)
    i = 0

    while i < len(s):
        ch = s[i]
        if ch in vowels:
            vowels[ch] += 1
        i += 1
    
    keys = list(vowels.keys())
    j = 0

    while j < len(keys):
        ch = keys[j]
        if ch not in vowels:
            return False
        j += 1
    return True

print(find_all_vowels('i love you india'))
        
    
