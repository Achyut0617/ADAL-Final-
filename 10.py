def tsp_dp(dist, n):
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]

    dp[1][0] = 0  # start at city 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue  # u not visited

            for v in range(n):
                if mask & (1 << v):  
                    continue  # v already visited

                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(
                    dp[new_mask][v],
                    dp[mask][u] + dist[u][v]
                )

    # return to start city (0)
    full_mask = (1 << n) - 1
    ans = min(dp[full_mask][i] + dist[i][0] for i in range(n))

    return ans


# -------- USER INPUT --------
n = int(input("Enter number of attractions: "))
print("Enter travel time matrix:")

dist = []
for _ in range(n):
    row = list(map(int, input().split()))
    dist.append(row)

result = tsp_dp(dist, n)
print("\nMinimum Travel Time (Best Circular Route):", result)
