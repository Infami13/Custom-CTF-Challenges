files = ['plaintext.txt', 'ciphertext.txt', 'message.txt']
content = []
for file in files:
    f = open(file, 'rb')
    content.append(f.read())
    f.close()

plaintext, ciphertext, message = content

key = int.from_bytes(plaintext) ^ int.from_bytes(ciphertext)
decrypt = int.from_bytes(message) ^ key
print(decrypt.to_bytes(20))
