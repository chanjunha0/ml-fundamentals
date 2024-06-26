"""

Algorithm for Caesar Cipher

- Ancient cryptography used by Julius Caesar.
- Substitution Cipher Family
- Based on transposition of alphabets
- Encrypt and decrypt based on the shift by transposition

Advantages
- Efficient, linear time complexity of O(n)

Disadvantages
- Easily broken (only 25 possible shifts)

"""


def caesar_cipher_encrypt(text: str, shift: int) -> str:
    """
    For a given input text, encrypts it using the Caesar cipher.

    Args:
        text (str): Text to encrypt
        shift (int): Integer to shift the the alphabet by

    Returns:
        result (str): Encrypted text
    """
    encrypted_text = []

    for char in text:
        if char.isupper():
            # "A" is 65 in ASCII
            # Note modulo %26 is for the wrapping around the alphabet in the event the character + shift exceeds the 26 range of the alphabet.
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # "a" is 97 in ASCII
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
        # not alphabetic character
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)


def caesar_cipher_decrypt(encrpyted_text: str, shift: int) -> str:
    """
    For a given encrypted text, dencrypts it using the Caesar cipher.

    Args:
        encrpyted_text (str): Text to dencrypt
        shift (int): Integer to shift the the alphabet back by

    Returns:
        result (str): Decrypted text
    """
    decrypted_text = []

    for char in encrpyted_text:
        if char.isupper():
            # "A" is 65 in ASCII
            decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            # "a" is 97 in ASCII
            decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
        # not alphabetic character
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)


# Example
text = "That girl is really pretty!"
shift = 5
encrypted_text = caesar_cipher_encrypt(text, shift)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

print("Original Text: " + text)
print("Encrypted Text: " + encrypted_text)
print("Decrypted Text: " + decrypted_text)
