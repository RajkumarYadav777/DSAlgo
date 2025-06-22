
# here we  find if any substring has uique

def all_unique(s, k):
    if k > len(s):
        return False
    
    for i in range(len(s)-k+1):
        window = s[i:i+k]

        if len(set(window)) == k:
            return True, window
    
    return False



# what if more than one window 


def all_unique(s, k):
    if k > len(s):
        return False
    
    uniqs = []
    i = 0
    while i <= len(s)-k:
        window = s[i:i+k]

        if len(set(window)) == k:
            uniqs.append(window)
        i += 1
    return uniqs


# pattern approach

def pattern_approach(s, k):
    if k > len(s):
        return False
    
    count = 1 # first charcter is always uniq

    for i in range(1, len(s)):

        if s[i] == s[i-1]:
            count += 1

            if count == k:
                return True
        else:
            count = 1
    return False



# this is classical sliding window incremental approach
# in this we use freq and count of chars

from collections import defaultdict
def has_uniq(s, k):
    if len(s) < k:
        return False
    
    freq = defaultdict(int)
    uniq_cnt = 0

    for i in range(k):
        if freq[s[i]] == 0:
            uniq_cnt += 1
        freq[s[i]] += 1

        if uniq_cnt == k:
            return True 
    # slide the window

    for i in range(k, len(s)):
        freq[s[i-k]] -= 1
        if freq[s[i-k]] == 0:
            uniq_cnt -= 1
        
        if freq[s[i]] == 0:
            uniq_cnt += 1
        freq[s[i]] += 1
        
        if uniq_cnt == k:
            return True
    
    return False
