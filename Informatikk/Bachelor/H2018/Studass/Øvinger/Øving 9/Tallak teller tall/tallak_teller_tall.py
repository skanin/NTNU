def number_of_lines(filename):
    f = open(filename, 'r')
    i = 1
    for c in f.read():
        if c == '\n':
            i += 1

    f.close()
    return i


print(number_of_lines('numbers.txt'))


freq = {}
def number_frequency(filename):
    f = open(filename, 'r')

    for c in f.read():
        if c.strip() == "":
            continue

        if c.strip() in freq:
            freq[c.strip()] += 1
        else:
            freq[c.strip()] = 1


number_frequency('numbers.txt')
print(freq)

for key in freq:
    print(key + ": " + str(freq[key]))

