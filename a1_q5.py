import sys
import csv

def graph_search(start_state, goal_state, graph, search_strategy, heuristic_func):
    """
    You are free to implement this however you like but you will most likely need to input the graph data structure G, the heuristic function h, the start state s, the goal state t, and the search strategy X  
    """

    depth = 0
    initial_path = [start_state]
    initial_g = 0
    start_node = Node(start_state, depth, initial_path, initial_g)

    frontier_nodes = [start_node]
    visited_nodes = set()

    while frontier_nodes:

        if search_strategy == "B":
            frontier_nodes.sort(key=lambda n:n.depth)
        # Greedy sorting based on heuristic of that node (h)
        elif search_strategy == "G":
            frontier_nodes.sort(key=lambda n:heuristic_func(n.value))
        # A* sorting based one heuristic + cost of that node (h + g)
        elif search_strategy == "A":
            frontier_nodes.sort(key=lambda n:heuristic_func(n.value) + n.g_cost)
    
        
        if search_strategy == "D":
            # get the node that was last added - LIFO
            curr_node = frontier_nodes.pop()
        else:
            # get the node that was first added - FIFO
            curr_node = frontier_nodes.pop(0)
        curr_state = curr_node.value

        # visit the node
        if curr_state in visited_nodes:
            continue
        else:
            visited_nodes.add(curr_state)

        if curr_state == goal_state:
            return curr_node.path
        
        curr_neighbours = graph[curr_state]
        for next_node_value, next_node_cost in enumerate(curr_neighbours):
            if (next_node_cost is not None) and (next_node_value not in visited_nodes):
                
                new_depth = curr_node.depth + 1
                new_path = curr_node.path + [next_node_value]
                new_cost = curr_node.g_cost + next_node_cost
                next_node = Node(next_node_value, new_depth, new_path, new_cost)

                frontier_nodes.append(next_node)
            else:
                continue
    
    return None

class Node:
    def __init__(self, value, depth, path, g_cost):
        self.value = value
        self.depth = depth
        self.path = path
        self.g_cost = g_cost

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
    path = graph_search(start_state, goal_state, graph, search_strategy, heuristic_func)
    if path is not None:
        path = str([state + 1 for state in path])
    print(path)


