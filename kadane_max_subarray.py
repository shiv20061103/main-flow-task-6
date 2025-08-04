def kadane_max_subarray(arr):
    if not arr:
        return 0

    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    return max_global

arr = list(map(int, input("Enter the list of integers (space-separated): ").split()))

max_sum = kadane_max_subarray(arr)

print(f"\nMaximum sum of contiguous subarray: {max_sum}")
