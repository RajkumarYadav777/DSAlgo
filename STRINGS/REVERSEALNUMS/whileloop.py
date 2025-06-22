

#  we use while loop to perform this task


def rev_only_alnums(s):
    i = 0
    alnums = [ch for ch in s if ch.isalnum()]
    res = []

    while i < len(s):

        if s[i].isalnum():
            res.append(alnums.pop())

        else:
            res.append(s[i])
        i += 1
    return ''.join(res)

print(rev_only_alnums('rajkumar$yadav'))