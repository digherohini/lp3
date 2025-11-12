

import random
import time


def deterministic_partition(arr, low, high):
    pivot = arr[high]  # last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


# ------------------------------------------------------
# Randomized Quick Sort (Pivot = Random Element)
# ------------------------------------------------------
def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]  # swap random pivot with last
    return deterministic_partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


# ------------------------------------------------------
# Main Program
# ------------------------------------------------------
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = [int(x) for x in input("Enter elements: ").split()]

    # Deterministic Quick Sort
    arr1 = arr.copy()
    start = time.time()
    deterministic_quicksort(arr1, 0, n - 1)
    end = time.time()
    print("\nSorted array using Deterministic Quick Sort:", arr1)
    print("Time taken (Deterministic): {:.6f} sec".format(end - start))

    # Randomized Quick Sort
    arr2 = arr.copy()
    start = time.time()
    randomized_quicksort(arr2, 0, n - 1)
    end = time.time()
    print("\nSorted array using Randomized Quick Sort:", arr2)
    print("Time taken (Randomized): {:.6f} sec".format(end - start))
