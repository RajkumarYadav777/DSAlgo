

# here we want to reverse only alnums not special characters

# frst store alnums and collects reversely using list


# FOREACH

def rev_only_alnums(s):
    alnums = [ch for ch in s if ch.isalnum()]

    res = []

    for char in s:

        if char.isalnum():
            res.append(alnums.pop())
        
        else:
            res.append(char)
        
    return ''.join(res)

print(rev_only_alnums('rajkumar$yadav'))
