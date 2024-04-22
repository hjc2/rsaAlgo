
def totient(p, q):
    return (p - 1) * (q - 1)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
    
def public_exponent(phi):
    E = 2
    while gcd(E, phi) != 1:
        E += 1
    return E

def rsa_encrypt(plaintext, E, n):
    return pow(plaintext, E, n)

def rsa_decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)
    