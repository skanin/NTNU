from collections import defaultdict

import numpy as np
from numpy.core.fromnumeric import var
import copy
import itertools

class Variable:
    def __init__(self, name, no_states, table, parents=[], no_parent_states=[]):
        """
        name (string): Name of the variable
        no_states (int): Number of states this variable can take
        table (list or Array of reals): Conditional probability table (see below)
        parents (list of strings): Name for each parent variable.
        no_parent_states (list of ints): Number of states that each parent variable can take.

        The table is a 2d array of size #events * #number_of_conditions.
        #number_of_conditions is the number of possible conditions (prod(no_parent_states))
        If the distribution is unconditional #number_of_conditions is 1.
        Each column represents a conditional distribution and sum to 1.

        Here is an example of a variable with 3 states and two parents cond0 and cond1,
        with 3 and 2 possible states respectively.
        +----------+----------+----------+----------+----------+----------+----------+
        |  cond0   | cond0(0) | cond0(1) | cond0(2) | cond0(0) | cond0(1) | cond0(2) |
        +----------+----------+----------+----------+----------+----------+----------+
        |  cond1   | cond1(0) | cond1(0) | cond1(0) | cond1(1) | cond1(1) | cond1(1) |
        +----------+----------+----------+----------+----------+----------+----------+
        | event(0) |  0.2000  |  0.2000  |  0.7000  |  0.0000  |  0.2000  |  0.4000  |
        +----------+----------+----------+----------+----------+----------+----------+
        | event(1) |  0.3000  |  0.8000  |  0.2000  |  0.0000  |  0.2000  |  0.4000  |
        +----------+----------+----------+----------+----------+----------+----------+
        | event(2) |  0.5000  |  0.0000  |  0.1000  |  1.0000  |  0.6000  |  0.2000  |
        +----------+----------+----------+----------+----------+----------+----------+

        To create this table you would use the following parameters:

        Variable('event', 3, [[0.2, 0.2, 0.7, 0.0, 0.2, 0.4],
                              [0.3, 0.8, 0.2, 0.0, 0.2, 0.4],
                              [0.5, 0.0, 0.1, 1.0, 0.6, 0.2]],
                 parents=['cond0', 'cond1'],
                 no_parent_states=[3, 2])
        """
        self.name = name
        self.no_states = no_states
        self.table = np.array(table)
        self.parents = parents
        self.no_parent_states = no_parent_states

        if self.table.shape[0] != self.no_states:
            raise ValueError(f"Number of states and number of rows in table must be equal. "
                             f"Recieved {self.no_states} number of states, but table has "
                             f"{self.table.shape[0]} number of rows.")

        if self.table.shape[1] != np.prod(no_parent_states):
            raise ValueError("Number of table columns does not match number of parent states combinations.")

        if not np.allclose(self.table.sum(axis=0), 1):
            raise ValueError("All columns in table must sum to 1.")

        if len(parents) != len(no_parent_states):
            raise ValueError("Number of parents must match number of length of list no_parent_states.")

    def __str__(self):
        """
        Pretty string for the table distribution
        For printing to display properly, don't use variable names with more than 7 characters
        """
        width = int(np.prod(self.no_parent_states))
        grid = np.meshgrid(*[range(i) for i in self.no_parent_states])
        s = ""
        for (i, e) in enumerate(self.parents):
            s += '+----------+' + '----------+' * width + '\n'
            gi = grid[i].reshape(-1)
            s += f'|{e:^10}|' + '|'.join([f'{e + "("+str(j)+")":^10}' for j in gi])
            s += '|\n'

        for i in range(self.no_states):
            s += '+----------+' + '----------+' * width + '\n'
            state_name = self.name + f'({i})'
            s += f'|{state_name:^10}|' + '|'.join([f'{p:^10.4f}' for p in self.table[i]])
            s += '|\n'

        s += '+----------+' + '----------+' * width + '\n'

        return s

    def probability(self, state, parentstates):
        """
        Returns probability of variable taking on a "state" given "parentstates"
        This method is a simple lookup in the conditional probability table, it does not calculate anything.

        Input:
            state: integer between 0 and no_states
            parentstates: dictionary of {'parent': state}
        Output:
            float with value between 0 and 1
        """
        if not isinstance(state, int):
            raise TypeError(f"Expected state to be of type int; got type {type(state)}.")
        if not isinstance(parentstates, dict):
            raise TypeError(f"Expected parentstates to be of type dict; got type {type(parentstates)}.")
        if state >= self.no_states:
            raise ValueError(f"Recieved state={state}; this variable's last state is {self.no_states - 1}.")
        if state < 0:
            raise ValueError(f"Recieved state={state}; state cannot be negative.")

        table_index = 0
        for variable in self.parents:
            if variable not in parentstates:
                raise ValueError(f"Variable {variable} does not have a defined value in parentstates.")

            var_index = self.parents.index(variable)
            table_index += parentstates[variable] * np.prod(self.no_parent_states[:var_index])

        return self.table[state, int(table_index)]
    
    def __repr__(self):
        return self.name


