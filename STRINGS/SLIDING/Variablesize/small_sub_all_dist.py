
# find the smallest substring with all distinct
# we need to find frst distincts in s; required

def smallest_sub_all_distinct(s):
    from collections import defaultdict

    if not s:
        return 0
    min_len = float('inf')
    distinct = set(s)
    need = len(distinct)
    have = 0
    start = 0

    window = defaultdict(int)

    for end in range(len(s)):
        window[s[end]] += 1
        if window[s[end]] == 1:
            have += 1
        
        while need == have:
            left_char = s[start]
            window[left_char] -= 1
            if window[left_char] == 0:
                have -= 1
            start += 1
            min_len = min(min_len, end-start+1)
    return min_len if min_len != float('inf') else 0

