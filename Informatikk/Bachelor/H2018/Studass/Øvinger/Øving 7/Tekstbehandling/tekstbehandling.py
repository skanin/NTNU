print("A-------------------------\n")


def clean_and_uppercase(st):
    return st.upper().strip()


print(clean_and_uppercase(" \n  The Sky's Awake So I'm Awake  \t  "))
print()
print("B-------------------------\n")


def split_str(st, ch):
    return st.split(ch)


print(split_str("Hakuna Matata", "a"))
print("D-------------------------\n")
print()


def zZz():
    for i in range(1, 8):
        print("Z"*i)
    for i in range(8,0,-1):
        print("Z"*i)


zZz()
