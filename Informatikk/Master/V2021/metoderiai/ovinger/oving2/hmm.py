import numpy as np

class HiddenMarkovModel():
    def __init__(self, transition_probabilities, emission_probabilities, start_probabilities):
        self.transition_probabilities = transition_probabilities
        self.emission_probabilities = emission_probabilities
        self.start_probabilities = start_probabilities
    
    def get_emission_probabilities(self, state):
        if state == 'true':
            return np.array([[self.emission_probabilities[0][0], 0], [0, self.emission_probabilities[1][0]]])
        elif state == 'false':
            return np.array([[self.emission_probabilities[0][1], 0], [0, self.emission_probabilities[1][1]]])
        elif state == 'identity':
            return np.array([[1, 0], [0, 1]])


def normalize(arr):
    return arr/np.sum(arr)

def forward(hmm, f, ev):
    """
    Calculates alpha * O_t * T^T * f, where O_t is the observation matrix, T^T is the transition probabilities and f is the forward message
    """
    return normalize(np.dot(np.matmul(ev, hmm.transition_probabilities.transpose()), f))

def forward_backward(hmm, ev):
    """
    Smoothing algorithm for the Hidden Markov Model hmm and evidence ev.
    Uses evidence of both future and past to get an estimate of the probabilities.
    """
    time = len(ev)

    fv = np.zeros((time, 2))
    sv = np.zeros((time, 2))
    b = np.ones(2)

    fv[0] = normalize(hmm.start_probabilities)

    for i, obs in enumerate(ev):
        if i == 0:
            continue
        fv[i] = forward(hmm, fv[i-1], hmm.get_emission_probabilities(obs))


    for i, obs in reversed(list(enumerate(ev))):
        sv[i] = normalize(np.multiply(fv[i], b))
        if i != 0:
            b = np.dot(np.matmul(hmm.transition_probabilities, hmm.get_emission_probabilities(obs)), b)
    return sv

def task1b(hmm, ev):
    """
    Calculate P(X_t|e_{1:t}) for t = 1, 2, 3, 4, 5, 6.
    Using the forward algorihtm, which uses the evidence 'ev' (list of True/False values (the first one being None)) 
    and the Transition and emission probabilities in the Hidden Markov Model 'hmm'.
    """
    fv = np.zeros((len(ev), 2))
    fv[0] = hmm.start_probabilities # The first one are just the start probabilities
    
    for i, obs in enumerate(ev):
        if i == 0: # If i == 0, we are at the evidence 'None'
            continue
        fv[i] = forward(hmm, fv[i-1], hmm.get_emission_probabilities(obs)) # Calculate the probability

    return fv
    
def task1c(hmm, obs):
    """
    Calculates P(X_t|e_{1:6}) for t = 7 to 30.
    Basically just uses the forward algorithm with evidence = the identity matrix.
    """
    fv = np.zeros((31, 2))
    fv[0:len(obs)] = task1b(hmm, obs)
    for i in range(len(obs), 31):
        fv[i] = forward(hmm, fv[i-1], hmm.get_emission_probabilities('identity'))
    return fv

def task1d(hmm, obs):
    """
    Calculates P(X_t|e_{1:6}) for t = 0 to len(evidence), uses the forward-backward algorithm.
    (The task asked for t = 0 to 5, but I compute all and just print 0 - 5 later).
    """
    return forward_backward(hmm, obs)

def task1e(hmm, obs):
    """
    Calculates argmax P(x_1 ... x_{t-1}, X_t|e_{1:t}), for t = 1 to 6.
    That is - it finds the most likely sequence of events, given a Hidden Markov model and evidence.
    """
    mt = np.zeros((len(obs), 2, 1))
    mt[0] = hmm.start_probabilities.reshape((2,1))

    for i, ev in enumerate(obs):
        if i == 0:
            continue
        if i == 1:
            mt[i] = forward(hmm, mt[0], hmm.get_emission_probabilities(ev)).reshape(2,1)
        else:
            # This is just the dot product between the evidence, and the max of the rows between the element wise multiplication between the transition probabilities and last message.
            mt[i] = np.dot(hmm.get_emission_probabilities(ev), np.max(np.array([hmm.transition_probabilities[:,0] * mt[i-1][0], hmm.transition_probabilities[:,1] * mt[i-1][1]]), axis=0).reshape((2,1)))
    return mt


if __name__ == '__main__':
    transition_probabilities_fish = np.array([[.8, .2], [.3, .7]])

    emission_probabilities_fish = np.array([[.75, .25], [.2, .8]])

    start_probabilities_fish = np.array([0.5, 0.5])
    
    observations = [None, 'true', 'true', 'false', 'true', 'false', 'true']

    hmm = HiddenMarkovModel(transition_probabilities_fish, emission_probabilities_fish, start_probabilities_fish)

    print('#######################')
    print('#       Task 1b       #')
    print('#######################')
    print('P(X_t|e_1:t): [Fish nearby, No fish nearby]')
    print('-------------------------------------------\n')
    for i, probs in enumerate(task1b(hmm, observations)):
        if i == 0:
            continue
        print(f'P(X_{i}|e_1:{i}): {probs}')
    
    print()
    print('#######################')
    print('#       Task 1c       #')
    print('#######################')
    print('P(X_t|e_1:6): [Fish nearby, No fish nearby]')
    print('-------------------------------------------\n')
    for i, probs in enumerate(task1c(hmm, observations)[len(observations):]):
        print(f'P(X_{i+len(observations)}|e_1:6): {probs}')
    
    print()
    print('#######################')
    print('#       Task 1d       #')
    print('#######################')
    print('P(X_t|e_1:6): [Fish nearby, No fish nearby]')
    print('-------------------------------------------\n')
    for i, probs in enumerate(task1d(hmm, observations)[0:6]):
        print(f'P(X_{i}|e_1:6): {probs}')

    print()
    print('#######################')
    print('#       Task 1e       #')
    print('#######################')
    print('Most likely sequence (1-6)')
    print('-------------------------------------------\n')
    mappings = {
        0: 'Fish',
        1: 'No fish'
    }
    for i, probs in enumerate(task1e(hmm, observations)[1:]):
        amax = np.argmax(probs)
        print(f'{mappings[amax]}: {probs[amax]}')