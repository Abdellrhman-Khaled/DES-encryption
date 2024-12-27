Overview:

The Word Cipher is an advanced command-line utility for secure communication. It now features encryption, decryption, and peer-to-peer messaging using sockets with the Diffie-Hellman key exchange for secure session key generation. This ensures robust communication while maintaining data confidentiality.

Features:

Encryption: Input any word and a secret key to produce the encrypted ciphertext.
Decryption: Reverse the process by inputting the ciphertext and the secret key to retrieve the original word.
Diffie-Hellman Key Exchange: Securely exchange keys between peers to establish a shared session key.
Peer-to-Peer Communication: Use sockets to enable two peers to communicate securely by encrypting messages with the session key.
Usage

Installation:

Clone this repository to your local machine.
Ensure you have Python installed (version 3.6 or higher).

Start Peer 1:
Run the following script to act as the server:

python
Copy code
import socket  
from diffi import generate_dh_parameters, generate_dh_keys, compute_shared_key, hex_session_key  
from Text_encryption_decryption import message_encryption, message_decryption  

# Peer 1 (Server) setup code...  
Start Peer 2:
Use a complementary script to connect to the server, exchange keys, and begin encrypted communication.

Example Peer Communication

Peer 1 initializes the Diffie-Hellman parameters and generates its keys:

Sends p, g, and public key to Peer 2.
Receives Peer 2’s public key and computes a shared session key.
Peer 2 follows the same steps, ensuring both peers establish a secure channel.

Encrypted messages are then exchanged as follows:

Peer 1: Encrypts and sends a message using the session key.
Peer 2: Decrypts the message and responds similarly.
Example Interaction:

Peer 1:

You: Hello, Peer 2!  
Peer 2: Hi, Peer 1! How are you?  

Notes:

Diffie-Hellman ensures secure key exchange without directly transmitting sensitive information.
Encryption and decryption maintain message confidentiality during peer-to-peer communication.
Ensure proper key management and keep your session key confidential.
