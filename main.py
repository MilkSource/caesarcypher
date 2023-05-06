def encrypt():

    plaintext = str(input("\n\nInput a plain text: "))
    shift = int(input("Shift: "))
    encrypted_text = ""

    for i in range(len(plaintext)):
        character = plaintext[i]

        if character == " ":
            encrypted_text += " "
        
        elif character.isupper():
            encrypted_text += chr((ord(character) + (shift-65)) % 26 + 65)
        
        else:
            encrypted_text += chr((ord(character) + (shift-97)) % 26 + 97)
    
    return encrypted_text



def decrypt():

    encrypted_text = str(input("\n\nInput a encrypted text: "))
    

    for x in range(26):
        decrypted_text = ""
        shift = x
        for i in range(len(encrypted_text)):
            character = encrypted_text[i]

            if character == " ":
                decrypted_text += " "
            
            elif character.isupper():
                decrypted_text += chr((ord(character) - shift-65) % 26 + 65)
            
            else:
                decrypted_text += chr((ord(character) - shift-97) % 26 + 97)
        
        print(f'\nDECRYPTION ({shift}): [{decrypted_text}]')
    



print("\n\n{Caesar Cypher}")

print("\n*Select a mode*")
print("[0] Encryption")
print("[1] Decryption")
mode = int(input("=: "))

if mode == 0:
    encrypted_text = encrypt()
    print(f"\n\nENCRYPTION: [{encrypted_text}]\n\n")

elif mode == 1:
    decrypted_text = decrypt()





