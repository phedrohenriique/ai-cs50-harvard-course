import csv
import sys
from degrees import neighbors_for_person

class BreadthFirstSearch(): 

    def __init__(self, adjacency_list):
        
        self.adjacency_list = adjacency_list
        
    def path_solution(self, start_node, end_node):

        # treat the id's of the persons

        queue_list = [start_node]
        checked_nodes = [start_node]

        path_queue = [[]]
        path_list = [[]]

        while len(queue_list) > 0 :

            path = path_queue.pop(0)

            node = queue_list.pop(0)
            neighbour_nodes = self.adjacency_list.get(node)

            if neighbour_nodes:

                for neighbour_node in neighbour_nodes:

                    if neighbour_node[1] == end_node:
                        #print('found the path')
                        for path in path_list:
                            for path_tuple in path:
                                if path_tuple[1] == end_node:
                                    print('Solution Path : ',path)
                                    return path

                    if neighbour_node not in checked_nodes:

                        new_path = list(path)
                        new_path.append(neighbour_node)
                        path_list.append(new_path)
                        path_queue.append(new_path)

                        #print('person : ', neighbour_node[1])
                        queue_list.append(neighbour_node[1])
                        checked_nodes.append(neighbour_node[1])
            
        return None        
                        
                        

# $ python degrees.py large
# Loading data...
# Data loaded.
# Name: Emma Watson
# Name: Jennifer Lawrence
# 3 degrees of separation.
# 1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
# 2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
# 3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class