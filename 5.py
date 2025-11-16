def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # result matrix
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):              # row of A
        for j in range(cols_B):          # column of B
            for k in range(cols_A):      # matching index
                result[i][j] += A[i][k] * B[k][j]

    return result


# ----- USER INPUT -----
print("Enter 4x4 transformation matrix:")
T = []
for _ in range(4):
    row = list(map(float, input().split()))
    T.append(row)

print("Enter 4x1 vertex (x y z 1):")
V = []
for _ in range(4):
    V.append([float(input())])

# ----- MULTIPLY -----
new_vertex = matrix_multiply(T, V)

print("\nTransformed Vertex:")
for row in new_vertex:
    print(row[0])
