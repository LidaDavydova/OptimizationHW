
class Simplex:
    def __init__(self, C, A, b, e):
        self.C = C
        self.A = A
        self.b = b
        self.e = e
        self.C_len = len(C)
        self.A_rows = len(A[0])

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
        B = self.B
        while min(self.C) < 0:
            row_i, col_i = self.pivot(self.min_col_C())

            # perfome 