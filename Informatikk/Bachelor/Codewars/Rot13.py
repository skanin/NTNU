dic = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm'
}


def rot13(message):
    enq_msg = ""
    for c in message:
        if c == c.upper() and c.lower() in dic:
            enq_msg += dic[c.lower()].upper()
            continue
        if c in dic:
            enq_msg += dic[c]
        else:
            enq_msg += c

    return enq_msg


print(rot13("test"))
print(rot13("Test"))


