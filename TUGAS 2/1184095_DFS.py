# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:18:50 2021

@author: Dian
"""

# Using a Python dictionary to act as an adjacency list
graph = {
    'Anggrek' : ['Mawar','Kamboja'],
    'Mawar' : ['Melati', 'Raflesia'],
    'Kamboja' : ['Teratai'],
    'Melati' : [],
    'Raflesia' : ['Teratai'],
    'Teratai' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'Anggrek')
