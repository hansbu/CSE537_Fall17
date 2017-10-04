#### implementing Dijkstra's algorithm

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:09:25 2017

@author: mac
"""

from queue import PriorityQueue
import heapq as HQ

# define the class Graph to define the vertices and the edges
class Graph_def:
    def __init__(self):
        self.edges = {} #edges are dict type
        self.heuristic = {}
        
    
    def Neighbors(self, vertice):
        temp = self.edges[vertice]      #output a dictionary
        return list(temp.keys())        #cast the keys to the list
    
    def Cost_movement(self, current_node, next_node):
        return self.edges[current_node][next_node]
    def Cost_heuristic(self, current_node, goal):
        return self.heuristic[current_node]
        
graph = Graph_def()
graph.edges = {         #define the weighted edges of the graph 
    'Arad':{'Zerind':75, 'Sibiu':140, 'Timisoara':118},
    'Zerind':{'Arad':75, 'Oradea':71},
    'Timisoara':{'Arad':118, 'Lugoj':111},
    'Oradea':{'Zerind':71, 'Sibiu':151},
    'Sibiu':{'Oradea':151, 'Arad':140, 'Fagaras':99, 'Rimnicu':80},
    'Lugoj':{'Timisoara':111, 'Mehadia':70},
    'Mehadia':{'Lugoj':70, 'Drobeta':75},
    'Drobeta':{'Mehadia':75, 'Craiova':120},
    'Craiova':{'Drobeta':120, 'Rimnicu': 146, 'Pitesti':138},
    'Rimnicu':{'Sibiu':80, 'Craiova':146, 'Pitesti':97},
    'Fagaras':{'Sibiu':99, 'Bucharest':211},
    'Pitesti':{'Rimnicu':97, 'Craiova':138, 'Bucharest':101},
    'Bucharest':{'Pitesti':101, 'Fagaras':211, 'Giurgiu':90, 'Urziceni':85},
    'Giurgiu':{'Bucharest':90},
    'Urziceni':{'Bucharest':85, 'Hirsova':98, 'Vaslui':142},
    'Hirsova':{'Urziceni':98, 'Eforie':86},
    'Eforie':{'Hirsova':86},
    'Vaslui':{'Urziceni':142, 'Iasi':92},
    'Iasi':{'Vaslui':92, 'Neamt':87},
    'Neamt':{'Iasi':87}
}
graph.heuristic = {
    'Arad':366, 'Bucharest':0, 'Craiova':160, 'Drobeta':242, 'Eforie':161, 
    'Fagaras':176, 'Giurgiu':77, 'Hirsova':151, 'Iasi': 226, 'Lugoj':244,
    'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':100, 'Rimnicu':193,
    'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199, 'Zerind':374
}


graph.edges = {         #define the weighted edges of the graph
   'S': {'A':1, 'B':1},
   'B': {'C':2},
   'C': {'G':3},
   'A': {'C':1},
}

graph.heuristic = {
       'S':2, 'A':4, 'B':1, 'C':1, 'G':0
       }

def TracebackFoundPath(parents, start, goal):
    temp = goal
    path_found = [temp]
    while temp != start:
        temp = parents[temp]
        path_found.append(temp)
    path_found.reverse() # reverse the sequence to show from the start to goal
    return path_found
    

def A_star(graph, start, goal = ''):
    parent_list = {}       #mark the node that just generated and keep track the 
                            #parent of each node
    parent_list[start] = None
    
    fringe_list = PriorityQueue()
    fringe_list.put((0, start))
    
    cost_now = {}
    cost_now[start] = 0 
    while(not fringe_list.empty()):     #check if the fringe list is empty or not
        current_node = fringe_list.get()[1]
        if(current_node == goal):   #Stop search when reaching goal
            break
        
        for new_node in graph.Neighbors(current_node):
            new_cost = cost_now[current_node] + graph.Cost_movement(current_node, new_node)
            if new_node not in cost_now or new_cost < cost_now[new_node]:
                Total_cost = new_cost + graph.Cost_heuristic(new_node, goal)
                fringe_list.put((Total_cost, new_node))
                parent_list[new_node] = current_node
                cost_now[new_node] = new_cost
        
    path_found = [goal]    
    path_found.append(parent_list[goal])
    
#   ## trace back the path to find the solution path
    return TracebackFoundPath(parent_list, start, goal)


print('Search A*: ', A_star(graph, 'S', 'G'))

#['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
#
# for place in graph.heuristic.keys():
#     Found_route = Dijkstra_algo(graph, place,'Bucharest')
#     print(Found_route, '\n')
