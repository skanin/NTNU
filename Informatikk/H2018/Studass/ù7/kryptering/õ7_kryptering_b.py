import binascii

def toHex(word):
    word = bytes(word, encoding = 'ascii')
    return int(str(binascii.hexlify(word), 'ascii'), 16)
 
def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(message, key):
    if len(key)==len(message):
        messageHex = toHex(message)
        keyHex = toHex(key)
        code = messageHex ^ keyHex
        return code
    else:
        print('Message and key most be of same length!')

def decrypt(code, key):
    keyHex = toHex(key)
    messageHex = int(code) ^ keyHex
    message = toString(messageHex)
    return message


c = input('Encrypted code: ')
k = input('Key: ')

print(decrypt(c, k))
