# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:16:49 2021

@author: Dian
"""

graph = {
    'Anggrek' : ['Mawar','Kamboja'],
    'Mawar' : ['Melati', 'Raflesia'],
    'Kamboja' : ['Teratai'],
    'Melati' : [],
    'Raflesia' : ['Teratai'],
    'Teratai' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'Anggrek')
