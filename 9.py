def knapsack(wt, val, capacity, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if wt[i-1] <= w:
                # choose max of taking or not taking
                dp[i][w] = max(
                    val[i-1] + dp[i-1][w - wt[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    # Backtrack selected items
    selected = []
    w = capacity
    i = n

    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:  # item i was taken
            selected.append(i)
            w -= wt[i-1]
        i -= 1

    return dp[n][capacity], selected[::-1]


# ---- USER INPUT ----
n = int(input("Enter number of items: "))
wt = []
val = []

print("Enter weight and value of each item:")
for _ in range(n):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)

capacity = int(input("Enter drone weight capacity: "))

max_value, selected_items = knapsack(wt, val, capacity, n)

print("\nSelected items:")
for item in selected_items:
    print(f"Item {item}")

print("\nMaximum total value =", max_value)
