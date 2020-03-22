def read_from_file(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


print(read_from_file('BIBLE.txt'))