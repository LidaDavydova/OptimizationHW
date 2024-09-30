
from matrix_operations import *


class Simplex:
    def __init__(self, C, A, b, e):
        C = [-c for c in C]
        
        size = len(A)
        identity = identity_matrix(size)
        for i in range(size):
            A[i].extend(identity[i])
            C.append(0)

        C += [0] # solution for C (z)
        M = []
        M.append(C)
        for i in range(size):
            M.append(A[i] + [b[i]])

        self.M = M

    def min_col_C(self) -> int:
        C = self.M[0][:-1]
        return C.index(min(C))

    def pivot(self, col_i) -> tuple:
        A = self.M[1:][:-1]
        b = [i[-1] for i in self.M[1:]] # exclude solution for C (z)
        mn_i = 0
        mn = -1
        
        for i in range(len(A)):
            b[i] /= A[i][col_i]
            if b[i] > 0 and (mn == -1 or b[i] < mn):
                mn = b[i]
                mn_i = i

        return (mn_i+1, col_i)


    def simplex(self):
        while min(self.M[0][:-1]) < 0:
            row_i, col_i = self.pivot(self.min_col_C())

            # perfome
            
            pivot = self.M[row_i][col_i]
            # update A - matrix
            self.M = devide_row(self.M, row_i, pivot)
            self.M = nullify_col_inside(self.M, p_row=row_i, p_col=col_i)

        return self.M[0] # C row

