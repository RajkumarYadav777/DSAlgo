
# here we use naive window pattern

def all_identical(s, k):
    if k > len(s):
        return False
    
    for i in range(len(s)-k + 1): # lenght-7 &k=3 ; 7-3 =4 windows

        window = s[i:i+k]

        if all(ch == window[0] for ch in window):
            return True, window
        
    return False


# here we may find more than one output window , if we want to display


def all_iden_sub(s, k):
    if len(s) < k:
        return False
    
    ident = []

    for i in range(len(s)-k+1):  # while i <= len(s)-k
        window = s[i:i+k]

        if all(ch == window[0] for ch in window):
            ident.append(window)
    return ident