def find_median_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    n = len(merged)
    if n % 2 == 0:
        median = (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        median = merged[n//2]

    return median

arr1 = list(map(int, input("Enter the first sorted list (space-separated): ").split()))
arr2 = list(map(int, input("Enter the second sorted list (space-separated): ").split()))

median = find_median_sorted_arrays(arr1, arr2)
print(f"\nMedian of the two sorted arrays: {median}")
