# here we find string compression 
# freqency based compression


def string_compression(st):
    seen = set()
    compression = ''

    for char in st:
        if char not in seen:
            seen.add(char)
            compression += str(st.count(char))+char
    return compression
print(string_compression('aaabbacccdaae'))

# freqency based frequency
from collections import Counter
def freq_based_compression(st):
    freq = Counter(st)
    
    return ''.join(str(freq[ch])+ch for ch in freq)
print(freq_based_compression('aabbacade'))