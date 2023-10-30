import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(cipher):
    return ''.join([chr(int(f"{ALPHABET.index(cipher[i]):04b}{ALPHABET.index(cipher[i+1]):04b}", 2)) for i in range(0, len(cipher), 2)])

def unshift(c, k):
    return ALPHABET[(ord(c) - ord(k)) % len(ALPHABET)]

encryptedFlag = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"

for key in ALPHABET:
    s = ''.join([unshift(c, key) for c in encryptedFlag])
    s = b16_decode(s)
    print(s)
