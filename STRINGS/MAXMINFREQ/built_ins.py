# we use some built in techniques to solve

from collections import Counter

def mx_mn_freq(st):
    freq = Counter(st)
    mx = max(freq, key = lambda key:freq[key])
    mn = min(freq, key = lambda key: freq[key])
    return (mx, freq[mx]), (mn, freq[mn])
print(mx_mn_freq('rajkumaryadav'))


# another version

def both_chr_count(st):
    
    freq = Counter(st)
    items = freq.items()
    mx = max(items, key=lambda item: item[1])
    mn = min(items, key=lambda item: item[1])

    return mx, mn
print(both_chr_count('rajkumaryadav'))