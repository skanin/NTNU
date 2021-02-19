def fu3(a):
    if(a<=2):
        r = 1
    else:
        r = 1 + fu3(a/2)

    return r


print(fu3(100))