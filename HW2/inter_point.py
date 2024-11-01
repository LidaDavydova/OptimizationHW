import numpy as np
from Simplex_Method import *

def primal_dual_interior_point(C, A, b, x0, e, alpha):
    A = np.array(A, float)
    C = np.array(C, float)
    m0, n0 = A.shape
    A = np.hstack((A, np.eye(m0)))
    C = np.hstack((C, np.zeros((1,m0), float)[0]))

    x0 = np.array(x0, float)
    m, n = A.shape

    # Check if dimensions match
    if len(C) != n or len(x0) != n or len(b) != m:
        print("The method is not applicable!")
        return None, None

    x = x0.copy()

    max_iter = 5000

    for k in range(max_iter):
        v = x
        D = np.diag(x)
        AA = np.dot(A,D)
        cc = np.dot(D, C)
        I = np.eye(n)
        F = np.dot(AA, np.transpose(AA))
        try:
            FI = np.linalg.inv(F)
        except np.linalg.LinAlgError:
            print("The problem does not have solution!")
            return None, None
        H = np.dot(np.transpose(AA), FI)
        P = np.subtract(I, np.dot(H, AA))
        cp = np.dot(P, cc)
        nu = np.absolute(np.min(cp))
        y = np.add(np.ones(n, float), ( alpha /nu ) * cp )
        yy = np.dot(D, y)
        x = yy
        # print(x)

        if np.linalg.norm(np.subtract(yy, v), ord=2) < e:
            break

    # Check if solution is found
    if k == max_iter - 1:
        print("The method did not converge within the maximum number of iterations.")
        return None, None

    # Compute the objective value
    obj_value = C @ x

    return x, obj_value