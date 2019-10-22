codes = {
    '1111': 'M',
    '000': 'R',
    '001': 'L',
    '1000': 'I',
    '1010': 'E',
    '1011': 'A',
    '1100': 'N',
    '1101': 'V',
    '1110': 'T',
    '1001': 'O',
    '011': 'F'
}

def decode(str, decoded=''):
    if len(str) == 0:
        return decoded
    try:
        decoded += codes[str[:4]]
        return decode(str[4::], decoded)
    except KeyError:
        decoded += codes[str[:3]]
        return decode(str[3::], decoded)


s = '100011000111001000111110111110100010011100'
t = '000101011100001000101011011011001'
print(decode(s))
print(decode(t))


b1 = [2, 4, 5, 5]
b2 = [4, 1, 8, 3]

avstand = 0
for i in range(len(b1)):
    avstand += abs(b2[i]-b1[i])

print(avstand)