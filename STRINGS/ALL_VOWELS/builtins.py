def all_vowels_present(s):
    vowels = set('aeiou')
    s_lower = s.lower()

    present_vowels = {ch for ch in s_lower if ch in vowels}

    return present_vowels == vowels

print(all_vowels_present('i love u india earth ocean'))


# using generator expression + all

def gen_exp(s):
    vowels = set('aeiou')
    s_lower = s.lower()

    # return all(ch in vowels for ch in s_lower)
    # we should check each vowel presnt in string
    return all(vowel in s_lower for vowel in vowels)
print(gen_exp(' i love you india'))


# dict_comp

def dict_comp(s):
    vowels = set('aeiou')
    s = s.lower()

    freq = {key : s.count(key) for key in vowels}
    return all(freq[key]>0 for key in freq)
print(dict_comp('i love you india'))


# we also use issubset
# it checks if all the vowels present in string
def use_issubset(s):
    vowels = set('aeiou')

    return vowels.issubset(set(s.lower()))
print(use_issubset(' i love you inida'))