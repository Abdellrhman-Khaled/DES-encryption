Overview:

The Word Cipher is a command-line utility that enables users to both encrypt and decrypt words using a secret key. By inputting a word and its corresponding key, the tool generates the encrypted ciphertext or retrieves the original word from the ciphertext. This is ideal for secure communication or safeguarding sensitive information.

Features:

Encryption: Input any word and a secret key to produce the encrypted ciphertext.
Decryption: Reverse the process by inputting the ciphertext and the secret key to retrieve the original word.
Usage

Installation:

Clone this repository to your local machine.
Ensure you have Python installed (version 3.6 or higher).
Run the Encryption or Decryption:

Open a terminal or command prompt.
Navigate to the project directory.
Execute the following command:
bash
Copy code
python DES.py  
Follow the prompts to input your word or ciphertext and secret key.
Example

To encrypt the word “266200199BBCDFF1” with the key “0123456789ABCDEF”:

Input word: 266200199BBCDFF1
Secret key: 0123456789ABCDEF
Ciphertext: 4E0E6864B5E1CA52

To decrypt the ciphertext 4E0E6864B5E1CA52 using the same key:

Ciphertext: 4E0E6864B5E1CA52
Secret key: 0123456789ABCDEF
Original word: 266200199BBCDFF1

Notes:

Choose a strong and unique key for better security.
Keep your key confidential; anyone with the key can decrypt the ciphertext.
Feel free to contribute or enhance this tool by submitting pull requests!
