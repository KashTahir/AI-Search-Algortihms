import sys
import csv


def graph_search(start_state):
    """
    You are free to implement this however you like but you will most likely need to input the graph data structure G, the heuristic function h, the start state s, the goal state t, and the search strategy X  
    """

    # ---- YOUR CODE HERE ----

    level = 0
    initial_path = [start_state]
    inital_g = 0
    start_node = Node(start_state, level, initial_path, inital_g)

    frontier_nodes = [start_node]

    # frontier sorting for each
    # BFS - regular
    # DFS - reverse
    # Greedy - based on heuristic of that node (h)
    # A* - based one heuristic + cost of that node (h + g)


    return None

class Node:
    def __init__(self, value, level, path, g_cost):
        self.value = value
        self.level = level
        self.path = path
        self.g_cost = g_cost

# ---- INCLUDE ANY OTHER CODE THAT YOU NEED HERE ----


if __name__ == "__main__":

    # get parameters from command line. We need -1 for our vertex numbers since our indexing starts at 0 in python
    start_state = int(sys.argv[1]) - 1
    goal_state = int(sys.argv[2]) - 1
    search_strategy = sys.argv[3]
    graph_csv = sys.argv[4]
    heuristic_csv = sys.argv[5]

    # get the graph
    graph = []
    with open(graph_csv, "r", encoding='utf-8-sig') as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            row_as_ints = [int(val) if val != '' else None for val in row]
            graph.append(row_as_ints)

    # get the heuristic matrix
    heuristic = []
    with open(heuristic_csv, "r", encoding='utf-8-sig') as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            heuristic_row = [float(val) if val != '' else None for val in row]
            heuristic.append(heuristic_row)

    # once we have the goal we can create the heuristic function using the matrix
    heuristic_func = lambda n: heuristic[n][goal_state]        
            
    # find and print the path. The vertices are numbered as they appear in the original graph. Add whatever inputs you need to your graph search function
    path = graph_search()
    if path is not None:
        path = str([state + 1 for state in path])
    print(path)


