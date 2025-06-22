
# here we use tail recursion both manually and patter wise 

# index + tail

def freq_tail(s):

    def helper(s, i, freq):
        
        # base case

        if i == len(s):
            return freq
        ch = s[i]
        freq[ch] = freq.get(ch, 0 ) + 1
        return helper(s, i+1, freq)
    return helper(s, 0, {})
print(freq_tail('rajkumaryadav'))


# using slicing

def tail_slice(s):

    def helper(s, freq=None):
        if freq is None:
            freq = {}
        
        # base case

        if not s:
            return freq
        
        ch = s[0]
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
        return helper(s[1:], freq)
    return helper(s,{})
print(tail_slice('rajkumaryadav'))
