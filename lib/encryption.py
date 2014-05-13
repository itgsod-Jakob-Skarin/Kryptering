def encrypt(cleartext, offset):
    letters1 = ['a', ' ', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    letters2 = ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = letters1 + letters2
    if len(cleartext) == 0:
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    for letter in cleartext:
        new_letter = letters.index(letter) + offset

    #new_cleartext = ''
    for new_letter
        add new_letter in new_cleartext
     bokstav i x, + y for ny bokstav
    return cleartext.upper()


print encrypt('the quick brown fox jumps over the lazy dog', 3)

