

def fractional_knapsack(values, weights, capacity):
    n = len(values)
    
    # Calculate value/weight ratio for each item
    ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    
    # Sort items by ratio in descending order (Greedy choice)
    ratio.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    remaining_capacity = capacity
    
    print("\nItem\tWeight\tValue\tValue/Weight")
    print("-------------------------------------")
    for r, v, w in ratio:
        print(f"{v}\t{w}\t{v}\t{r:.2f}")
    
    print("\n--- Selection Process ---")
    for r, v, w in ratio:
        if remaining_capacity == 0:
            break
        
        if w <= remaining_capacity:
            total_value += v
            remaining_capacity -= w
            print(f"Took full item (weight={w}, value={v})")
        else:
            fraction = remaining_capacity / w
            total_value += v * fraction
            print(f"Took {fraction*100:.2f}% of item (weight={w}, value={v})")
            remaining_capacity = 0
    
    print(f"\nMaximum value in Knapsack = {total_value:.2f}")
    return total_value



if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    values = [float(x) for x in input("Enter values of items: ").split()]
    weights = [float(x) for x in input("Enter weights of items: ").split()]
    capacity = float(input("Enter capacity of knapsack: "))
    
    fractional_knapsack(values, weights, capacity)
