def bellman_ford(n, edges, source):
    dist = [float('inf')] * n
    dist[source] = 0

    # Relax edges (n-1) times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Negative cycle detected!")
            return None

    return dist


# USER INPUT
n = int(input("Enter number of city junctions: "))
e = int(input("Enter number of roads: "))

edges = []
print("Enter each road as: from to time")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter starting junction: "))

dist = bellman_ford(n, edges, source)

print("\nShortest travel times from source:")
for i in range(n):
    print(f"To {i}: {dist[i]}")
