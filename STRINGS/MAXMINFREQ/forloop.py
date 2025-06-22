
# here we use manually find frequency and its max


def max_min_freq(st):

    freq = {}

    for ch in st:
        freq[ch] = freq.get(ch, 0) + 1

    mx_val = float('-inf')
    mn_val = float('inf')
    mx_pair = None
    mn_pair = None

    for key, val in freq.items():
        if val > mx_val:
            mx_val = val
            mx_pair = (key, mx_val)

        if val < mn_val:
            mn_val = val
            mn_pair = (key, mn_val)
    return mx_pair, mn_pair

print(max_min_freq('rajkumaryadav'))
            

# now we just return max and min char only

def mx_mn_char(st):

    freq = {}

    for ch in st:
        freq[ch] = freq.get(ch, 0) + 1

    mx_ch = mn_ch = st[0]

    for key in freq:
        if freq[key] > freq[mx_ch]:
            mx_ch = key
        
        if freq[key] < freq[mn_ch]:
            mn_ch = key
    
    return mx_ch, mn_ch

print(mx_mn_char('rajkumaryadav'))

# find all mx and mn frequencies
# sometimes same characters have same frequencies


def all_mx_mn_ch(string):

    freq = {}

    for ch in string:
        freq[ch] = freq.get(ch, 0) + 1

    mx_val = float('-inf')
    mn_val = float('inf')
    mx_pairs = mn_pairs = []

    for key, val in freq.items():
        if val > mx_val:
            mx_val = val
            mx_pairs = [(key,mx_val)]
        
        elif val == mx_val:
            mx_pairs.append((key, mx_val))

        if val < mn_val:
            mn_val = val
            mn_pairs = [(key, mn_val)]
        
        elif val == mn_val:
            mn_pairs.append((key, mn_val))
        
    return mx_pairs, mn_pairs

print(all_mx_mn_ch('rajkumaryradavr'))