class BayesianNetwork:
    """
    Class representing a Bayesian network.
    Nodes can be accessed through self.variables['variable_name'].
    Each node is a Variable.

    Edges are stored in a dictionary. A node's children can be accessed by
    self.edges[variable]. Both the key and value in this dictionary is a Variable.
    """
    def __init__(self):
        self.edges = defaultdict(lambda: [])  # All nodes start out with 0 edges
        self.variables = {}                   # Dictionary of "name":TabularDistribution

    def add_variable(self, variable):
        """
        Adds a variable to the network.
        """
        if not isinstance(variable, Variable):
            raise TypeError(f"Expected {Variable}; got {type(variable)}.")
        self.variables[variable.name] = variable

    def add_edge(self, from_variable, to_variable):
        """
        Adds an edge from one variable to another in the network. Both variables must have
        been added to the network before calling this method.
        """
        if from_variable not in self.variables.values():
            raise ValueError("Parent variable is not added to list of variables.")
        if to_variable not in self.variables.values():
            raise ValueError("Child variable is not added to list of variables.")
        self.edges[from_variable].append(to_variable)

    def sorted_nodes(self):
        """
        Returns: List of sorted variable names.
        """
        l = [] # List for storing the topological ordered nodes
        s = [variable[1] for variable in self.variables.items() if len(variable[1].parents) == 0] # Start S with nodes with no parents
        e = copy.copy(self.edges) # Copy edges object, so we don't change the original object

        # For some reason, I had to do copy and the loop below. Deepcopy did not work.
        # (I think deepcopy made new variable objects or something, so that when I check, further down,
        # if the object is still in someones "child" list (or if it has parents Ig), it was always False because it was a different object)

        for var, edges in self.edges.items():
            e[var] = edges.copy() 
            
        while s: # As long as we have some nodes with no parents that are not added to L ..
            v = s.pop(0) #.. pop the first node ..
            l.append(v) # .. and append it to L.

            for variable in self.edges[v]:
                e[v].remove(variable) # Remove the edge between parent V and child variable

                if not variable in itertools.chain(*e.values()): # If the variable is not in any more edges (aka is has no more parents)
                    s.append(variable) # Append it to S.
        
        return l # Return the topological ordered list of nodes. 


class InferenceByEnumeration:
    def __init__(self, bayesian_network):
        self.bayesian_network = bayesian_network
        self.topo_order = bayesian_network.sorted_nodes()

    def _normalize_lst(self, lst):
        """
        Normalizes the list lst.
        Returns: Numpy array with normalized values
        """
        return np.array(list(map(lambda x: x * (1/sum(lst)), lst)))

    def _enumeration_ask(self, X, evidence):
        """
        Returns: Normalized numpy array with a distribution over X, given evidence evidence
        """
        q = [] # Init distribution over X, initially empty.
        var = self.bayesian_network.variables[X] # Get the variable object for variable name X
        for xi in range(var.no_states): # Loop thorough var's possible states (0, 1) for True, False, (0,1,2) for Monty hall
            evidence_tmp = evidence.copy() # copy evidence object
            evidence_tmp[X] = xi # Extend evidence with X's state (overwrite each time the loop loops)
            q.append(self._enumerate_all(self.bayesian_network.sorted_nodes(), evidence_tmp)) # Call enumerate_all and append to q.
        return self._normalize_lst(q) # Return normalized numpy array. 

    def _enumerate_all(self, vars, evidence):
        """
        Helper function for _enumeration_ask.
        Actually calculates the probabilities.
        """

        if len(vars) == 0: # If we are out ouf variables...
            return 1.0 # ... return 1 for the multiplication below.
        
        y = vars.pop(0) # Pop the first variable in the vars list
        if y.name in evidence: # If the variable is in the evidence set, we should just lookup it's probability given it's state, and mulitpy with all other vars probablitity (supplied by a recursive call)
            return y.probability(evidence[y.name], evidence.copy()) * self._enumerate_all(vars.copy(), evidence.copy())
        else: # If it is not in the evidence set, we'll have to calculate the probability, given the variable's legal states (e.g 0 and 1 (True, False))
            summ = 0
            tmp_evidence = evidence.copy()
            for x in range(y.no_states):
                tmp_evidence[y.name] = x
                summ += y.probability(x, evidence.copy()) * self._enumerate_all(vars.copy(), tmp_evidence.copy())
            return summ


    def query(self, var, evidence={}):
        """
        Wrapper around "_enumeration_ask" that returns a
        Tabular variable instead of a vector
        """
        q = self._enumeration_ask(var, evidence).reshape(-1, 1)
        return Variable(var, self.bayesian_network.variables[var].no_states, q)


