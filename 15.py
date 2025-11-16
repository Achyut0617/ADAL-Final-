import math

def tsp_branch_and_bound(graph):
    n = len(graph)
    best_cost = math.inf
    best_path = []

    def solve(path, visited, cost_so_far):
        nonlocal best_cost, best_path

        # If all cities visited, return to start
        if len(path) == n:
            final_cost = cost_so_far + graph[path[-1]][path[0]]
            if final_cost < best_cost:
                best_cost = final_cost
                best_path = path[:] + [path[0]]
            return

        # Branch & Bound: prune paths already worse
        if cost_so_far >= best_cost:
            return

        last = path[-1]

        # Try next unvisited city
        for nxt in range(n):
            if not visited[nxt]:
                visited[nxt] = True
                solve(path + [nxt], visited, cost_so_far + graph[last][nxt])
                visited[nxt] = False

    visited = [False] * n
    visited[0] = True
    solve([0], visited, 0)

    return best_cost, best_path


# ------------ USER INPUT --------------- #

n = int(input("Enter number of attractions: "))
graph = []

print("Enter travel time matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

cost, route = tsp_branch_and_bound(graph)

print("\nMost Efficient Circular Route:")
print(" -> ".join(map(str, route)))

print("Minimum Travel Time:", cost)
