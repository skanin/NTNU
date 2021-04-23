class TreeNode:
    def __init__(self, label, value, id, parent=None):
        self.label = label
        self.value = value
        self.id = id
        self.parent = parent
        self.branches = {}
        self.continous = False

    def add_branch(self, label, subtree):
        self.branches[label] = subtree