
from matrix_operations import *


class Simplex:
    def __init__(self, C, A, b, e):
        self.len_vars = len(C)
        self.e = e
        solution = [['z',0],
                    ['s',b[0]],
                    ['s',b[1]],
                    ['s',b[2]]]
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
        self.solution = solution

    def min_col_C(self) -> tuple:
        C = self.M[0][:-1]
        mn = 0
        mn_i = -1
        for i in range(len(C)):
            if C[i] < mn and C[i] < -self.e:
                mn = C[i]
                mn_i = i
        return (mn, mn_i)

    def pivot(self, col_i) -> tuple:
        A = self.M[1:]
        b = [i[-1] for i in self.M[1:]] # exclude solution for C (z)
        mn_i = -1
        mn = float('inf')
        
        for i in range(len(A)):
            # try:
            #     b[i] /= A[i][col_i]
            # except ZeroDivisionError:
            #     b[i] = -1
            # if b[i] > 0 and (mn == -1 or b[i] < mn):
            #     mn = b[i]
            #     mn_i = i

            if A[i][col_i] > self.e:
                ratio = b[i] / A[i][col_i]
                if ratio < mn - self.e: 
                    mn = ratio
                    mn_i = i
                elif abs(ratio - mn) < self.e and i < mn_i:  
                    mn_i = i

        if mn_i == -1:
            return (-1, -1) # no solution

        return (mn_i+1, col_i)


    def simplex(self):
        mn, mn_col = self.min_col_C()
        z = -1
        # n = 0
        while mn < -self.e and z != self.M[0][-1]:
            z = self.M[0][-1]

            row_i, col_i = self.pivot(mn_col)

            if (row_i, col_i) == (-1, -1):
                return None

            # perfome
            
            pivot = self.M[row_i][col_i]
            # update A - matrix
            self.M = devide_row(self.M, row_i, pivot)
            self.M = nullify_col_inside(self.M, p_row=row_i, p_col=col_i)

            if col_i == 0:
                var = 'x1'
            elif col_i == 1:
                var = 'x2'
            elif col_i == 2:
                var = 'x3'
            else:
                var = 's'
            
            for i in range(len(self.solution)):
                if self.solution[i][0] == var:
                    self.solution[i] = ['s',0]
                    break
            self.solution[row_i] = [var, self.M[row_i][-1]]

            mn, mn_col = self.min_col_C()
        
        for i in range(len(self.solution)):
            self.solution[i][1] = self.M[i][-1]
        self.solution.append(['ans', self.M[0][-1]])
        
        # res = [row[-1] for row in self.M]
        # return res # solution column
        return self.solution 