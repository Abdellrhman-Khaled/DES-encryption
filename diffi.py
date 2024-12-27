from sympy import randprime
import random
from Constants import *
from Conversions import *
from DES import *
from Text_encryption_decryption import *

def generate_large_prime(bits=512):
    return randprime(2**(bits-1), 2**bits)

def generate_dh_parameters(bits=512):
    p = generate_large_prime(bits)
    g = random.randint(2, p - 2)
    return p, g

def generate_dh_keys(p, g):
    private_key = random.randint(1, p - 1)
    public_key = pow(g, private_key, p) #pow(base, exp, mod)
    return private_key, public_key

def compute_shared_key(public_key, private_key, p):
    return pow(public_key, private_key, p)

def hex_session_key(shared_key):
    # Convert the shared key to hexadecimal
    hex_key = hex(shared_key)[2:]  # Convert to hex and remove the '0x' prefix
    # Pad with zeros or truncate to ensure it's 16 characters
    return hex_key.zfill(16)[:16]


if __name__ == "__main__":
    # Step 1: Generate Diffie-Hellman Parameters (prime p and generator g)
    print("Generating Diffie-Hellman parameters...")
    p, g = generate_dh_parameters(bits=512)
    print(f"Prime (p): {p}")
    print(f"Generator (g): {g}\n")

    # Step 2: User A generates keys
    print("User A generates keys...")
    private_a, public_a = generate_dh_keys(p, g)
    print(f"User A Private Key: {private_a}")
    print(f"User A Public Key: {public_a}\n")

    # Step 3: User B generates keys
    print("User B generates keys...")
    private_b, public_b = generate_dh_keys(p, g)
    print(f"User B Private Key: {private_b}")
    print(f"User B Public Key: {public_b}\n")

    # Step 4: Compute Shared Keys
    print("Computing shared keys...")
    shared_key_a = compute_shared_key(public_b, private_a, p)
    shared_key_b = compute_shared_key(public_a, private_b, p)

    # Both keys should match
    assert shared_key_a == shared_key_b, "Shared keys do not match!"
    print(f"Shared Key (User A's computation): {shared_key_a}")
    print(f"Shared Key (User B's computation): {shared_key_b}\n")

    # Step 5: Derive 16-character Session Key
    session_key = hex_session_key(shared_key_a)
    print(f"Derived 16-character Session Key (Hexadecimal): {session_key}")
    message = "Hello sou and zoz"
    enc = message_encryption(message,session_key)
    print(f"The cypher text : {enc}")
    original_text = message_decryption(enc,session_key)
    print("The original text : ",original_text)