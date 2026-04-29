import string
import secrets

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Aucun type de caractère sélectionné.")

    return ''.join(secrets.choice(characters) for _ in range(length))