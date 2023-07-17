r = int(input())
c = int(input())
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        element = int(input())
        row.append(element)
    matrix.append(row)
l = []
for i in range(c):
    col_sum = 0
    for j in range(r):
        col_sum += matrix[j][i]
    l.append(col_sum)
print(l)
