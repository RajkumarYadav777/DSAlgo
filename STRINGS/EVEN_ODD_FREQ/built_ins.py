
# here we use counter and list comprehension


from collections import Counter

def using_lst_comp(st):
    freq = Counter(st)

    odd = [(ch, count) for ch, count in freq.items() if count%2]
    even = [(ch,count) for ch, count in freq.items() if count%2==0]
    return odd, even
print(using_lst_comp('rajkumaryadav')) 