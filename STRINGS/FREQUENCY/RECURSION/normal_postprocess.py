

# here we follow post processing without accumaltor pattern

def freq_count(s,i):

    if i == len(s):
        return {}
    
    # first complete recursion and after unwind /process
    freq = freq_count(s, i+1)

    ch = s[i]
    
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
    return freq

print(freq_count('rajkumaryadav',0))


# using with helper



def freq_main(s):
    def helper(s, i):

        if i == len(s):
            return {}
        
        freq = helper(s, i+1)
        ch = s[i]

        freq[ch] = freq.get(ch, 0)+1
        return freq
    return helper(s, 0)

print(freq_main('rajkumaryadav'))


# pre processing without accumalator pattern

def freq_count(s):
    def helper(i):
        if i == len(s):
            return {}

        # 💡 Pre-processing step — process current character first
        char = s[i]
        freq = {char: 1}  # Create frequency for current char

        # 🔁 Get frequency from rest of string
        rest_freq = helper(i + 1)

        # 🧩 Merge rest_freq into current freq
        if char in rest_freq:
            freq[char] += rest_freq[char]
            del rest_freq[char]

        # Merge both dictionaries
        freq.update(rest_freq)
        return freq

    return helper(0)

# Test
print(freq_count("rajkumaryadav"))
