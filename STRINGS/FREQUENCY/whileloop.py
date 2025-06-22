
# here we can find freq using counter


def freq_count(s):
    i = 0

    freq = {}

    while i < len(s):
        if s[i]  in freq:
            freq[s[i]] += 1
        
        else:
            freq[s[i]] = 1
        i += 1

    return freq

print(freq_count('rajkumaryadav'))