import copy

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]
    
# Heuristic function 
# (Misplaced Titles)
# def heuristic(state):
    # count = 0
    # for i in range(3):
    #     for j in range(3):
    #         if state[i][j] != goal[i][j] and state[i][j] != 0:
    #             count +=1
    # return count

# (manhanttan)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                # calculate where the tile should be
                target_x = (val-1) // 3
                target_y = (val - 1) % 3

                # distance   =   x1 - x2    +   y1 - y2
                distance += abs(i-target_x) + abs(j - target_y)
    return distance

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i , j

# Generate all possible next states.- child
def generate(state):
    x,y = find_blank(state)

    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    children = []     # child states

    for dx,dy in moves:
        # Calculate new blank position
        nx,ny = dx+x, dy+y

        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = copy.deepcopy(state)

            temp[x][y], temp[nx][ny] = temp[nx][ny] ,temp[x][y]

            children.append(temp)
        
    return children

# A* Algorithm
def Astar(start):
    open_list = [(start,0)] # (state,level-path cost g(n))
    visited = []

    while open_list:

        # sort according to : f(n) = g(n)+h(n)- Smallest f(n) comes first.
        open_list.sort(key=lambda x : x[1] + heuristic(x[0]))

        state, level = open_list.pop(0)

        print(f"\nLevel {level} State: ")
        for row in state:
            print(row)

        # Goal state
        if heuristic(state) == 0:
            print("\nGoal state reached!")
            return 
        visited.append(state)

        # Generate children
        for child in generate(state):
            if child not in visited:
                open_list.append((child,level+1))

# Main program
print("Enter initial State:")
start = []

for i in range(3):
    row = list(map(int,input().split()))
    start.append(row)

Astar(start)