
from pydoc import plain


def totient(p, q):
    return (p - 1) * (q - 1)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Took from SO
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

    
def choose_public_exponent(phi):
    # Choose a public exponent E that is coprime to phi
    E = 2
    while gcd(E, phi) != 1:
        E += 1
    return E

def encode_ascii_to_number(text):
    total = 0
    for i, char in enumerate(text):
        total = total * 100 + ord(char)
    return total
def decode_number_to_ascii(number):
    text = ""
    while number > 0:
        text = chr(number % 100) + text
        number //= 100
    return text
    
def rsa_encrypt(plaintext, E, n):
    M = encode_ascii_to_number(plaintext)
    print("after encode " + str(M))
    ciphertext = pow(M, E, n)
    return ciphertext

def rsa_decrypt(ciphertext, d, n):
    # Decrypt the ciphertext to get the integer M

    M = pow(ciphertext, d, n)
    print("descryped text " + str(M))

    plaintext = decode_number_to_ascii(M)

    return plaintext
    
