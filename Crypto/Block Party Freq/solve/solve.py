file = open('ciphertext.txt', 'rb')
ciphertext = file.read()
file.close()

cipher_blocks = []
for i in range(0, len(ciphertext), 2):
    cipher_blocks.append(ciphertext[i:i+2])

commonness = 0
for block in set(cipher_blocks):
    if cipher_blocks.count(block) > commonness:
        most_common_block = block
        commonness = cipher_blocks.count(block)

key = int.from_bytes(most_common_block) ^ int.from_bytes(b'th')
key_pad = b''.join([key.to_bytes(2)] * len(cipher_blocks))

plaintext = b''
for c, k in zip(ciphertext, key_pad):
    plaintext += (c ^ k).to_bytes()

file = open('plaintext.txt', 'wb')
file.write(plaintext)
file.close()
