
from Constants import *
from Conversions import *
from DES import *



message = ""
key = "133457799BBCDFF1"

#------------------------- meesage encryption 
#This function takes an input ascii string and a 16 hexadecimal string key and return a hexadecimal encrypted string 
def message_encryption(message , key):
    # message is ascii string
    hex_chunks = Assci_to_hex(message)
    print(hex_chunks)
    encrypted_text ="" 
    for i in range(len(hex_chunks)):
      encrypted_text += encrypt(hex_chunks[i],key)
    
    return bin2hex(encrypted_text)
#------------------------------------------

#---------------------message decryption
#this function takes an input of hex string and a 16 hexadecimal string key and return ascii decrypted string
def message_decryption(message, key):
    #message is hex_string
    hex_chunks = [message[i:i+16] for i in range(0, len(message), 16)]
    print(hex_chunks)
    decrypted_text = ""
    for i in range(len(hex_chunks)):
        decrypted_text += decrypt(hex_chunks[i], key)
    
    # print("binary string",decrypted_text )
    decrypted_hex = binary_to_hex(decrypted_text)
    # print("hex string",decrypted_hex )
    assci_string = hex_to_ascii(decrypted_hex)
    return assci_string

  

# result=message_encryption(message , key )
# print("final string",result )

# result2=message_decryption(result , key )
# print("final string",result2 )
