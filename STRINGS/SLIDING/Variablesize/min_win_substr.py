
# we find  minimum window substring

from collections import Counter
def min_wind_sub(s, t):
    if not s or not t:
        return ''
    
    target_freq = Counter(t)
    window_freq = {}
    have, need = 0 , len(target_freq)
    res, res_len = [-1,-1], float('inf')  # res stores indices of best window

    start = 0 # window starting point 
    
    for end in range(len(s)):
        char = s[end]

        window_freq[char] = window_freq.get(char,0)+1

        if char in target_freq and window_freq[char] == target_freq[char]:
            have += 1

        
        while have == need:
            window_size = end-start + 1

            # checking the current window size to previous one
            if window_size < res_len:
                res = [start, end]
                res_len = window_size

            # shrinking left and check window validity
            left_char = s[start]
            window_freq[left_char] -= 1

            # after removing is there invalidity

            if left_char in target_freq and window_freq[left_char] < target_freq[left_char]:
                have -= 1
            start += 1

    l, r = res

    return s[l:r+1] if res_len != float('inf') else ''