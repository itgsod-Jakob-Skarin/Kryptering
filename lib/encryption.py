def encrypt(cleartext, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if len(cleartext) == 0:
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    output = ''
    for char in cleartext:
        char = char.lower()
        if char == ' ':
            output += ' '
        elif alphabet.index(char) + offset > 25:
            new_pos =+ alphabet.index(char) + offset - 26
            output += alphabet[new_pos]
        else:
            new_pos = alphabet.index(char) + offset
            output += alphabet[new_pos]
    return output.upper()