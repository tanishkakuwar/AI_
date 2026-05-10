import heapq

# Heuristic function
def heuristic(board):
    h = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):

            # Same column
            if board[i] == board[j]:
                h += 1

            # Same diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                h += 1

    return h


# Generate neighbors
def neighbors(board):
    n = len(board)
    states = []

    for row in range(n):
        for col in range(n):

            if board[row] != col:
                temp = board[:]
                temp[row] = col
                states.append(temp)

    return states


# A* Algorithm
def Astar(n):

    # Initial state
    start = [0] * n

    # Priority Queue
    pq = []

    #   pq <- h(n), g(n)-path cost from start,curr state
    heapq.heappush(pq, (heuristic(start), 0, start))

    visited = set()

    while pq:

        # smallest f(n) - pop
        f, g, current = heapq.heappop(pq)

        # Convert list to tuple for hashing
        state_tuple = tuple(current)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        # Goal state
        if heuristic(current) == 0:
            return current

        # Generate neighbors
        for neighbor in neighbors(current):

            if tuple(neighbor) not in visited:

                g_new = g + 1
                h_new = heuristic(neighbor)
                f_new = g_new + h_new

                heapq.heappush(pq, (f_new, g_new, neighbor))


# Print Chessboard
def print_board(board):

    n = len(board)

    print("\nSolution Board:\n")

    for i in range(n):

        for j in range(n):

            if board[i] == j:
                print("Q", end=" ")
            else:
                print("_", end=" ")

        print()


# Main Program
n = int(input("Enter value of N: "))

solution = Astar(n)

print("\nSolution State:", solution)

print_board(solution)