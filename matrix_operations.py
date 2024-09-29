
# if row is inside nullified matrix/vector
def nullify_col_inside(A, p_row: int, p_col):
    n_rows = len(A)
    for i in range(n_rows):
        mltp = A[i][p_col]
        for j in range(len(A[i])):
            if j != p_col:
                A[i][j] -= mltp * A[p_row][j]
    return A

# if row is not in nullified matrix/vector
def nullify_col(A, row: list, p_col):
    n_rows = len(A)
    for i in range(n_rows):
        mltp = A[i][p_col]
        for j in range(len(A[i])):
            if j != p_col:
                A[i][j] -= mltp * row[j]
    return A

# devide row by devider
def devide_row(A, row, devider):
    for i in range(len(A[row])):
        A[row][i] /= devider
    return A