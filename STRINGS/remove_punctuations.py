# here we remove punctuations from sting


import string
def remove_puncts(st):
    return ''.join(char for char in st if char not in string.punctuation)
print(remove_puncts('raj!kumar:yadav.'))
'''
string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.punctuation

NOTE: these are all important methods from string module

'''

# str.maketrans()
'''
# str.maketrans() is used to replace char to char , it builds transaltion table
str.maketrans(x, y, z)
x -> which char you want to replace
y-> char that will replaced x 
z-> deletes the char 
# z positions values point to None , transalte will deletes them
# remove special symbols
str.maketrans('', '', '!@#$')
{
ord(!):None,
ord(@):None,
ord(#):None,
ord($):None

# here we did not want to replace anycha with original s as we set x = '' and y= ''

}

'''

# str.translate(table)
'''
# translate uses table and modifies or replace or deletes the original s
'''

def remove_punctuations(st):
    table = st.maketrans('', '', string.punctuation)
    res = st.translate(table)
    return res
print(remove_punctuations("Hello, world! It's a beautiful day :) #blessed"))