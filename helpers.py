def alphabet_position(letter):
    a = ord(letter)
    if a >= 65 and a <= 91:
        b = a - 65
        return b
    elif a >= 97 and a <= 122:
        b = a - 97
        return b
    else:
        return (False)
def rotate_character(char, rot):
    import string
    strg = string.ascii_uppercase 
    strg_lwr = string.ascii_lowercase
    ch = alphabet_position(char)
    d = ch + rot
    if d >= 0 and d <= 25:        
        if char in strg:
            e = strg[d]
            return e
        if char in strg_lwr:
            e = strg_lwr[d]
            return e
        else:
            return char
    else:
        sm = d // 26
        am = sm * 26
        h = d - am
        if char in strg:
            e = strg[h]
            return e
        if char in strg_lwr:
            e = strg_lwr[h]
            return e
        else:
            return char    
