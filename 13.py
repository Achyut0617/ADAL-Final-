def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()


def is_safe(x, y, maze, visited, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]


def solve_maze(maze, x, y, n, path, paths, visited):
    # If destination reached
    if x == n - 1 and y == n - 1:
        paths.append(path)

        # Print the visited matrix for this path
        print("\nPath Found:", path)
        print("Visited Matrix Representation:")
        print_board(visited)

        return

    visited[x][y] = 1   # mark current cell

    # Move Down
    if is_safe(x + 1, y, maze, visited, n):
        solve_maze(maze, x + 1, y, n, path + "D", paths, visited)

    # Move Right
    if is_safe(x, y + 1, maze, visited, n):
        solve_maze(maze, x, y + 1, n, path + "R", paths, visited)

    # Move Up
    if is_safe(x - 1, y, maze, visited, n):
        solve_maze(maze, x - 1, y, n, path + "U", paths, visited)

    # Move Left
    if is_safe(x, y - 1, maze, visited, n):
        solve_maze(maze, x, y - 1, n, path + "L", paths, visited)

    visited[x][y] = 0   # BACKTRACK


# ---- MAIN ----
n = int(input("Enter maze size (n): "))

maze = []
print("\nEnter maze row by row (0 = blocked, 1 = open):")
for _ in range(n):
    maze.append(list(map(int, input().split())))

print("\nMaze Matrix:")
print_board(maze)

visited = [[0]*n for _ in range(n)]
paths = []

if maze[0][0] == 1:
    solve_maze(maze, 0, 0, n, "", paths, visited)

print("\nAll Possible Paths:")
if paths:
    for p in paths:
        print(p)
else:
    print("No path exists.")
