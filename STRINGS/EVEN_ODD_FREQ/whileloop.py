
def even_odd_freq(st):
    freq = {}
    i = 0
    while i < len(st):
        ch = st[i]
        freq[ch] = freq.get(ch, 0) + 1
        i += 1
    
    j = 0
    odd = ['odd  :']
    even = ['even :']
    keys = list(freq.keys())

    while j < len(freq):
        # ch = st[j] # if we take string we will get duplicates
        ch = keys[j]
        if freq[ch]%2:
            odd.append((ch, freq[ch]))
        else:
            even.append((ch, freq[ch]))
        j += 1
    return odd, even
print(even_odd_freq('rajkumaryadav'))



# here we gradually shrinks the dictionary

def shrink_dictionary(st):
    freq = {}

    i = 0

    while i < len(st):
        freq[st[i]] = freq.get(st[i],0) + 1
        i+=1

    odd = {}
    even = {}

    while freq:
        # popitem removes last item and returns it
        ch, count = freq.popitem()
        if count%2 == 0:
            even.update([(ch, count)])
        
        else:
            odd.update([(ch, count)])
    return odd, even

print(shrink_dictionary('rajkumaryadav'))
