print("GRAPH COLORING PROBLEM")

# Check if color can be assigned
# c - spcific color
# m - total color
# color - array
# v - curr vertex

def is_safe(v, graph, color, c, n):

    for i in range(n):
#  If there is an edge (graph[v][i] == 1) AND the neighbor has color 'c
        if graph[v][i] == 1 and color[i] == c:
            return False

    return True


# Backtracking function
def solve(v, graph, m, color, n):

    # All vertices colored
    if v == n:
        return True

    # Try all colors
    for c in range(1, m + 1):

        if is_safe(v, graph, color, c, n):
            color[v] = c

            # Recursive call
            if solve(v + 1, graph, m, color, n):
                return True

            # Backtrack
            color[v] = 0

    return False


# -------- MAIN --------

n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

# Instead of: row = list(map(int, input().split()))
# Use this:
for i in range(n):
    line = input()          # Take the input string (e.g., "0 1 0")
    parts = line.split()    # Split the string into a list of strings: ["0", "1", "0"]
    row = []                # Create an empty list for the current row
    
    for x in parts:
        row.append(int(x))  # Convert each string to an integer and add to row
        
    graph.append(row)       # Add the completed row to the graph

# for i in range(n):
#     row = list(map(int, input().split()))
#     graph.append(row)

m = int(input("Enter number of colors: "))

color = [0] * n

if solve(0, graph, m, color, n):

    print("\nColor Assigned to Vertices:")

    for i in range(n):

        print("Vertex", i, "-> Color", color[i])

else:
    print("Solution does not exist")