
from matrix_operations import *


class Simplex:
    def __init__(self, C, A, b, e):
        C = [-c for c in C]
        C.extend([0 for _ in range(len(A))])
        self.C = C
        self.A = A
        self.b = b
        self.e = e
        self.z = 0

    def min_col_C(self) -> int:
        # here check for min < e => stop ?????????
        return self.C.index(min(self.C))

    def pivot(self, col_i) -> tuple:
        A = self.A
        b = self.b
        
        for i in range(self.A_rows):
            b[i] /= A[i][col_i]
        
        return (b.index(min(b)), col_i)


    def simplex(self):
        A = self.A
        b = self.b
        C = self.C
        while min(self.C) < 0:
            row_i, col_i = self.pivot(self.min_col_C())

            # perfome
            
            pivot = A[row_i][col_i]
            # update A - maatrix
            A = devide_row(A, row_i, A[row_i][col_i])
            A = nullify_col_inside(A, p_row=row_i, p_col=col_i)

            # update b - vector
            b[row_i] /= pivot
            b = nullify_col_inside(b, p_row=row_i, p_col=0)

            # update C - vector
            C[row_i] /= pivot
            C = nullify_col(C, row=A[row_i], p_col=col_i)

