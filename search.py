# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def graph_search(problem, fringe):
    fringe.push([(problem.getStartState(), "", 1.0)])
    visited = []
    while not fringe.isEmpty():
        node_details = fringe.pop()
        node         = node_details[-1][0]
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return [path[1] for path in node_details[1:]]
            else:
                successors = [nodes for nodes in problem.getSuccessors(node) if nodes[0] not in visited]
                if successors:
                    for successor in successors:
                        total_path = node_details[:]
                        total_path.append(successor)
                        fringe.push(total_path)
    return []

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    fringe     = util.Stack()
    return graph_search(problem, fringe)

def breadthFirstSearch(problem):
    fringe        = util.Queue()
    return graph_search(problem, fringe)

def uniformCostSearch(problem):
    cost_function = lambda priority: problem.getCostOfActions([x[1] for x in priority[1:]])
    fringe        = util.PriorityQueueWithFunction(cost_function)
    return graph_search(problem, fringe)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
     cost_function = lambda total_path: problem.getCostOfActions([x[1] for x in total_path[1:]]) + heuristic(total_path[-1][0], problem)
     fringe        = util.PriorityQueueWithFunction(cost_function)
     return graph_search(problem, fringe)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
