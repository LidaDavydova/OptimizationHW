
from matrix_operations import *


class Simplex:
    def __init__(self, C, A, b, e):
        self.len_vars = len(C)
        C = [-c for c in C]
        solution = dict(x1=A[0][2],x2=A[1][2],ans=C[2]) #dictionary for soliutions that we are going to return 
        size = len(A)
        identity = identity_matrix(size)
        for i in range(size):
            A[i].extend(identity[i])
            C.append(0)

        C += [0] # solution for C (z)
        C = ['z'] + C #append name for row
        M = []
        M.append(C)
        for i in range(size):
            M.append(['x' + str(i+1)] + A[i] + [b[i]]) 

        self.M = M
        self.solution = solution 

    def min_col_C(self) -> int:
        C = self.M[0][:self.len_vars]
        return C.index(min(C))

    def pivot(self, col_i) -> tuple:
        A = self.M[1:]
        b = [i[-1] for i in self.M[1:]] # exclude solution for C (z)
        mn_i = 0
        mn = -1
        
        for i in range(len(A)):
            try:
                b[i] /= A[i][col_i]
            except ZeroDivisionError:
                b[i] = -1
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
            if self.M[row_i][0] == 'x1':
                self.solution.update({'x1':0})
                self.M[row_i][0] = 's'
            elif self.M[row_i][0] == 'x2':
                self.solution.update({'x2':0})
                self.M[row_i][0] = 's'
            elif self.M[row_i][0] == 's':
                if col_i == 1:
                    self.solution.update({'x1':self.A[row_i][-1]})
                    self.M[row_i][0] = 'x1'
                elif col_i == 2:
                    self.solution.update({'x2':self.A[row_i][-1]})
                    self.M[row_i][0] = 'x2'
            print(self.M)
            self.solution.update({'ans':self.M[0][-1]})
        # return self.M[0] # C row
        return self.solution

