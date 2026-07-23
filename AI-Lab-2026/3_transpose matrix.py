def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [4, 5, 6]]
print("Original Matrix:")
for row in matrix:
    print(row)
print("\nTransposed Matrix:")
for row in transpose(matrix):
    print(row)
