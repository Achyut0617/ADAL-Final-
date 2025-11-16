def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c

            if graph_coloring_util(graph, m, color, v + 1):
                return True

            color[v] = 0  # backtrack
    return False


def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    if not graph_coloring_util(graph, m, color, 0):
        print("No solution exists with", m, "colors.")
        return

    print("\nGraph Coloring Solution:")
    for i in range(n):
        print(f"Vertex {i} → Color {color[i]}")


# ---- USER INPUT ----
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors allowed: "))

graph_coloring(graph, m)
