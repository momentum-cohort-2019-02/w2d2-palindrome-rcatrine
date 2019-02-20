# Enter phrase
phrase = input("Enter phrase: ")

def identify_palindrome(characters):
    """Takes string and identifies whether or not it is a palindrome"""
    # Make all characters lowercase and leave only letters and numbers
    characters = ("".join(e for e in characters if e.isalnum())).lower()
    # Start at first and last character and remove character until palindrome/non-palindrome detected
    first_character = characters[0]
    last_character = characters[-1]
    
    while len(characters) > 1:
        if first_character == last_character:
            characters = characters[1:-1]        
        else:
            return print("is not a palindrome")
    return print("is a palindrome")

identify_palindrome(phrase)
