
def hexa2bin(input): 
  lis = {'0' : "0000",  
        '1' : "0001", 
        '2' : "0010",  
        '3' : "0011", 
        '4' : "0100", 
        '5' : "0101",  
        '6' : "0110", 
        '7' : "0111",  
        '8' : "1000", 
        '9' : "1001",  
        'A' : "1010",
        'a' : "1010", 
        'B' : "1011",
        'b' : "1011",  
        'C' : "1100",
        'c' : "1100", 
        'D' : "1101",
        'd' : "1101",  
        'E' : "1110",
        'e' : "1110", 
        'F' : "1111",
        'f' : "1111" } 
  binary = "" 
  for i in range(len(input)): 
    binary = binary + lis[input[i]] 
  return binary
    
 
def bin2hex(input): 
  lis = {"0000" : '0',  
        "0001" : '1', 
        "0010" : '2',  
        "0011" : '3', 
        "0100" : '4', 
        "0101" : '5',  
        "0110" : '6', 
        "0111" : '7',  
        "1000" : '8', 
        "1001" : '9',  
        "1010" : 'A', 
        "1011" : 'B',  
        "1100" : 'C', 
        "1101" : 'D',  
        "1110" : 'E', 
        "1111" : 'F' } 
  hex="" 
  for i in range(0,len(input),4): 
    s="" 
    s=s+input[i] 
    s=s+input[i+1]  
    s=s+input[i+2]  
    s=s+input[i+3]  
    hex=hex+lis[s] 
  return hex
  
# Conversions -------------Copyright goes to https://github.com/Abdellrhman-Khaled ---------------------------------------


def bin2dec(input):  
  decimal,i=0,0
  while(input!=0):  
    remainder=input%10
    decimal=decimal+remainder*pow(2, i)  
    input=input//10
    i+=1
  return decimal 
  
def dec2bin(num):  
  result=bin(num).replace("0b", "") 
  if(len(result)%4 != 0): 
    div=len(result) / 4
    div=int(div) 
    counter=(4*(div+1))-len(result)  
    for i in range(0, counter): 
      result='0'+result 
  return result

def XOR(x,y): 
  result="" 
  for i in range(len(x)): 
    if(x[i]==y[i]): 
      result=result+"0"
    else: 
      result=result+"1"
  return result


def Assci_to_hex(ascii_string):
    
    hex_string = ''.join(format(ord(char), '02x') for char in ascii_string)
    
    
    hex_chunks = [hex_string[i:i+16] for i in range(0, len(hex_string), 16)]
    

    if len(hex_chunks[-1]) < 16:
        hex_chunks[-1] = hex_chunks[-1].ljust(16, '0')
    
    return hex_chunks


def hex_to_ascii(hex_chunks): 
   
   hex_string = ''.join(hex_chunks) 
    
   ascii_string = ''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2)) 
   return ascii_string.strip('\x00')


def binary_to_hex(binary_string):
    
    binary_chunks = [binary_string[i:i+64] for i in range(0, len(binary_string), 64)]
    hex_chunks = []

    for chunk in binary_chunks:
        
        hex_value = hex(int(chunk, 2))[2:]  
        hex_chunks.append(hex_value.zfill(16))  
    
    return hex_chunks
