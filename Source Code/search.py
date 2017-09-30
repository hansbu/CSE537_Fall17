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

from copy import deepcopy
import  copy

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

        This methood returns the ttal cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
    # return ['West', 'West', 'East', 'East']


def TracebackFoundPath(parents, start, goal):    #Trace back the list of action taken
    path_found = []                              #list of action
    temp = goal                                  #traceback from the goal to the start node
    while temp != start:
        temp, action, cost = parents[temp]      #unpack tuple of value parents[temp]
        path_found.append(action)               #add action to the list

    path_found.reverse()  # reverse the sequence to show from the start to goal
    return path_found

from memory_profiler import  profile
# @profile

#this DFS used Closed list
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # # util.raiseNotDefined()
    import time
    import util

    t_start = time.time()
    closed_list = []  # mark the node that just explored
    start = problem.getStartState()     # save the start node of the problem
    goal = ()                       # initialize the goal node, to save for the traceback path
    fringe_list = util.Stack()          # fringe list that contains all visited but not explored node
    fringe_list.push(start)             # push start node to the fringe list

    parent_list = {}       # contains the parent node of each node and action, cost from that node to each node
    parent_list[start] = None

    while (not fringe_list.isEmpty()):      # check if the fringe list is empty or not
        current_node = fringe_list.pop()    # get the next node in the fringe list
        closed_list.append(current_node)    # mark current_node as explored

        if (problem.isGoalState(current_node)):  # Stop search when reaching goal
            goal = current_node                  # save the goal node for the traceback task
            break

        for new_node, action, cost in problem.getSuccessors(current_node):  # unpack tuple of successor to get next_nodes
            if (new_node not in closed_list):         # only query nodes that are not explored, meaning NOT in closed list
                fringe_list.push(new_node)          # push node to the fringe list
                parent_list[new_node] = (current_node, action, cost)     # save the parent of the new node, including action and cost

    if len(goal) == 0:
        print "\n\nSearching Failed. Cannot find solution! \n\n"
        return -1

    print "Processing Time: ", time.time() - t_start            # calculate processing time of the algorithm
    print "number of nodes in closed_list: ", len(closed_list) - 1  # count number of nodes in that are explored
    return TracebackFoundPath(parent_list, start, goal)





#this DFS used VISITED list
def depthFirstSearch_visited(problem):

    #"*** YOUR CODE HERE ***"
    # # util.raiseNotDefined()
    import  util
    import time
    import Queue  # using data structure like Stack, Queue

    t_start = time.time()
    visited_list = []  # mark the node that just explored
    start = problem.getStartState()     # save the start node of the problem
    goal = ()                       # initialize the goal node, to save for the traceback path
    fringe_list = util.Stack()          # fringe list that contains all visited but not explored node
    fringe_list.push(start)             # push start node to the fringe list

    parent_list = {}       # contains the parent node of each node and action, cost from that node to each node
    parent_list[start] = None

    visited_list.append(start)  # mark current_node as explored

    while (not fringe_list.isEmpty()):      # check if the fringe list is empty or not
        current_node = fringe_list.pop()    # get the next node in the fringe list


        if (problem.isGoalState(current_node)):  # Stop search when reaching goal
            goal = current_node                  # save the goal node for the traceback task
            break

        for new_node, action, cost in problem.getSuccessors(current_node):  # unpack tuple of successor to get next_nodes
            if new_node not in visited_list:         # only query nodes that are not explored, meaning NOT in closed list
                fringe_list.push(new_node)          # push node to the fringe list
                parent_list[new_node] = (current_node, action, cost)     # save the parent of the new node, including action and cost
                visited_list.append(new_node)  # mark current_node as explored

    if len(goal) == 0:
        print "\n\nSearching Failed. Cannot find solution! \n\n"
        return -1

    print "Processing Time: ", time.time() - t_start            # calculate processing time of the algorithm
    print "number of nodes in closed_list: ", len(visited_list) - 1  # count number of nodes in that are explored
    print "number of nodes in closed_list: ", len(set(visited_list)) - 1  # count number of nodes in that are explored
    return TracebackFoundPath(parent_list, start, goal)
#


# @profile

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    import time
    t_start = time.time()

    import Queue        # using data structure like Stack, Queue
    closed_list = []  # mark the node that just explored
    start = problem.getStartState()     # save the start node of the problem
    goal = ()                       # initialize the goal node, to save for the traceback path

    fringe_list = Queue.Queue()  # fringe list that contains all visited but not explored node
    fringe_list.put(start)             # push start node to the fringe list


    parent_list = {}       # contains the parent node of each node and action, cost from that node to each node
    parent_list[start] = None

    while (not fringe_list.empty()):      # check if the fringe list is empty or not
        current_node = fringe_list.get()    # get the next node in the fringe list
        # if current_node not in closed_list:
        closed_list.append(current_node)    # mark current_node as explored

        if (problem.isGoalState(current_node)):  # Stop search when reaching goal
            goal = current_node                  # save the goal node for the traceback task
            print "Goal Found!"
            break

        for new_node, action, cost in problem.getSuccessors(current_node):  # unpack tuple of successor to get next_nodes
            if (new_node not in closed_list) and (new_node not in fringe_list.queue):         # only query nodes that are not explored, meaning NOT in closed list
                fringe_list.put(new_node)      # push node to the fringe list
                parent_list[new_node] = (current_node, action, cost)     # save the parent of the new node, including action and cost

    if len(goal) == 0:
        print "\n\nSearching Failed. Cannot find solution! \n\n"
        return -1

    print "Processing Time: ", time.time() - t_start            # calculate processing time of the algorithm
    print "number of nodes in closed_list: ", len(closed_list) - 1  # count number of nodes in that are explored
    # print "number of unique nodes in closed_list: ", len(set(closed_list)) - 1
    return TracebackFoundPath(parent_list, start, goal)

