def fu2(input):
    r = 0
    s = 0
    t = 0
    u = 0
    n = len(input)
    for c in input:
        if(c.isalpha()):
            r = r + 1
        elif(c.isdigit()):
            s = s + 1
        elif(c==' '):
            t = t + 1
        else:u = u + 1
    r = 100*r/n
    s = 100*s/n
    t = 100*t/n
    u = 100*u/n
    return(r,s,t,u)


print(fu2("Ut pa tur, aldri sur"))