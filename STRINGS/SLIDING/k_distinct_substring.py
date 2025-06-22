
# here we find no of substrings that has k distinct character

# two pointers + freq + fixed sliding
from collections import defaultdict

def k_distinct_chars(s, k):
    if len(s) < k:
        return 0
    
    freq = defaultdict(int)

    count = 0

    start = 0

    for end in range(len(s)):

        freq[s[end]] += 1

        # check window size
        if end-start+1 == k :
            if len(freq) == k:
                count += 1

            # slide the window by shrinking left only

            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
            
            start += 1
    return count


# here we use sliding window + freq


def k_distinc_sliding(s, k):
    if len(s) < k:
        return 0
    count = 0
    freq = defaultdict(int)
    for i in range(k):
        freq[s[i]] += 1
    
    if len(freq) == k:
        count += 1
    
    # slide the window

    for i in range(k, len(s)):
        freq[s[i-k]] -= 1

        if freq[s[i-k]] == 0:
            del freq[s[i-k]]

        freq[s[i]] += 1
    return count 