def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(0, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
weights = list(map(int, input("Enter the weights separated by spaces: ").split()))

values = list(map(int, input("Enter the values separated by spaces: ").split()))

capacity = int(input("Enter the maximum capacity of the knapsack: "))

if len(weights) != len(values):
    print("Error: Number of weights and values must be the same.")
else:
    max_value = knapsack(weights, values, capacity)
    print(f"\nMaximum value that can be carried: {max_value}")
