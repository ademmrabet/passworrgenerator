import random
import string

def genratePassword(minLength, numbers=True, specialCharacter=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #print(letters, digits, special)

    characters = letters
    if numbers:
        characters += digits
    if specialCharacter:
        characters += special

    pwd = ""
    meetscriteria =  False
    has_number = False
    has_special = False

    while not meetscriteria or len(pwd) < minLength:
        newChar =  random.choice(characters)
        pwd += newChar

        if newChar in digits:
            has_number = True
        elif newChar in special:
            has_special = True
        
        meetscriteria = True
        if numbers:
            meetscriteria = has_number
        
        if specialCharacter:
            meetscriteria = meetscriteria and has_special
    
    return pwd

password = genratePassword(12)
print(password)