# @profile
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    import time
    import util                 # to use data structure such as Stack, Queue
    t_start = time.time()
    fringe_data = set()            # contain same element as Fringe queue but it is a set to check if a node in the Fringe

    closed_list = []            # mark the node that just explored
    start = problem.getStartState()     # save the start node of the problem
    goal = ()                           # initialize the goal node, to save for the traceback path
    fringe_list = util.PriorityQueue()          # fringe list that contains all visited but not explored node
    fringe_list.push(start, 0)                  # push start node to the fringe list
    fringe_data.add(start)

    parent_list = {}  # mark the node that just generated and keep track the parent of each node

    cost_now = {}           # save the cost from the start to each node g(n)
    cost_now[start] = 0     # this is trivial g(start) = 0
    while (not fringe_list.isEmpty()):  # check if the fringe list is empty or not
        current_node = fringe_list.pop()    # pop the lowest priority element from the fringe list
        fringe_data.remove(current_node)
        closed_list.append(current_node)  # mark current_node as explored

        if (problem.isGoalState(current_node)):  # Stop search when reaching goal
            goal = current_node
            break
        # algorithm page 84, Russell, S., and Norvig, P. 2003. Artificial Intelligence, A Modern Approach. Prentice Hall
        for new_node, action, cost in problem.getSuccessors(current_node):  # unpack tuple of successor to get next_nodes
            new_cost = cost_now[current_node] + cost                        # g(n') = g(n) + c(n, n')
            checkNodeInFringe = new_node in fringe_data     # True if the node is in Fringe already
            if (new_node not in closed_list) and not checkNodeInFringe:
                fringe_list.push(new_node, new_cost)                      # update the Priority Queue with new node & new cost
                fringe_data.add(new_node)
                parent_list[new_node] = (current_node, action, cost)  # update the parent of the new node
                cost_now[new_node] = new_cost
            elif checkNodeInFringe and cost_now[new_node] > new_cost:                              # update the cost g(n)
                fringe_list.update(new_node, new_cost)
                parent_list[new_node] = (current_node, action, cost)  # update the parent of the new node
                cost_now[new_node] = new_cost

    if len(goal) == 0:
        print "\n\nSearching Failed. Cannot find solution! \n\n"
        return -1

    #   ## trace back the path to find the solution path
    print "Processing Time: ", time.time() - t_start            # calculate processing time of the algorithm
    print "number of nodes in closed_list: ", len(closed_list) - 1  # count number of nodes in that are explored
    return TracebackFoundPath(parent_list, start, goal)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


# @profile
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    import time
    t_start = time.time()

    import util  # to use data structure such as Stack, Queue
    closed_list = []  # mark the node that just explored
    start = problem.getStartState()  # save the start node of the problem
    goal = ()  # initialize the goal node, to save for the traceback path
    fringe_list = util.PriorityQueue()  # fringe list that contains all visited but not explored node
    fringe_list.push(start, 0)  # push start node to the fringe list
    fringe_data = set()
    fringe_data.add(start)
    parent_list = {}  # mark the node that just generated and keep track the
    # parent of each node

    cost_now = {}  # save the cost from the start to each node g(n)
    cost_now[start] = 0
    while (not fringe_list.isEmpty()):  # check if the fringe list is empty or not
        current_node = fringe_list.pop()
        closed_list.append(current_node)  # mark current_node as explored
        fringe_data.remove(current_node)

        if (problem.isGoalState(current_node)):  # Stop search when reaching goal
            goal = current_node
            break


        for new_node, action, cost in problem.getSuccessors(current_node):  # unpack tuple of successor to get next_nodes
            new_cost = cost_now[current_node] + cost                        # g(n') = g(n) + c(n, n')
            checkNodeInFringe = new_node in fringe_data     # True if the node is in Fringe already
            if (new_node not in closed_list) and not checkNodeInFringe:
                Total_cost = new_cost + heuristic(new_node, problem)  # f(n) = g(n) + h(n)
                fringe_list.push(new_node, Total_cost)                      # update the Priority Queue with new node & new cost
                fringe_data.add(new_node)
                parent_list[new_node] = (current_node, action, cost)  # update the parent of the new node
                cost_now[new_node] = new_cost
            elif checkNodeInFringe and cost_now[new_node] > new_cost:
                Total_cost = new_cost + heuristic(new_node, problem)  # f(n) = g(n) + h(n)# update the cost g(n)
                fringe_list.update(new_node, Total_cost)  # update the Priority Queue
                parent_list[new_node] = (current_node, action, cost)  # update the parent of the new node
                cost_now[new_node] = new_cost
    if len(goal) == 0:
        print "\n\nSearching Failed. Cannot find solution! \n\n"
        return -1

    print "Processing Time: ", time.time() - t_start
    # ## trace back the path to find the solution path
    # print "start node: ", start
    # print "goal node: ", goal
    return TracebackFoundPath(parent_list, start, goal)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
