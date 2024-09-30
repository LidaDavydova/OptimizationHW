
# if row is inside nullified matrix
def nullify_col_inside(A, p_row: int, p_col):
    n_rows = len(A)
    for i in range(n_rows):
        if i == p_row:
            continue
        mltp = A[i][p_col]
        for j in range(len(A[i])):
            A[i][j] -= mltp * A[p_row][j]
    return A


# devide row by devider
def devide_row(A, row, devider):
    for i in range(len(A[row])):
        A[row][i] /= devider
    return A

def identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]