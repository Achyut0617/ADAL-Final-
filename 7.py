def prims(cost):
    n = len(cost)
    selected = [False] * n
    selected[0] = True   # start from office 1

    edges = []
    total_cost = 0

    for _ in range(n - 1):
        minimum = float('inf')
        x = y = 0         # offices to connect

        # find minimum edge from selected → unselected
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and cost[i][j] != 0:
                        if cost[i][j] < minimum:
                            minimum = cost[i][j]
                            x, y = i, j

        edges.append((x+1, y+1, minimum)) # for human-readable office numbering
        total_cost += minimum
        selected[y] = True

    return edges, total_cost


# ------- USER INPUT --------
n = int(input("Enter number of offices: "))
cost = []

print("Enter adjacency matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

edges, total_cost = prims(cost)

print("\nSelected Connections:")
for u, v, w in edges:
    print(f"{u} -- {v} : {w}")

print("\nMinimum Total Cost =", total_cost)
