def encrypt(cleartext, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if len(cleartext) == 0:
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    output = ''
    if alphabet.index(char) + offset > 25:
        alphabet.index(char) + offset - 26

    for char in cleartext:
        if char == ' ':
            output += ' '
        else:
            new_pos = alphabet.index(char) + offset
            output += alphabet[new_pos]
    return cleartext.upper


#If pos + offset > 25:
#pos + offset - 26:

    # for letter in cleartext:
    #     new_letter = letters.index(letter) + offset
    #
    # #new_cleartext = ''
    # for new_letter
    #     add new_letter in new_cleartext
    #  bokstav i x, + y for ny bokstav
    # return cleartext.upper()


print encrypt('the quick brown fox jumps over the lazy dog', 3)