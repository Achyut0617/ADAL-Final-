class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parent[pa] = pb
            return True
        return False


def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    dsu = DSU(n)

    mst_cost = 0
    mst_edges = []

    for u, v, cost in edges:
        if dsu.union(u, v):
            mst_cost += cost
            mst_edges.append((u, v, cost))

    return mst_cost, mst_edges


# ------ USER INPUT ------
n = int(input("Enter number of zones: "))
m = int(input("Enter number of cable routes: "))

edges = []
print("Enter cables as: zone1 zone2 cost")
for _ in range(m):
    u, v, c = map(int, input().split())
    edges.append((u-1, v-1, c))

cost, selected = kruskal(edges, n)

print("\nSelected Cables:")
for u, v, c in selected:
    print(f"{u+1} -- {v+1} (Cost = {c})")

print(f"\nMinimum Installation Cost = {cost}")
