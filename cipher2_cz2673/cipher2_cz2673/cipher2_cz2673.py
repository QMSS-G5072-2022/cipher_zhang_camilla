def cipher(text, shift, encrypt=True):

    """
    Encrypts or decrypts text based on Caesar cipher

    Parameters
    ----------
    text : str
      A string that you wish to encrypt/decript
    shift : int
      A number of type int that defines how many indices you want to move for the purposes of encryption/decryption
    encrypt : bool
      A boolean that defines whether you wish to encrypt or decrypt your text
    

    
    Returns
    -------
    str
      The newly encrypted/decrypted text 

    Examples
    --------
    Example 1:
    >>> from cipher_cz2673 import cipher_cz2673
    >>> text = "text"
    >>> shift = 1
    >>> encrypt = True
    >>> cipher_module.cipher(text, shift, encrypt)
    "text"

    Example 2:
    >>> from cipher_cz2673 import cipher_cz2673
    >>> text = "hello"
    >>> shift = 2
    >>> encrypt = False
    >>> cipher_module.cipher(text, shift, encrypt)
    "fcjjm"
"""
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text: #for every letter in the text
        index = alphabet.find(c) #find the letter index in the alphabet
        if index == -1: #if there is no index aka the item isn't in the alphabet
            new_text += c #output c
        else:
            new_index = index + shift if encrypt == True else index - shift #if encrypt = true, new index = index + shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text



