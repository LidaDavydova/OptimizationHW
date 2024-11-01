
import numpy as np

from HW2.inter_point import primal_dual_interior_point


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

    
