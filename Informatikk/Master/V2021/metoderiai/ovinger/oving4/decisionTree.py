import pandas as pd
import numpy as np
from treeNode import TreeNode
from graphviz import Digraph
from collections import defaultdict

class DecisionTree:
    def __init__(self, data, classifier, classifier_positive, classifier_negative, continous):
        self.data = data
        self.data.fillna(self.data.mean(), inplace=True)
        self.classifier = classifier
        self.classifier_pos = classifier_positive
        self.classifier_neg = classifier_negative
        self.curr_id = 0
        self.color_mappings = defaultdict(lambda: 'black')
        self.color_mappings[self.classifier_neg] = 'red'
        self.color_mappings[self.classifier_pos] = 'green'
        self.continous = continous
        
    def _get_id(self):
        _id = self.curr_id
        self.curr_id += 1
        return str(_id)

    def decision_tree_learning(self, examples, attributes, parent_examples):
        try:
            attributes.remove(self.classifier)
        except:
            pass
        
        if not len(examples):
            return self.plurality_value(parent_examples)
        elif self.has_same_classifications(examples):
            return TreeNode(examples[self.classifier].iloc[0], examples[self.classifier].iloc[0], self._get_id())
        elif not len(attributes):
            return self.plurality_value(examples)

        max_attr_tupl = max(self.importance(examples, attributes), key=lambda x: x[0])

        A = max_attr_tupl[1]
        
        tree = TreeNode(A, None, self._get_id())
        tree.continous = A in self.continous
        attributes.remove(A) 
        if A not in self.continous:
            for value in sorted(self.data[A].unique()):
                exs = examples[examples[A] == value]
                subtree = self.decision_tree_learning(
                    exs, attributes.copy(), examples.copy())
                tree.add_branch(value, subtree)
                subtree.parent = tree
        else:
            for i, exs in enumerate([examples[examples[A] < max_attr_tupl[2]], examples[examples[A] > max_attr_tupl[2]]]):
                subtree = self.decision_tree_learning(exs, attributes.copy(), examples.copy())
                op = '<' if i == 0 else '>'
                tree.add_branch(f'{op}{max_attr_tupl[2]}', subtree)
                subtree.parent = tree
        return tree

    def plurality_value(self, examples):
        value = examples[self.classifier].value_counts().idxmax(1)
        return TreeNode(value, value, self._get_id())

    def has_same_classifications(self, examples):
        return len(examples[self.classifier].unique()) == 1

    def B(self, q):
        return 0.0 if (q == 0 or (1-q) == 0) else -(q * np.log2(q) + (1-q)*np.log2(1-q))

    def remainder(self, data, key, p, n, examples):
        tmp_sum = 0
        for value in examples[key].unique():
            if value == self.classifier:
                continue
            try:
                pk = data[(self.classifier_pos, value)]
            except KeyError:
                pk = 0
            
            try:
                nk = data[(self.classifier_neg, value)]
            except KeyError:
                nk = 0

            tmp_sum += ((pk + nk) / (p + n)) * self.B(pk / (pk + nk))

        return tmp_sum

    def importance(self, examples, attributes):
        l = []
        for key in attributes:
            tmp = examples.groupby(self.classifier)[
                    key].value_counts().unstack(fill_value=0).stack()
            p, n = tmp[(self.classifier_pos, )].sum(), tmp[(self.classifier_neg, )].sum()
            if key in self.continous:
                sorted_values = sorted(examples[key].unique())
                curr_best_gain = None
                curr_best_valsplit = None
                for value in sorted_values:
                    less_than_or_equal = examples[examples[key] < value]
                    if not len(less_than_or_equal):
                        continue
                    tmp2 = less_than_or_equal.groupby(self.classifier)[
                        key].value_counts().unstack(fill_value=0).stack()

                    try:
                        p2 = tmp2[(self.classifier_pos, )].sum()
                    except KeyError:
                        p2 = 0

                    try:
                        n2 = tmp2[(self.classifier_neg, )].sum()
                    except KeyError:
                        n2 = 0

                    gain = self.B(p2 / (p2 + n2)) - self.remainder(tmp2, key, p2, n2, less_than_or_equal)
                    if curr_best_gain is None or gain >= curr_best_gain:
                        curr_best_gain = gain
                        curr_best_valsplit = value
                if curr_best_gain is None:
                    curr_best_gain = 0
                    curr_best_valsplit = 0
                else:
                    ind = sorted_values.index(curr_best_valsplit)
                    if len(sorted_values) == 2 and 0 in sorted_values and 2 in sorted_values:
                      pass  
                    elif ind != len(sorted_values)-1:
                        curr_best_valsplit = (sorted_values[ind] + sorted_values[ind + 1])/2
                    else:
                        curr_best_valsplit = (sorted_values[ind-1] + sorted_values[ind])/2
                    
                l.append((curr_best_gain, key, curr_best_valsplit))
            else:
                remainder = self.remainder(tmp, key, p, n, examples)
                l.append((self.B(p / (p + n)) - remainder, key))
        return l

    def generate_nodes_and_edges(self, tree, graph):
        graph.node(tree.id, str(tree.label), shape='box')
        for key, val in tree.branches.items():
            color = self.color_mappings[val.label]
            style = 'filled' if color != 'black' else ''
            fontcolor = 'white' if color == 'red' else 'black'
            graph.node(val.id, str(val.label), shape='box',
                       color=color, style=style, fontcolor=fontcolor)
            if val.parent is not None:
                graph.edge(val.parent.id, val.id, label=str(key))

        l = filter(lambda x: x[1], tree.branches.items())
        for node in l:
            self.generate_nodes_and_edges(node[1], graph)

    def draw_tree(self, tree, graph_name):
        graph = Digraph(format='pdf')
        self.generate_nodes_and_edges(tree, graph)
        graph.render(f'{graph_name}.gv', view=True)


def predict(tree, data):
    if not len(list(tree.branches.items())):
        return tree.value
    if tree.continous:
        keys = list(tree.branches.keys())
        keys = list(map(lambda x: (x, eval(f'{data[tree.label]}{x}')), keys))
        key = list(filter(lambda x: x[1], keys))[0][0]
    else:
        key = data[tree.label]

    return predict(tree.branches[key], data)

def run_titanic_example(columns, filename):
    data = pd.read_csv('titanic/train.csv')
    data.fillna(data.mean(), inplace=True)
    dt: DecisionTree = DecisionTree(data, 'Survived', 1, 0, ['Age', 'Parch', 'Ticket', 'SibSp'])
    tree = dt.decision_tree_learning(dt.data, columns, None)
    dt.draw_tree(tree, filename)
    predictions = []
    test = pd.read_csv('titanic/test.csv')
    test.fillna(test.mean(), inplace=True)
    for _, row in test.iterrows():
        prediction = predict(tree, row)
        predictions.append(prediction == row['Survived'])

    print(f'Accuracy: {sum(predictions)/len(predictions)}')


if __name__ == '__main__':
    print('Problem A: ')
    run_titanic_example(['Sex', 'Embarked', 'Pclass', 'Survived'], 'DecisionTreeProblemA')
    print('--------------------')
    print('Problem B:')
    run_titanic_example(['Sex', 'Embarked', 'Pclass', 'Parch', 'Ticket', 'Age', 'SibSp', 'Survived'], 'DecisionTreeProblemB')
    

