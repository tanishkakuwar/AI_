import copy
import heapq

# Selection sort
def selection_sort():
    arr = list(map(int,input("Enter elements: ").split()))
    n = len(arr)

    for i in range(n):
        min_index = i # Fixed: min_index should start at i, not 1
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i] , arr[min_index] = arr[min_index], arr[i]
    print("Sorted Array:",arr)

# MST - Prim's algorithm
def prims():
    INF = 999999999
    n = int(input("Enter number of vertices: "))

    graph = []
    print("Enter adjacency matrix:")
    for i in range(n):
        row = list(map(int,input().split()))
        graph.append(row)

    # Corrected: Initialize selected list properly
    selected = [False] * n
    selected[0] = True
    edge_count = 0

    print("\nEdges in MST:")

    while edge_count < n - 1:
        minimum = INF
        x = 0 # Source vertex
        y = 0 # Destination vertex

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    # Edge must connect a selected vertex to an unselected one
                    # and the weight must be greater than 0 (graph[i][j] > 0)
                    if (not selected[j]) and graph[i][j] > 0:  
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        # This ensures we only pick the absolute minimum after checking all possibilities
        if minimum != INF:
            print(x, "-", y, ":", graph[x][y])
            selected[y] = True
            edge_count += 1
        else:
            print("Graph is not connected.")
            break
        
# Kruskal’s Minimum Spanning Tree Algorithm
def Kruskal():
    edges = []
    n_edges = int(input("Enter number of edges: ")) 

    for i in range(n_edges):
        u = input("Enter u: ")
        v = input("Enter v: ")
        w = int(input("Enter weight: ")) # Fixed: Weights must be integers for sorting

        edges.append((w,u,v))

    edges.sort()
    parent = {} #Changed to dictionary to support string nodes

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        parent[find(x)] = find(y) # Corrected indexing find(x)

    for edge in edges:
        w,u,v = edge
        if u not in parent: parent[u] = u
        if v not in parent: parent[v] = v

    print("\nEdges in MST: ")
    for edge in edges:
        w,u,v = edge
        if find(u) != find(v):
            print(u,"-",v,":",w)
            union(u,v)

# Dijkstra’s Shortest Path Algorithm 
def Single_src():
    print("Single source shortest path")
    graph = {}
    n = int(input("Enter number of edges: "))

    for i in range(n):
        u = input("Enter u: ")
        v = input("Enter v: ")
        w = int(input("Enter w: "))

        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []

        graph[u].append((v,w))
        graph[v].append((u,w))

    source = input("Enter source vertex: ")
    
    distance = {}

    for node in graph:
        distance[node] = float('inf')

    distance[source] = 0
    pq = [(0,source)]

    while pq:
        dist,node = heapq.heappop(pq)
        
        if dist > distance[node]: continue # Optimization

        for neighbor,weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq,(new_dist,neighbor))

    print("\nShortest Distance from",source)
    for node in distance:
        print(source,"to",node,"=",distance[node])

# Job Scheduling Problem
def job_sch():
    jobs = []
    n = int(input("Enter number of jobs: "))

    for i in range(n):
        name = input("Enter job names: ")
        deadline = int(input("Enter Deadlines: "))
        profit = int(input("Enter the Profit: "))
        jobs.append((name,deadline,profit))

    jobs.sort(key=lambda x : x[2],reverse =True)

    result = []
    time = 0
    total_profit = 0

    for job in jobs:
        if time < job[1]:
            result.append(job[0]) 
            total_profit += job[2]
            time += 1

    print("\nSelected Jobs:",result)
    print("\nTotal Profit:",total_profit)

# main program
run = True
while run:
    print("\n1 - selection_sort")
    print("2 - prims") 
    print("3 - Kruskal")
    print("4 - Single_src")
    print("5 - Job Scheduling")
    print("6 - Quit")
    m = int(input("Choose from (1-6): "))

    if m == 1:
        selection_sort()
    elif m == 2:
        prims()
    elif m == 3:
        Kruskal()
    elif m == 4:
        Singel_src()
    elif m == 5:
        job_sch()
    elif m == 6:
        run = False
    else:
        print("Enter the valid option!")