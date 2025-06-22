
# here we use freq counter pattern

def freq_pattern(s):
    freq = dict.fromkeys(s, 0)

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    return freq

print(freq_pattern('rajkumaryadav'))