import random

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def mod_inverse(a, p):
    return pow(a, p - 2, p)

def generate_keys(p, g):
    private_key = random.randint(2, p - 2)
    public_key = mod_exp(g, private_key, p)
    return private_key, public_key

def encrypt(p, g, public_key, message):
    k = random.randint(2, p - 2)
    c1 = mod_exp(g, k, p)
    c2 = (message * mod_exp(public_key, k, p)) % p
    return c1, c2

def decrypt(p, private_key, c1, c2):
    s = mod_exp(c1, private_key, p)
    s_inv = mod_inverse(s, p)
    message = (c2 * s_inv) % p
    return message

if '__name__' == "_main_":
    p = int(input("Enter a prime number p: "))
    g = int(input("Enter a Generator: "))
    
    private_key, public_key = generate_keys(p, g)
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    message = int(input("Enter the message (as an integer) to encrypt: "))
    
    c1, c2 = encrypt(p, g, public_key, message)
    print(f"Encrypted Message: ({c1}, {c2})")
    
    decrypted_message = decrypt(p, private_key, c1, c2)
    print(f"Decrypted Message: {decrypted_message}")