
from Constants import *
from Conversions import *

def InitialPermutation(plain_text,InitialPerm, no_bits): 
  permutation="" 
  for i in range(0,no_bits): 
    permutation=permutation+plain_text[InitialPerm[i]-1] 
  return permutation 

def ShiftingLeft(key,nth_shifts): 
  s="" 
  for i in range(nth_shifts): 
    for j in range(1,len(key)): 
      s=s+key[j] 
    s=s+key[0] 
    key=s 
    s=""  
  return key

def encrypt(input,key):
  print("Encryption")
  input=hexa2bin(input)
  input = InitialPermutation(input, InitialPerm, 64) 

  key = hexa2bin(key) 

  key = InitialPermutation(key, PermChoice1, 56)
 
 
  l_key=key[0:28]
  r_key=key[28:56]
 
  l_message = input[0:32] 
  r_message =input[32:64] 

  Pc2BinKey=[]
  Pc2HexKey=[]
  for k in range(16):
    l_key=ShiftingLeft(l_key,ShiftingTable[k])
    r_key=ShiftingLeft(r_key,ShiftingTable[k])
    merge_key=l_key+r_key

    round_key=InitialPermutation(merge_key,PermChoice2,48)
    Pc2BinKey.append(round_key)
    Pc2HexKey.append(bin2hex(round_key))
 
 
  for j in range(16):

    right_expand=InitialPermutation(r_message,ExpantionPerm,48)
    XOR_x=XOR(right_expand,Pc2BinKey[j])

    Sbox="" 
    for i in range(0,8):
      r=bin2dec(int(XOR_x[i*6]+XOR_x[i*6+5]))
      c=bin2dec(int(XOR_x[i*6+1]+XOR_x[i*6+2]+XOR_x[i*6+3]+XOR_x[i*6+4]))
      val=s[i][r][c]
      Sbox=Sbox+dec2bin(val)

    Sbox=InitialPermutation(Sbox,PermTable,32)

    result=XOR(l_message,Sbox)
    l_message=result

    
    if(j!=15):
      l_message, r_message=r_message, l_message

  merge=l_message+r_message
  Cipher=InitialPermutation(merge,FinalPerm,64)
  return Cipher


def tuple_to_string_list(input_tuple:tuple):

    result_list = []

    for item in input_tuple:

        result_list.append(str(item))

    return result_list

def final_step(input_tuple:tuple):
    result_list = tuple_to_string_list(input_tuple)
    plain_text=result_list[1]  
    key=result_list[0]
    Cipher=bin2hex(encrypt(plain_text,key))
    return Cipher

# Main function
#print("Enter the message to be encrypted: ")
input_tuple = ("266200199BBCDFF1", "0123456789ABCDEF")
result=final_step(input_tuple)
print("final string",result )

