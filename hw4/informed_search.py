# ----------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 4 - Implement astar and some heuristics
#
# Author(s): Michael Wong, Joseph Nguyen
#
# ----------------------------------------------------------------------
"""
A* Algorithm and heuristics implementation
Your task for homework 4 is to implement:
1.  astar
2.  single_heuristic
3.  better_heuristic
4.  gen_heuristic
"""
import data_structures


def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    # Enter your code here and remove the pass statement below
    closed = set()  # keep track of our explored states
    fringe = data_structures.PriorityQueue()  # for astar, the fringe is a priority queue
    state = problem.start_state()
    root = data_structures.Node(state)
    fringe.push(root, root.cumulative_cost + heuristic(state, problem))  # priority cost + heuristic
    while True:
        if fringe.empty():
            return None  # Failure -  no solution was found
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node.actions()
        if node.state not in closed:  # we are implementing graph search
            closed.add(node.state)
            for child_state, action, action_cost in problem.expand(node.state):
                child_node = data_structures.Node(child_state, node, action)
                child_node.cumulative_cost = node.cumulative_cost + action_cost  # update cost of each child
                fringe.push(child_node, child_node.cumulative_cost + heuristic(child_state, problem))


def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*.
    Running A* with this null heuristic, gives us uniform cost search
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def manhattan(pos1, pos2):
    """
    :param pos1: current position in terms of (x, y)
    :param pos2: objective position in terms of (x, y)
    :return: the manhattan distance between two positions
    """
    row1, col1 = pos1
    row2, col2 = pos2

    return abs(row1 - row2) + abs(col1 - col2)


def single_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: the manhattan distance from sammy to the goal as a heuristic
    """
    # Enter your code here and remove the pass statement below
    sammy, medal = state
    heuristic = 0
    if len(medal) == 0:
        return heuristic
    else:
        heuristic = manhattan(sammy, medal[0])

    return heuristic


def better_heuristic(state, problem):
    """
    A better heuristic to be used when we know for sure that there is only one medal in the quest.
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    sammy, medal = state
    if len(medal) == 0:
        return 0
    (r1, c1) = sammy
    if (23 < c1 < 26 and 1 <= r1 <= 9):
        return 0
    else:
        return 100


def gen_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    # Enter your code here and remove the pass statement below
    pass