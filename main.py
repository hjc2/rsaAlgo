

from ascii import encodeAscii, decodeAscii

from rsa import totient, choose_public_exponent, modinv, rsa_encrypt, rsa_decrypt


print(encodeAscii("k"))


p = 923978444369

q = 496509772799

n = p * q

phi = totient(p, q)

e = choose_public_exponent(phi)
d = modinv(e, phi)

P = "Hello!"

print("p : " + str(p))
print("q : " + str(p))
print("n : " + str(n))

print("phi : " + str(phi))
print("e : " + str(e))
print("d : " + str(d))
print("")

print("Public key (E, n):", (e, n))
print("Private key (d, n):", (d, n))

encodedText = int(encodeAscii(P))
print("text after ascii encoding as integer : " + str(encodedText))
ciphertext = rsa_encrypt(encodedText, e, n)

print("Ciphertext: " + str(ciphertext))

decrypted_text = rsa_decrypt(ciphertext, d, n)

decodedText = decodeAscii(decrypted_text)

print("Decrypted text: " + str(decodedText))
