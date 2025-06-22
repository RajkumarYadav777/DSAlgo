

# here we find the substring with the highest frequency of a given character

def high_freq_char(s, c, k):
    if k > len(s):
        return ''
    
    count = sum(1 for ch in s[:k] if ch == c)
    start = 0
    max_count = count
    for i in range(k, len(s)):
        if s[i-k] ==c :
            count -= 1
        
        if s[i] == c:
            count += 1
        
        if count > max_count:
            max_count = count
            start = i-k+1
    return max_count, s[start:start+k]

    