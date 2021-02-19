import binascii
import random

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

def main(message):
    keyList=[]
    seq=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in range (len(message)):
        keyList.append(random.choice(seq))
    key = ''.join(keyList)

    print(encrypt(message, key))
    print(decrypt(encrypt(message, key), key))


m = input('Message(english characters only): ')
main(m)