def problem3c():
    # Define variables
    d1 = Variable('A', 2, [[0.8], [0.2]])
    d2 = Variable('B', 2, [[0.5, 0.2],
                           [0.5, 0.8]],
                  parents=['A'],
                  no_parent_states=[2])
    d3 = Variable('C', 2, [[0.1, 0.3],
                           [0.9, 0.7]],
                  parents=['B'],
                  no_parent_states=[2])
    d4 = Variable('D', 2, [[0.6, 0.8],
                           [0.4, 0.2]],
                  parents=['B'],
                  no_parent_states=[2])

    # Initialize bayesian network
    bn = BayesianNetwork()
    
    # Add variables to the network
    bn.add_variable(d1)
    bn.add_variable(d2)
    bn.add_variable(d3)
    bn.add_variable(d4)

    # Add edges to the network
    bn.add_edge(d1, d2)
    bn.add_edge(d2, d3)
    bn.add_edge(d2, d4)

    # Initialize inference object
    inference = InferenceByEnumeration(bn)

    # Calculate probability distribution of P(C | not D)
    posterior = inference.query('C', {'D': 1})

    print(f"Probability distribution, P({d3.name} | !{d4.name})")
    print(posterior)


def monty_hall():
    # Initialize variables
    chosenByGuest = Variable('ChosenByGuest', 3, [[1/3], [1/3], [1/3]])
    prize = Variable('Prize', 3, [[1/3], [1/3], [1/3]])

    openedByHost = Variable('OpenedByHost', 3, [
        [0, 0, 0, 0, 0.5, 1, 0, 1, 0.5], 
        [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5], 
        [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]
        ], parents=['ChosenByGuest', 'Prize'], no_parent_states=[3, 3])
    
    # Initialize bayesian network
    bn = BayesianNetwork()

    # Add variables to the network
    bn.add_variable(chosenByGuest)
    bn.add_variable(prize)
    bn.add_variable(openedByHost)

    # Add edges to the network
    bn.add_edge(chosenByGuest, openedByHost)
    bn.add_edge(chosenByGuest, prize)

    # Initialize inference object
    inference = InferenceByEnumeration(bn)

    # Calculate probability distribution of P(prize | ChosenByGuest = 1 and OpenedByHost = 2)
    prizeGivenGuestAndHost = inference.query('Prize', {'ChosenByGuest': 0, 'OpenedByHost': 2})

    # Calculate probability of P(Prize | ChosenByGuest = 1) (so that we can see if it is to our advantage to swap doors)
    prizeGivenGuest = inference.query('Prize', {'ChosenByGuest': 0})
    
    print('Probability distribution, P(Prize | ChosenByGuest = 1, OpenedByHost = 3)')
    print(prizeGivenGuestAndHost)

    print('Is it to my advantage to switch doors, given that I have chosen door 1 and host opens 3?')
    print('Yes!' if prizeGivenGuestAndHost.probability(1, {}) > prizeGivenGuest.probability(0, {}) else 'No!')
    


if __name__ == '__main__':
    print('Problem 3c:')
    problem3c()

    print('\nMonty Hall:')
    monty_hall()
