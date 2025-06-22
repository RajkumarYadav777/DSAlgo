

def mx_mn_freq(st):
    freq = {}
    i = 0
    while i < len(st):
        ch = st[i]
        freq[ch] = freq.get(ch, 0) + 1
        i += 1

    mx_ch = mn_ch = st[0]

    j = 0 
    while j < len(freq):
        ch = st[j]
        if freq[ch] > freq[mx_ch]:
            mx_ch = ch
        

        if freq[ch] < freq[mn_ch]:
            mn_ch = ch
        j += 1
    return mx_ch, mn_ch

print(mx_mn_freq('rajkumaryadav'))