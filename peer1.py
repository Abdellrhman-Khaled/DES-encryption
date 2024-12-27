import socket
from diffi import generate_dh_parameters, generate_dh_keys, compute_shared_key, hex_session_key
from Text_encryption_decryption import message_decryption, message_encryption

# Generate Diffie-Hellman parameters
p, g = generate_dh_parameters()
private_key, public_key = generate_dh_keys(p, g)
# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5001))
server.listen(1)
print("Waiting for Peer 2 to connect...")

conn, addr = server.accept()
print("Peer 2 connected.")

# Exchange keys
conn.send(f"{p},{g},{public_key}".encode())  # Send p, g, and public_key
peer_public_key = int(conn.recv(1024).decode())  # Receive Peer 2's public key

# Compute shared session key
shared_key = compute_shared_key(peer_public_key, private_key, p)
session_key = hex_session_key(shared_key)
print(f"Session Key: {session_key}")

# Messaging loop
while True:
    message = input("You: ")
    encrypted_message = message_encryption(message, session_key)
    conn.send(encrypted_message.encode())

    received = conn.recv(1024).decode()
    decrypted_message = message_decryption(received, session_key)
    print(f"Peer 2: {decrypted_message}")
