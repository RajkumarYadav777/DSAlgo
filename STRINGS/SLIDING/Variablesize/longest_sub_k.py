
# here we will find longest substring with atmost k distinct characters


def longest_sub_k_distinct(s, k):
    if k==0 or not s:
        return 0
    
    max_len = 0
    window_freq = {}
    start = 0

    for end in range(len(s)):
        char = s[end]
        window_freq[char] = window_freq.get(char, 0) + 1

        while len(window_freq) > k:
            left_char = s[start]
            window_freq[left_char] -= 1
            if window_freq[left_char] == 0:
                del window_freq[left_char]
            start += 1
        max_len = max(max_len, end-start + 1)
    return max_len