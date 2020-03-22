# a


import binascii
import random, string


def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)


def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')


def encrypt(message, key):
    message = bytes(message, encoding='ascii')
    key = bytes(key, encoding='ascii')
    message_hex = toHex(message)
    key_hex = toHex(key)
    code = message_hex ^ key_hex

    return code


# b


def decrypt(code, key):
    key = bytes(key, encoding='ascii')
    key_hex = toHex(key)
    message = code ^ key_hex

    return toString(message)


# c

def randomword(lengde):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(lengde))


def main(setning):
    key = randomword(len(setning))
    print("Encrypted: ", encrypt(setning, key))
    print("Decrypted: ", decrypt(encrypt(setning, key), key))


setning = input("Skriv inn en setning du vil kryptere: ")
main(setning)
