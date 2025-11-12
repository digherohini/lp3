
def knapsack(values, weights, capacity):
    n = len(values)
    
    # Create DP table of size (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include item i-1 or exclude it — take max value
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # dp[n][capacity] holds the maximum value
    return dp[n][capacity]


# -----------------------------------------------------
# Main Program
# -----------------------------------------------------
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    values = [int(x) for x in input("Enter values of items: ").split()]
    weights = [int(x) for x in input("Enter weights of items: ").split()]
    capacity = int(input("Enter capacity of knapsack: "))
    
    max_value = knapsack(values, weights, capacity)
    print(f"\nMaximum value in Knapsack = {max_value}")
