import random
import string
def GenerateCharacter():
    if(random.randint(0, 1)) == 1:
        return random.choice(string.ascii_letters.upper())
    else:
        return str(random.randint(0,9))
def GenerateCharacters():
    part = ""
    i = 0
    while i != 5:
        part = part + GenerateCharacter()
        i = i + 1
    return part
def GenerateKey():
    print(GenerateCharacters() + "-" + GenerateCharacters() + "-" + GenerateCharacters())
GenerateKey()