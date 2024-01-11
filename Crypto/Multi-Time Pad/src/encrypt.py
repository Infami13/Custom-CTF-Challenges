def encrypt(plaintext, key):
    ciphertext = b''
    for p, k in zip(plaintext, key):
        ciphertext += (p ^ k).to_bytes()
    return ciphertext

