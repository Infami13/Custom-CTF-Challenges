file = open('message.txt', 'rb')
plaintext = file.read()
file.close()

if len(plaintext) % 2:
    plaintext += b'\x00'

key = 16904
ciphertext = b''
for i in range(0, len(plaintext), 2):
    plain_block = plaintext[i:i+2]
    cipher_bytes = int.from_bytes(plain_block) ^ key
    ciphertext += int.to_bytes((cipher_bytes & 0xff00) >> 8)
    ciphertext += int.to_bytes(cipher_bytes & 0xff)

file = open('ciphertext.txt', 'wb')
file.write(ciphertext)
file.close()


    
