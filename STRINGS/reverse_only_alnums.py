
# here we write program to reverse only characters not special chars
# string is immutable, so we can not assign new or modify original
# so , frst convert it to list and later revert back to string


def reverse_only_alnums(st):
    st = list(st)
    start = 0
    end = len(st)-1

    while start < end:
        if not st[start].isalnum():
            start += 1
        elif not st[end].isalnum():
            end -= 1
        
        else:
            st[start], st[end] = st[end], st[start]
            start += 1
            end -= 1
    return ''.join(st)
print(reverse_only_alnums('rajkum$yad#v'))