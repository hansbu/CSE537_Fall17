#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:09:25 2017

@author: mac
"""

import queue

# define the class Graph to define the vertices and the edges
class Graph_def:
    def __init__(self):
        self.edges = {} #edges are dict type
        self.costs = {}
        
    
    def Neighbors(self, vertice):
        return self.edges[vertice]
    

graph = Graph_def()
graph.edges = {         #define the edges of the graph
    'S': ['A', 'B', 'D']
    'A': ['C'],
    'B': ['D'],
    'C': ['A'],
    'D': ['A', 'C', 'G'],
    'G': ['C', 'D']
}
        

def BFS(graph, start, goal = ''):
    parent_list = {}       #mark the node that just generated and keep track the 
                            #parent of each node
    closed_list = []    #to contain nodes that are explored
                        
    parent_list[start] = None
    print('type of parent_list: ', type(parent_list))
    
    fringe_list = queue.Queue() #BFS uses FIFO
    fringe_list.put(start)
    
    while(not fringe_list.empty()):     #check if the fringe list is empty or not
        current_node = fringe_list.get()
        closed_list.append(current_node)   #current_node is explored
        
        if(current_node == goal):   #Stop search when reaching goal
            break
        
        for new_node in graph.Neighbors(current_node):
            if new_node not in closed_list:
                fringe_list.put(new_node)
                parent_list[new_node] = current_node
        
    path_found = [goal]    
    path_found.append(parent_list[goal])
    
### trace back the path to find the solution path
    root = ''
    while (root != start):
        for key, value in parent_list.items():
            if value not in path_found:
                len_path_found = len(path_found)
                last_node = path_found[len_path_found-1]
                root = parent_list[last_node]
                path_found.append(root)
                
                
    path_found.reverse()    
    return path_found
    
def DFS(graph, start, goal = ''):
    visisted_list = {}   #mark the node that just visisted
    fringe_list = queue.LifoQueue()  #BFS uses LIFO
    fringe_list.put(start)
    
    while(not fringe_list.empty()):     #check if the fringe list is empty or not
        current_node = fringe_list.get()
        print(current_node)
        visisted_list[current_node] = True
        
        if(current_node == goal):   #Stop search when reaching goal
            break
        
        for new_node in graph.Neighbors(current_node):
            if new_node not in visisted_list:
                fringe_list.put(new_node)
                visisted_list[new_node] = True 




# print('Search BFS: ')
# BFS_route = BFS(graph,'A','E')
# print(BFS_route)



print('Search DFS: ')
DFS_route = DFS(graph,'A')
print(DFS_route)
    
