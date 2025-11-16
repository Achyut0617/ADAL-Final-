
def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
    items = []

    # Store (profit/weight ratio, weight, profit, index)
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i], i + 1))

    # Sort by ratio descending
    items.sort(reverse=True)

    total_profit = 0
    item_selection = []

    for ratio, weight, profit, item_no in items:
        if capacity == 0:
            break

        if weight <= capacity:
            # take full item
            total_profit += profit
            capacity -= weight
            item_selection.append((item_no, 1.0))   # 100% taken
        else:
            # take fractional part
            frac = capacity / weight
            total_profit += profit * frac
            item_selection.append((item_no, frac))
            capacity = 0

    return total_profit, item_selection


# ----- USER INPUT -----
n = int(input("Enter number of items: "))

weights = []
profits = []

print("Enter weight and profit for each item:")
for _ in range(n):
    w, p = map(float, input().split())
    weights.append(w)
    profits.append(p)

capacity = float(input("Enter truck capacity: "))

max_profit, selected = fractional_knapsack(weights, profits, capacity)

print("\nSelected Items (item number, fraction taken):")
for item_no, frac in selected:
    print(f"Item {item_no}: {frac*100:.2f}%")

print(f"\nMaximum Profit = {max_profit}")
