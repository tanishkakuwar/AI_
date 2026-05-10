from collections import deque

# create a graph using adj list
graph = {}

# Function to add edge
def add_edge(u,v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    
    # indirected graph
    graph[u].append(v)
    graph[v].append(u)

# BFS 
def bfs(start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("\nBFS Traversal:")

    while queue:
        vertex = queue.popleft()
        print(vertex,end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
            
# DFS (Recursion)
def dfs(vertex,visited):
    visited.add(vertex)

    print(vertex,end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor,visited)

# MAIN PROGRAM
n = int(input("Enter the number of edges: "))

print("Enter edges (u v): ")

for i in range(n):
    u, v = map(int, input().split())
    add_edge(u,v)

start = int(input("Enter the starting edge: "))

# BFS
bfs(start)

# DFS
visited = set()
print("\nDFS Traversal: ")
dfs(start,visited)

# to run this in ubuntu - python3 AI_BFS_DFS.py