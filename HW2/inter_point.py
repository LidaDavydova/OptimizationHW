import numpy as np
from Simplex_Method import *

def primal_dual_interior_point(C, A, b, x0, e, alpha):
    A = np.array(A, float)
    x0 = np.array(x0, float)
    m, n = A.shape

    # Check if dimensions match
    if len(C) != n or len(x0) != n or len(b) != m:
        print("The method is not applicable!")
        return None, None

    x = x0.copy()
    s = np.ones(n)
    y = np.zeros(m)

    max_iter = 5000
    tol = e
    mu = (x @ s) / n

    for k in range(max_iter):
        # # Compute residuals
        r_b = A @ x - b
        r_c = A.T @ y + s - C
        r_mu = x * s

        # Stopping condition
        if np.linalg.norm(r_b) <= tol and np.linalg.norm(r_c) <= tol and mu <= tol:
            break

        # Form the KKT matrix
        diag_x_inv = np.diag(x)
        diag_s = np.diag(s)
        M = A @ diag_x_inv @ diag_s @ A.T

        # Right-hand side
        r = -r_b + A @ diag_x_inv @ (alpha * mu * np.ones(n) - r_mu)

        # Solve for Δy
        try:
            delta_y = np.linalg.solve(M, r)
        except np.linalg.LinAlgError:
            print("The problem does not have solution!")
            return None, None

        # Solve for Δx and Δs
        delta_x = -diag_x_inv @ (A.T @ delta_y + s - C)
        delta_s = -r_c - A.T @ delta_y

        # Compute step sizes
        idx_x_neg = delta_x < 0
        idx_s_neg = delta_s < 0
        alpha_primal = min(1, alpha * min((-x[idx_x_neg] / delta_x[idx_x_neg]).min(), 1) if idx_x_neg.any() else 1)
        alpha_dual = min(1, alpha * min((-s[idx_s_neg] / delta_s[idx_s_neg]).min(), 1) if idx_s_neg.any() else 1)

        # Update variables
        x += alpha_primal * delta_x
        y += alpha_dual * delta_y
        s += alpha_dual * delta_s

        mu = (x @ s) / n

        # v = x
        # D = np.diag(x)
        # AA = np.dot(A,D)
        # cc = np.dot(D, C)
        # I = np.eye(n)
        # F = np.dot(AA, np.transpose(AA))
        # try:
        #     FI = np.linalg.inv(F)
        # except np.linalg.LinAlgError:
        #     print("The problem does not have solution!")
        #     return None, None
        # H = np.dot(np.transpose(AA), FI)
        # P = np.subtract(I, np.dot(H, AA))
        # cp = np.dot(P, cc)
        # nu = np.absolute(np.min(cp))
        # y = np.add(np.ones(n, float), ( alpha /nu ) * cp )
        # yy = np.dot(D, y)
        # x = yy

    # Check if solution is found
    if k == max_iter - 1:
        print("The method did not converge within the maximum number of iterations.")
        return None, None

    # Compute the objective value
    obj_value = C @ x

    return x, obj_value

def main():
    # Input data
    print("Enter the coefficients of the objective function (number of variables is 3):")
    C = np.array(list(map(float, input().split())))

    m, n = 3, 3

    print("Enter the coefficients of the constraint matrix row-wise (number of constrains is 3):")
    A_elements = []
    for _ in range(m):
        row = list(map(float, input().split()))
        if len(row) != n:
            print("The method is not applicable!")
            return
        A_elements.append(row)
    A = np.array(A_elements)

    print("Enter the right-hand side vector (b):")
    b = np.array(list(map(float, input().split())))

    if len(b) != m:
        print("The method is not applicable!")
        return

    print("Enter the initial starting point (x0):")
    x0 = np.array(list(map(float, input().split())))

    if len(x0) != n:
        print("The method is not applicable!")
        return

    print("Enter the approximation accuracy (e):")
    e = float(input())

    # Run for alpha = 0.5
    alpha = 0.5
    x, z = primal_dual_interior_point(C, A, b, x0, e, alpha)
    if x is not None:
        print(f"A vector of decision variables (alpha = {alpha}): {x}")
        print(f"Maximum value of the objective function (alpha = {alpha}): {z}")

    # Run for alpha = 0.9
    alpha = 0.9
    x, z = primal_dual_interior_point(C, A, b, x0, e, alpha)
    if x is not None:
        print(f"A vector of decision variables (alpha = {alpha}): {x}")
        print(f"Maximum value of the objective function (alpha = {alpha}): {z}")

    
