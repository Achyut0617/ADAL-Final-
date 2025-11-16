def knapsack_bb(wt, profit, W, n):
    best_profit = [0]           # using list to modify inside recursion
    best_items  = [[]]          # store chosen item indices

    def backtrack(i, curr_w, curr_p, chosen):
        # If weight exceeded → invalid
        if curr_w > W:
            return

        # If all items checked
        if i == n:
            if curr_p > best_profit[0]:
                best_profit[0] = curr_p
                best_items[0] = chosen[:]
            return

        # --- BOUND (simple upper bound) ---
        remaining_profit = sum(profit[i:])     # max possible from here
        if curr_p + remaining_profit < best_profit[0]:
            # prune branch
            return

        # -----------------------------
        # OPTION 1 → INCLUDE item i
        # -----------------------------
        chosen.append(i)
        backtrack(i + 1, curr_w + wt[i], curr_p + profit[i], chosen)
        chosen.pop()

        # -----------------------------
        # OPTION 2 → EXCLUDE item i
        # -----------------------------
        backtrack(i + 1, curr_w, curr_p, chosen)

    # Call recursion from 0th item
    backtrack(0, 0, 0, [])

    return best_profit[0], best_items[0]


# ----------- USER INPUT -----------
n = int(input("Enter number of items: "))
wt = []
profit = []

print("Enter weight and profit of each item:")
for _ in range(n):
    w, p = map(int, input().split())
    wt.append(w)
    profit.append(p)

W = int(input("Enter capacity of box: "))

max_profit, items_selected = knapsack_bb(wt, profit, W, n)

print("\nMaximum Profit =", max_profit)
print("Items selected (0-based index):", items_selected)
