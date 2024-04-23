
def totient(p, q):
    return (p - 1) * (q - 1)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def public_exponent(phi):
    E = 2
    while gcd(E, phi) != 1:
        E += 1
    return E

def rsa_encrypt(plaintext, E, n):
    return pow(plaintext, E, n)

def rsa_decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)
    