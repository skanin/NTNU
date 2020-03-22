import math


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def sum_stack(self):
        return sum(self.items)

    def clear_stack(self):
        self.items = []

    def largest(self):
        return max(self.items)

f = open("input.spp", 'r')

temp = ""
for c in f:
    c = c.strip("\n")
    for j in c:
        temp += j

''''
rules = {
    " ":
}
'''

stack = Stack()


def space(a):
    push(a, 31)

def kolon(a):
    summ = sum(a)
    a.clear()
    push(a, summ)


def strek(a):
    push(a, 3)


def apostroff(a):
    b = pop(a)
    c = pop(a)

    push(a, b + c)


def punktum(a):
    b = pop(a)
    c = pop(a)
    push(a, b-c)
    push(a, c-b)


def underscore(a):
    b = pop(a)
    c = pop(a)

    push(a, b * c)
    push(a, b)


def slash(a):
    pop(a)


def i(a):
    push(a, peek(a))


def backslash(a):
    b = pop(a)

    push(a, b+1)


def star(a):
    b = pop(a)
    c = pop(a)

    push(a, int(math.floor(b/c)))


def left_bracket(a):
    b = pop(a)

    if b % 2 == 0:
        push(a, 1)


def right_bracket(a):
    b = pop(a)

    if b % 2 != 0:
        push(a, b)


def tilde(a):
    b = pop(a)
    c = pop(a)
    d = pop(a)

    push(a, max(b, c, d))


def push(a, val):
    a.insert(0, val)


def pop(a):
    print(a)
    b = a[0]
    del a[0]

    return b


def peek(a):
    return a[0]


j = 0
'''
switch = {
    " ": space(),
    ":": kolon(),
    "|": strek(),
    "'": apostroff(),
    ".": punktum(),
    "_": underscore(),
    "/": slash(),
    "i": i(),
    r'"\"': backslash(),

}
'''
a = []
print(temp)
while j < len(temp):
    c = temp[j]
    if c == " ":
        space(a)
    elif c == ":":
        kolon(a)
    elif c == "|":
        strek(a)
    elif c == "'":
        apostroff(a)
    elif c == ".":
        punktum(a)
    elif c == "_":
        underscore(a)
    elif c == "/":
        slash(a)
    elif c == "i":
        i(a)
    elif c == r'\\'[1]:
        backslash(a)
    elif c == "*":
        star(a)
    elif c == "]":
        left_bracket(a)
    elif c == "[":
        right_bracket(a)
    elif c == "~":
        tilde(a)

    if c == "k":
        j += 3
    else:
        j += 1

print(max(a))