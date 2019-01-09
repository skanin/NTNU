import itertools


def get_pins(observed):
    dic = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['5', '9'],
        '7': ['4', '8'],
        '8': ['5', '7', '9', '0'],
        '9': ['6', '8'],
        '0': ['8']
    }


    temp = []
    for elem in observed:
        temp2 = [elem]
        for elem in dic[elem]:
            temp2.append(elem)
        temp.append(temp2)

    temp3 = []
    for elem in temp:
        st = ''.join(elem)
        print(st)
        temp3.append([''.join(comb) for comb in itertools.product(st, repeat=len(observed))])

    return temp3
    '''
    it = list(itertools.combinations_with_replacement(''.join(lst), len(observed)))
    for elem in itertools.permutations(''.join(lst), len(observed)):
        it.append(elem)

    return list(set([''.join(elem) for elem in it]))
    '''
    # temp = [''.join(elem) for elem in it]
    '''
    print(temp)
    if len(observed) > 1:
        for i in lst:
            if i*len(observed) not in temp:
                temp.append(i*len(observed))

    return temp
    '''


print(sorted(get_pins('369')))