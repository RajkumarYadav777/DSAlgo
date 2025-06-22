
# here we will coutn vowels and consonants

# condition is frst is it alphabet then is it in vowels 

def vowels_consonants(st):
    vowels = set('aeiou')
    vow_count = 0
    cons_count = 0

    for char in st:
        if char.isalpha():
            if char in vowels:
                vow_count += 1
            else:
                cons_count += 1
    return f'vowels_count : {vow_count}\n cons_count:{cons_count}'

print(vowels_consonants(' i love you india'))