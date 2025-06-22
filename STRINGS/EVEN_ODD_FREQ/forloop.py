

# we just follow regular way

def even_odd_fre(st):
    freq = {}

    for ch in st:
        freq[ch] = freq.get(ch, 0) + 1

    odd_f = {}
    even_f = {}

    for key, val in freq.items():
        if val%2 == 0:
            even_f.update({key:val})
        
        else:
            odd_f.update({key:val})
    return even_f, odd_f
print(even_odd_fre('rajkumaryadav'))


# use dict comprehension

def dict_comprehension(st):
    freq = {}
    for ch in st:
        freq[ch] = freq.get(ch, 0)+1

    result = {
        'even':{key:val for key, val in freq.items() if val%2==0},
        'odd' :{key:val for key, val in freq.items() if val%2}
    }
    return result

print(dict_comprehension('rajkumaryadav'))