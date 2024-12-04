##50.	Write a program that implements a breadth-first search for a graph structure.
from collections import deque

def bfs(graph,start):

    visited = []
    queue=deque([start])

    while queue:
        node=queue.popleft()

    if node not in visited:
        visited.append(node)
        queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return visited

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

print(bfs(graph,'A'))
