def is_alphabet(char):
    # Check if the character is an alphabet using isalpha() method
    return char.isalpha()

# Example: check if a character is an alphabet
character = 'a'
if is_alphabet(character):
    print("{} is an alphabet.".format(character))
else:
    print("{} is not an alphabet.".format(character))
