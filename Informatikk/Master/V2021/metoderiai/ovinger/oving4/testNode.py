class Node:
    def __init__(self, name, children, parents, value=None):
        self.name = name
        self.value = value
        self.parents = parents
        self.children = children
    
    def set_value(self, value):
        self.value = value

    def add_parents(self, parents):
        self.parents.extend(parents)

    def add_children(self, children):
        self.children.extend(children)
    


if __name__ == '__main__':
    a = Node('a', [], [])
    print(a.children)
    b = Node('b', [], [])
    print(b.children)
    a.add_children(['b'])
    print(a.children)
    print(b.children)