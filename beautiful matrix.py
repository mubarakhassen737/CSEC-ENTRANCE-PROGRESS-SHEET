matrix = []

row = 0
col = 0

for i in range(5):
    row_values = list(map(int, input().split()))
    matrix.append(row_values)
    
    if 1 in row_values:
        row = i
        col = row_values.index(1)

# Center is (2,2) in 0-based indexing
moves = abs(row - 2) + abs(col - 2)

print(moves)