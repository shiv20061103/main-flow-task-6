def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0) 

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop() 
    return max_area

def maximal_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    n_cols = len(matrix[0])
    heights = [0] * n_cols
    max_area = 0

    for row in matrix:
        for i in range(n_cols):

            heights[i] = heights[i] + 1 if row[i] == 1 else 0
        max_area = max(max_area, largest_rectangle_area(heights))

    return max_area

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the binary matrix row by row (0s and 1s separated by spaces):")
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    if len(row) != cols:
        print("Error: Row length does not match number of columns.")
        exit()
    matrix.append(row)

max_rectangle = maximal_rectangle(matrix)
print(f"\nArea of the largest rectangle of 1's: {max_rectangle}")
