import encryption
import decryption
TRUE = True 
while TRUE:
    
    encode_decode= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if encode_decode == 'encode':
        message = input("Type your message: \n").lower()
        shift_number = int(input("Type the shift number: \n"))
        encryption.encryption(message,shift_number)
    elif encode_decode == 'decode':
        message = input("Type your message: \n").lower()
        shift_number = int(input("Type the shift number: \n"))
        decryption.decryption(message,shift_number)
    else:
        TRUE = True
        
    Continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if Continue == 'yes':
        TRUE = True
    else:
        TRUE = False


 