import socket
from diffi import generate_dh_parameters, generate_dh_keys, compute_shared_key, hex_session_key
from Text_encryption_decryption import message_decryption, message_encryption


# Connect to Peer 1
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5001))


# Receive Diffie-Hellman parameters and Peer 1's public key
data = client.recv(1024).decode()
p, g, peer_public_key = map(int, data.split(","))

# Generate own keys
private_key, public_key = generate_dh_keys(p, g)
client.send(str(public_key).encode())  # Send public key to Peer 1

# Compute shared session key
shared_key = compute_shared_key(peer_public_key, private_key, p)
session_key = hex_session_key(shared_key)
print(f"Session Key: {session_key}")

# Messaging loop
while True:
    received = client.recv(1024).decode()
    decrypted_message = message_decryption(received, session_key)
    print(f"Peer 1: {decrypted_message}")

    message = input("You: ")
    encrypted_message = message_encryption(message, session_key)
    client.send(encrypted_message.encode())
