from functools import lru_cache

# ---------------- TSP with path reconstruction ---------------- #

def solve_tsp(graph):
    n = len(graph)
    FULL_MASK = (1 << n) - 1

    @lru_cache(None)
    def tsp(mask, pos):
        if mask == FULL_MASK:
            return graph[pos][0], [0]  # return to start node

        best_cost = float('inf')
        best_path = []

        for nxt in range(n):
            if not (mask & (1 << nxt)):      # if nxt not visited
                cost, path = tsp(mask | (1 << nxt), nxt)
                new_cost = graph[pos][nxt] + cost

                if new_cost < best_cost:
                    best_cost = new_cost
                    best_path = [nxt] + path

        return best_cost, best_path

    cost, path = tsp(1, 0)
    full_route = [0] + path   # starting point + path
    return cost, full_route


# ---------------- USER INPUT ---------------- #

n = int(input("Enter number of attractions: "))
graph = []

print("Enter travel time matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

cost, route = solve_tsp(graph)

print("\nShortest Route:", " -> ".join(map(str, route)))
print("Minimum Travel Time:", cost)
