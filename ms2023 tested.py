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

    ###
    ###
    ##
    ##
    #
    #

def test_mod_exp():
    print("Testing mod_exp...")
    assert mod_exp(2, 3, 5) == 3, "Failed: 2^3 % 5 should be 3"
    assert mod_exp(5, 2, 13) == 12, "Failed: 5^2 % 13 should be 12"
    assert mod_exp(10, 0, 7) == 1, "Failed: 10^0 % 7 should be 1"
    print("mod_exp passed all tests.")

def test_mod_inverse():
    print("Testing mod_inverse...")
    assert mod_inverse(3, 7) == 5, "Failed: Modular inverse of 3 mod 7 should be 5"
    assert mod_inverse(4, 11) == 3, "Failed: Modular inverse of 4 mod 11 should be 3"
    assert mod_inverse(10, 17) == 12, "Failed: Modular inverse of 10 mod 17 should be 12"
    print("mod_inverse passed all tests.")

def test_generate_keys():
    print("Testing generate_keys...")
    p = 23
    g = 5
    private_key, public_key = generate_keys(p, g)
    assert 2 <= private_key < p - 1, "Failed: Private key is out of valid range."
    assert public_key == mod_exp(g, private_key, p), "Failed: Public key calculation is incorrect."
    print(f"Generated Keys: Private Key={private_key}, Public Key={public_key}")
    print("generate_keys passed all tests.")

def test_encrypt_decrypt():
    print("Testing encrypt and decrypt...")
    p = 23
    g = 5
    private_key, public_key = generate_keys(p, g)
    message = 15
    c1, c2 = encrypt(p, g, public_key, message)
    decrypted_message = decrypt(p, private_key, c1, c2)
    assert decrypted_message == message, f"Failed: Decrypted message {decrypted_message} does not match original {message}."
    print(f"Original Message: {message}, Encrypted: ({c1}, {c2}), Decrypted: {decrypted_message}")
    print("encrypt and decrypt passed all tests.")

def all_tests():
    test_mod_exp()
    test_mod_inverse()
    test_generate_keys()
    test_encrypt_decrypt()

if __name__ == "__main__":
    all_tests()
