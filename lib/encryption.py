def encrypt(cleartext, offset): # två argument, text och förskutning
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #veta vilken lista det förskuts i, eftersom den
    # inte själv kan alfabetet
    if len(cleartext) == 0: # om text in är tom så ska/kan den inte ändra något
        raise ValueError('can not encrypt empty string')
    if offset == 0: # om förskutningen är 0 händer inget, error måste inte ges egentligen.
        raise ValueError('offset must not be zero')
    output = '' # gör en output redo
    for char in cleartext:
        char = char.lower()
        if char == ' ':
            output += ' ' #gör så att space fortsätter vara space, annars behöver man ha med mellanrum i alfabetet
        elif alphabet.index(char) + offset > 25: # det här hindrar det från att bugga när den går mot slutet av listan
            new_pos =+ alphabet.index(char) + offset - 26
            output += alphabet[new_pos]
        else:
            new_pos = alphabet.index(char) + offset
            output += alphabet[new_pos]
    return output.upper()

def decrypt(cleartext, offset):
    return encrypt(cleartext, -offset).lower()