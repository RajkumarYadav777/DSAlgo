
# here we compress string based on consecutive nature not frequency based

def consecutive_compress(st):
    res = []
    count = 1

    for i in range(1, len(st)):
        # compare current and previous
        if st[i] == st[i-1]:
            count += 1
        
        else:
            res.append(st[i-1] + str(count))
            # reset count
            count = 1
    # last group
    res.append(st[-1] + str(count))
    return ''.join(res)
print(consecutive_compress('aaabbccaad'))