
# find the substring with higest frequency of a given character


def max_c_count_substring(s, c, k):
    if len(s) < k:
        return ''
    
    count = sum(1 for ch in s[:k] if ch == c)
    max_count = count
    start_index = 0

    for i in range(k, len(s)):
        if s[i-k] == c:
            count -= 1
        
        if s[i] == c:
            count += 1
        if count > max_count:
            max_count = count
            start_index = i-k+1
    
    return s[start_index:start_index+k]