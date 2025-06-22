
# find maximum sum of ascii values in a substring of length k

# follow incremental sliding window


def msx_sum_ascii(s, k):
    if len(s) < k:
        return ''
    
    cur_sum = 0
    max_sum = 0

    # initial window
    for i in range(k):
        cur_sum = sum(ord(ch) for ch in s[:k])
    
    max_sum = cur_sum

    # slide the window

    for i in range(k, len(s)):
        # remove from left
        cur_sum -= ord(s[i-k])

        # add from right
        cur_sum += ord(s[i])

        max_sum = max(max_sum, cur_sum)

    return max_sum



# return substrig itself

def max_substring_ascii(s, k):
    if len(s) > k:
        return ''
    
    cur_sum = sum(ord(ch) for ch in s[:k])
    max_sum = cur_sum

    start_index = 0

    for i in range(k, len(s)):
        cur_sum -= ord(s[i-k])
        cur_sum += ord(s[i])

        if cur_sum > max_sum:
            max_sum = cur_sum
            start_index = i-k+1

    return s[start_index : start_index + k]


# Two pointers


def ascii_sum(s, k):
    if len(s)< k:
        return 0
    cur_sum = 0
    max_sum = 0
    start_id = 0
    end = 0
    start = 0

    while end < len(s):
        cur_sum += ord(s[end])

        if end-start+1 == k:
            if cur_sum > max_sum:
                max_sum = cur_sum
                start_id = start
            
            cur_sum -= ord(s[start])
            start += 1
        end += 1
    return max_sum, s[start_id:start_id+k]
        


