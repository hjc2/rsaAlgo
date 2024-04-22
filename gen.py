import random

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_large_prime():
    while True:
        prime_candidate = random.randint(10**6, 10**7)
        if is_prime(prime_candidate):
            return prime_candidate

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(message, e, n):
    encrypted_message = pow(message, e, n)
    return encrypted_message

def decrypt(encrypted_message, d, n):
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message

def ascii_to_integer(string):
    integer_representation = int(''.join(str(ord(char)) for char in string))
    return integer_representation
    
def integer_to_ascii(integer):
    integer_str = str(integer)
    string_representation = ''.join(chr(int(integer_str[i:i+3])) for i in range(0, len(integer_str), 3))
    return string_representation

# Exampl
# Example usage:
integer = 72101108108111
result = integer_to_ascii(integer)
print("String representation:", result)



# Generate large prime numbers p and q
p = generate_large_prime()
q = generate_large_prime()

# Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Choose a public key 'e' such that 1 < e < phi_n and gcd(e, phi_n) = 1
e = random.randint(2, phi_n - 1)
while gcd(e, phi_n) != 1:
    e = random.randint(2, phi_n - 1)

# Calculate the private key 'd' using the modular inverse of 'e' mod phi_n
d = mod_inverse(e, phi_n)

# Message to be encrypted
message = "HiH"

messageIn = int(ascii_to_integer(message))

print(messageIn)

# Encrypt the message
encrypted_message = encrypt(messageIn, e, n)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, d, n)

dec = integer_to_ascii(decrypted_message)
print("Decrypted Message:", dec)
