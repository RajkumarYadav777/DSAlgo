
# lonest substring with out repeating characterr


def length_of_longest_substr(s):
    if not s:
        return 0
    
    window = {}
    max_len = 0
    res = [0, 0]
    start = 0

    for end in range(len(s)):
        char = s[end]
        window[char] = window.get(char,0) + 1

        # if dup reduce from left , if not update length
        while window[char] > 1:
            left_char = s[start]
            window[left_char] -= 1
            start += 1

        # for each character we need to update window
        window_size = end - start + 1
        if window_size > max_len:
            max_len = window_size
            res = [start, end]
    
    l, r = res
    return s[l:r+1], max_len



# using set

def logest_sub_with_set(s):
    if not s:
        return 0
    
    max_len = 0
    seen = set()
    start = 0

    for end in range(len(s)):
        seen.add(s[end])
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        max_len = max(max_len, end-start + 1)
    return max_len

