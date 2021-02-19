import numpy as np
import random 

class Percepton:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
        self.threshold = 1000
        self.weights = np.zeros(3)
        self.bias = random.uniform(-0.5, 0.5)

    def predict(self, inputs, train=True):
        yp = np.dot(inputs, self.weights)
        return 1 if yp > 0 else 0
    
    def train(self, train_data):
        for i in range(self.threshold):
            x, expected = random.choice(train_data)
            prediction = self.predict(x)
            self.weights += self.learning_rate * (expected - prediction) * x


def main():
    p_and = Percepton()
    p_or = Percepton()

    training_set_AND = [
        (np.array([0, 0, 1]), 0),
        (np.array([0, 1, 1]), 0),
        (np.array([1, 0, 1]), 0),
        (np.array([1, 1, 1]), 1),
    ]

    training_set_OR = [
        (np.array([0, 0, 1]), 0),
        (np.array([0, 1, 1]), 1),
        (np.array([1, 0, 1]), 1),
        (np.array([1, 1, 1]), 1),
    ]

    p_and.train(training_set_AND)
    p_or.train(training_set_OR)

    values = [
        np.array([0, 0, 1]),
        np.array([0, 1, 1]),
        np.array([1, 0, 1]),
        np.array([1, 1, 1]),
    ]

    string = "------------ AND ------------" + "\t" * 2 + "------------ OR ------------\n"
    for val in values:
        string += f'[{val[0]}, {val[1]}] --> {p_and.predict(val, train=False):<29}'
        string += f'[{val[0]}, {val[1]}] --> {p_or.predict(val)}'
        string += '\n'

    string += f'\n\nWeights: {p_and.weights}\t\tWeigths: {p_or.weights}\nBias: {p_and.weights[2]}\t\t\t\tBias: {p_or.weights[2]}\n'
    print(string)
    # print(p.predict(np.array([[0, 1,1]])))

    p_xor = Percepton()

    training_set_XOR = [
        (np.array([0, 0, 1]), 0),
        (np.array([0, 1, 1]), 1),
        (np.array([1, 0, 1]), 1),
        (np.array([1, 1, 1]), 0),
    ]

    for val in values:
        print(f'{val}: {p_xor.predict(val)}')


if __name__ == "__main__":
    for i in range(3):
        main()
    