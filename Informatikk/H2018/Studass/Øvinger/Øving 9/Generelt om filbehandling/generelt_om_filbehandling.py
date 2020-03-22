def write_to(data):
    f = open('my_file.txt', 'w')
    f.write(data)
    f.close()
    print('Successful!!!')


def read_from(file):
    f = open(file, 'r')
    innhold = f.read()
    print(innhold)


def main():
    svar = ''

    while not svar == 'done':
        svar = input("Do you want to read or write? r/w ")
        if svar == 'r':
            try:
                read_from('my_file.txt')
            except FileNotFoundError:
                print('That file does not exist')
        elif svar == 'w':
            data = input('What do you want to write? ')

            write_to(data)

    print('Goodbye')


main()