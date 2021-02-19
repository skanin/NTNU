# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def minimax(self, depth, state, agent=0):
        # If win or lose, return no action.
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state), None
        
        # If it's Pacman's turn ...
        if agent == 0:
            # Max value is -inf and action is None.
            maxEval, a = float('-inf'), None
            # Loop through all legal moves 
            for action in state.getLegalActions(agent):
                # Get new state after performing move
                new_state = state.generateSuccessor(agent, action)
                # Get max value by calling recursive and reducing depth
                evaluation = self.minimax(depth-1, new_state, 1)[0]
                # If new max value is greater than current max value, update both value and action
                if evaluation > maxEval:
                    maxEval, a = evaluation, action
            # Return max value and best action
            return maxEval, a
        # If agent are ghost
        else:
            # init min value to inf
            minEval, a = float('inf'), None
            # Loop thorugh all legal moves
            for action in state.getLegalActions(agent):
                # Get new state from action
                new_state = state.generateSuccessor(agent, action)
                # If we are at the last ghost ...
                if state.getNumAgents() - 1 == agent:
                    # ... and on last depth ...
                    if depth == 0:
                        # ... get static evaluation of state...
                        evaluation = self.evaluationFunction(new_state)
                    else:
                        # ... if we are not at last depth, it is Pacman's turn again ...
                        evaluation = self.minimax(depth, new_state)[0]
                # If we have more ghosts left
                else:
                    # get new min value from calling recursive
                    evaluation = self.minimax(depth, new_state, agent + 1)[0]
                # Update min value if found lower value
                if evaluation < minEval:
                    minEval, a = evaluation, action
            # Return min value and action
            return minEval, a

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        score, action = self.minimax(self.depth, gameState)
        return action


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def minimax(self, depth, state, alpha, beta, agent=0):
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state), None
        
        if agent == 0:
            maxEval, a = float('-inf'), None
            for action in state.getLegalActions(agent):
                new_state = state.generateSuccessor(agent, action)
                evaluation = self.minimax(depth-1, new_state, alpha, beta, 1)[0]

                if evaluation > maxEval:
                    maxEval, a = evaluation, action
                    # Update alpha to be max of alpha and found max value
                    alpha = max(alpha, maxEval)
                # if max value are better than min's best path earlier, return max value - since min will not choose this path anyway.
                if maxEval > beta:
                    return maxEval, a

            return maxEval, a
        else:
            minEval, a = float('inf'), None
            for action in state.getLegalActions(agent):
                new_state = state.generateSuccessor(agent, action)
                if state.getNumAgents() - 1 == agent:
                    if depth == 0:
                        evaluation = self.evaluationFunction(new_state)
                    else:
                        evaluation = self.minimax(depth, new_state, alpha, beta)[0]
                else:
                    evaluation = self.minimax(depth, new_state, alpha, beta, agent + 1)[0]
                
                if evaluation < minEval:
                    minEval, a = evaluation, action
                    # Update beta to be min of beta and min value found.
                    beta = min(minEval, beta)
                # if min value are better than max's best path earlier, return min value - since max will not choose this path anyway.
                if minEval < alpha:
                    return minEval, a

            return minEval, a

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        val, a = self.minimax(self.depth, gameState, float('-inf'), float('inf'))
        return a

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
