import heapq

def a_star(graph, start, goal, heuristic):
    pq = [(0, start)]    # (f(n), node)
    g_cost = {start: 0}
    parent = {start: None}

    while pq:
        f, node = heapq.heappop(pq)

        if node == goal:
            # reconstruct path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], g_cost[goal]

        for neigh, cost in graph[node]:
            new_g = g_cost[node] + cost

            if neigh not in g_cost or new_g < g_cost[neigh]:
                g_cost[neigh] = new_g
                f = new_g + heuristic[neigh]
                parent[neigh] = node
                heapq.heappush(pq, (f, neigh))

    return None, float('inf')


# ---- USER INPUT ----
n = int(input("Enter number of nodes: "))
graph = {i: [] for i in range(n)}

print("Enter edges: node1 node2 cost (enter -1 to stop):")
while True:
    u = int(input("u = "))
    if u == -1:
        break
    v = int(input("v = "))
    w = int(input("cost = "))
    graph[u].append((v, w))
    graph[v].append((u, w))   # undirected graph

heuristic = {}
print("Enter heuristic (estimated cost to goal) for each node:")
for i in range(n):
    heuristic[i] = int(input(f"h[{i}] = "))

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

path, cost = a_star(graph, start, goal, heuristic)

print("\nBest Path Found:", path)
print("Estimated Communication Cost:", cost)
