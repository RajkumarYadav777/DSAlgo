# find the max no of vowels in a given substring of size k

# it follows incremental sliding window
# remove from left and adding from right and process and update the result

def max_no_vowels(s, k):
    vowels = set('aeiou')
    cur_count = 0
    max_count = 0

    # first window

    for i in range(k):
        if s[i] in vowels:
            cur_count += 1

    max_count = cur_count

    for i in range(k, len(s)):
        # remove left most
        if s[i-k] in vowels:
            cur_count -= 1
        
        # add from right
        if s[i] in vowels:
            cur_count += 1
        max_count = max(max_count, cur_count)
    
    return max_count



# using two pointers

def max_vowles_substring(s, k):
    if k > len(s):
        return ''
    
    vowels = set('aeiou')
    res = ''
    start = end = 0
    cur_count = max_count = 0
    


    while end < len(s):
        if s[end] in vowels:
            cur_count += 1

        if end-start+1 == k:
            if cur_count > max_count:
                max_count = cur_count
                res = s[start:end+1]
                

            if s[start] in vowels:
                cur_count -= 1
            start += 1
        end += 1
    return res, max_count

