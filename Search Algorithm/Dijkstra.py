#### implementing Dijkstra's algorithm

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:09:25 2017

@author: mac
"""

#import queue
import heapq as HQ

# define the class Graph to define the vertices and the edges
class Graph_def:
    def __init__(self):
        self.edges = {} #edges are dict type
        
    
    def Neighbors(self, vertice):
        temp = self.edges[vertice]      #output a dictionary
        return list(temp.keys())        #cast the keys to the list
    
    def Cost_movement(self, current_node, next_node):
        return self.edges[current_node][next_node]
        
graph = Graph_def()
graph.edges = {         #define the weighted edges of the graph 
    'A': {'B':4, 'D':1},
    'B': {'A':5, 'C':3, 'D':10},
    'C': {'A':1},
    'D': {'E':2},
    'E': {'B':7}
}

   

#The lowest valued entries are retrieved first (the lowest valued entry is the 
#one returned by sorted(list(entries))[0]). A typical pattern for entries is a 
#tuple in the form: (priority_number, data).     

def Dijkstra_algo(graph, start, goal = ''):
    parent_list = {}       #mark the node that just generated and keep track the 
                            #parent of each node
    
    parent_list[start] = None
#    fringe_list = queue.PriorityQueue()
    fringe_list = []
    HQ.heappush(fringe_list, (0, start))
#    fringe_list.put(start, 0)
    
    cost_now = {}
    cost_now[start] = 0 
    
#    while(not fringe_list.empty()):     #check if the fringe list is empty or not
    while(len(fringe_list)):
#        current_node = fringe_list.get()
        current_node = HQ.heappop(fringe_list)[1]
        print(current_node)
        
        if(current_node == goal):   #Stop search when reaching goal
            break
        
        for new_node in graph.Neighbors(current_node):
            new_cost = cost_now[current_node] + graph.Cost_movement(current_node, new_node)
            if new_node not in cost_now or new_cost < cost_now[new_node]:
                HQ.heappush(fringe_list, (new_cost, new_node))
#                fringe_list.put(new_node, new_cost)
                parent_list[new_node] = current_node
                cost_now[new_node] = new_cost
        
    path_found = [goal]    
    path_found.append(parent_list[goal])
    
    print(parent_list)
    
### trace back the path to find the solution path
    temp = goal
    path_found = [temp]
    while temp != start:
        temp = parent_list[temp]
        path_found.append(temp)
#    path.append(start) # optional
    path_found.reverse() # optional
    
    return path_found


#print('Search Dijkstra: ')             
Found_route = Dijkstra_algo(graph,'B','E')
print(Found_route)
