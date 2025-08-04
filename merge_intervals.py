def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
  
    merged = []
  
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged

user_input = input("Enter intervals (e.g. 1 3,2 6,8 10): ")
intervals = []
for pair in user_input.split(','):
    start, end = map(int, pair.strip().split())
    intervals.append([start, end])
merged_result = merge_intervals(intervals)

print("\nMerged Intervals:")
for interval in merged_result:
    print(interval)
