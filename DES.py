
# -------------Copyright goes to https://github.com/Abdellrhman-Khaled ---------------------------------------

from Constants import *
from Conversions import *

def Computational_Permutation(plain_text,InitialPerm, no_bits): 
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
  input = Computational_Permutation(input, InitialPerm, 64) 

  key = hexa2bin(key) 

  key = Computational_Permutation(key, PermChoice1, 56)
 
 
  l_key=key[0:28]
  r_key=key[28:56]
 
  l_message = input[0:32] 
  r_message =input[32:64] 

  Pc2BinKey=[]
  # Pc2HexKey=[]

  #Round keys permutations------------------------------
  for k in range(16):
    l_key=ShiftingLeft(l_key,ShiftingTable[k])
    r_key=ShiftingLeft(r_key,ShiftingTable[k])
    merge_key=l_key+r_key

    round_key=Computational_Permutation(merge_key,PermChoice2,48)
    Pc2BinKey.append(round_key)
    # Pc2HexKey.append(bin2hex(round_key))
 #--------------------------------------------------------------------
 
  for j in range(16):


    #Changing 32bit right text into 48bit--------------
    right_expand=Computational_Permutation(r_message,ExpantionPerm,48)
    #------------------------------------

    #Xoring the round key with the right text F = K1+E(R0)---------------
    XOR_x=XOR(right_expand,Pc2BinKey[j])

    # -----------------------------------

    #Changing 48 bit [F = K1+E(R0)] into 32bit using x-boxes--------------
    Sbox="" 
    for i in range(0,8):
      r=bin2dec(int(XOR_x[i*6]+XOR_x[i*6+5]))
      c=bin2dec(int(XOR_x[i*6+1]+XOR_x[i*6+2]+XOR_x[i*6+3]+XOR_x[i*6+4]))
      val=s[i][r][c]
      Sbox=Sbox+dec2bin(val)

    
    #Permutation after s-box 
    Sbox=Computational_Permutation(Sbox,PermTable,32)
    #-------------------------------------------------------------------

    #XORing left message with the computed permutation
    result=XOR(l_message,Sbox)
    
    # -----------------------------------------
    
    l_message=result

    
    if(j!=15):
      # Rj =L(j-1)+𝐹(R(j-1) , K(j))    changing the right side an the left side

      l_message, r_message=r_message, l_message

  merge=l_message+r_message
  #Final permutation[Inverse intial]-----------------------------
  Cipher=Computational_Permutation(merge,FinalPerm,64)
  return Cipher



def decrypt(input,key):
  print("Decryption")
  input=hexa2bin(input)
  input = Computational_Permutation(input, InitialPerm, 64) 

  key = hexa2bin(key) 

  key = Computational_Permutation(key, PermChoice1, 56)
 
 
  l_key=key[0:28]
  r_key=key[28:56]
 
  l_message = input[0:32] 
  r_message =input[32:64]
  
  Pc2BinKey=[]
  # Pc2HexKey=[]

  #Round keys permutations------------------------------
  for k in range(16):
    l_key=ShiftingLeft(l_key,ShiftingTable[k])
    r_key=ShiftingLeft(r_key,ShiftingTable[k])
    merge_key=l_key+r_key

    round_key=Computational_Permutation(merge_key,PermChoice2,48)
    Pc2BinKey.append(round_key)
    #--------------------------------------------------------------------
 
    k=15
  for j in range(16):

    #Changing 32bit right text into 48bit--------------
    right_expand=Computational_Permutation(r_message,ExpantionPerm,48)
    #------------------------------------

    #Xoring the round key with the right text F = K1+E(R0)---------------
    XOR_x=XOR(right_expand,Pc2BinKey[k])
    k=k-1

    # -----------------------------------

    #Changing 48 bit [F = K1+E(R0)] into 32bit using x-boxes--------------
    Sbox="" 
    for i in range(0,8):
      r=bin2dec(int(XOR_x[i*6]+XOR_x[i*6+5]))
      c=bin2dec(int(XOR_x[i*6+1]+XOR_x[i*6+2]+XOR_x[i*6+3]+XOR_x[i*6+4]))
      val=s[i][r][c]
      Sbox=Sbox+dec2bin(val)

    
    #Permutation after s-box 
    Sbox=Computational_Permutation(Sbox,PermTable,32)
    #-------------------------------------------------------------------

    #XORing left message with the computed permutation
    result=XOR(l_message,Sbox)
    
    # -----------------------------------------
    
    l_message=result

    
    if(j!=15):
      # Rj =L(j-1)+𝐹(R(j-1) , K(j))    changing the right side an the left side

      l_message, r_message=r_message, l_message

  merge=l_message+r_message
  #Final permutation[Inverse intial]-----------------------------
  plain=Computational_Permutation(merge,FinalPerm,64)
  return plain

  

