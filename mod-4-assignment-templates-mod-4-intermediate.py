'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
'''
    def shift_letter(letter, shift):
    if letter == " ":
        return " "
    
    alphabet = "ABDEFGHIJKLMNOPQRSTUVWXYZ"
    position = alphabet.find(letter)
    new_position = (position + shift) % 26
    shifted_letter = alphabet[new_position]
    
    return shifted_letter

letter = str(input("Enter a single uppercase English letter or space:"))
shift = int(input("Enter the number by which to shift the letter:"))
shifted_result = shift_letter(letter, shift)
print(f"Thhe shifted letter is {shifted_result}")

'''

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
 '''
def caesar_cipher(message, shift):
    alphabet = "ABDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for char in message:
        if char == " ":
            result += " "
        else:
            position = alphabet.find(char)
            new_position = (position + shift) % 26
            shifted_char = alphabet[new_position]
            result += shifted_char
    return result

message = str(input("Enter a message using uppercase English letters and space only:"))
shift = int(input("Enter the number by which to shift the letters:"))
ciphered_message = caesar_cipher(message, shift)
print(f"The ciphered message is {ciphered_message}")

  ''' 
def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
'''
def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    letter_value = ord(letter) - ord("A")
    shift_value = ord(letter_shift) - ord("A")
    new_value = (letter_value + shift_value) % 26
    shifted_letter = chr(new_value + ord("A"))
    return shifted_letter

letter = str(input("Enter a single uppercase English letter or space:"))
letter_shift = str(input("Enter a single uppercase English letter or shift:"))
shifted_result = shift_by_letter(letter, letter_shift)
print(f"The letter shifted is {shifted_result}")

'''

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
'''
def shift_letter(letter, shift):
    if letter == " ":
        return " "
    
    alphabet = "ABDEFGHIJKLMNOPQRSTUVWXYZ"
    position = alphabet.find(letter)
    new_position = (position + shift) % 26
    shifted_letter = alphabet[new_position]
    
    return shifted_letter

letter = str(input("Enter a single uppercase English letter or space:"))
shift = int(input("Enter the number by which to shift the letter:"))
shifted_result = shift_letter(letter, shift)
print(f"Thhe shifted letter is {shifted_result}")

'''

    
