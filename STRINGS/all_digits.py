# here we check if a string contains all the digits 

def is_all_digits(st):

    for char in st:

        if not char.isdigit():
            return False
    return True
print(is_all_digits('123456y'))

# we will use all()

def check_isidgits(st):

    return all(char.isdigit() for char in st)

print(check_isidgits('12345'))