from Simplex_Method import *
from inter_point import primal_dual_interior_point

def test_cases():
    num_of_decision_var = 3

    test_data = [
        ([3, 5], [[1, 0], [0, 2], [3, 2]], [4, 12, 18], [2, 6], 0.0001),
        ([10, 20, 15], [[2, 1, 3], [1, 3, 2], [4, 2, 1]], [30, 40, 50], [5, 5, 0, 15, 20, 20], 0.0001),
        ([2, 3, -1], [[2, -1, -2], [3, 2, -3], [-1, 3, 4]], [16, 18, 24], [4, 6, 2, 18, 0, 2], 0.0001),
        ([9, 10, 16], [[18, 15, 12], [6, 4, 8], [5, 3, 3]], [360, 192, 180], [0, 1, 1, 333, 180, 174], 0.0001),
        ([2, -2, 6], [[2, 1, -2], [1, 2, 4], [1, -1, 2]], [24, 23, 10], [0, 1, 1, 25, 17, 9], 0.0001),

    ]

    for i, (C, A, b, x0, e) in enumerate(test_data):
        print(f"\nTest Case {i + 1}:")
        # Iterior point method
        eps = len(str(e).split(".")[1])

        alpha = 0.5
        x, z = primal_dual_interior_point(C, A, b, x0, e, alpha)
        # print(f"A vector of decision variables - ({round(x1, e)}, {round(x2, e)}, {round(x3, e)}).")  # excluding slack variables
        if (x is not None):
            x1, x2, x3 = x[0], x[1], x[2]
            print(f"A vector of decision variables - ({round(x1, eps)}, {round(x2, eps)}, {round(x3, eps)}).")
            print(f"Maximum value of the objective function: {round(z, eps)}.") # z

        alpha = 0.9
        x, z = primal_dual_interior_point(C, A, b, x0, e, alpha)
        if (x is not None):
            x1, x2, x3 = x[0], x[1], x[2]
            print(f"A vector of decision variables - ({round(x1, eps)}, {round(x2, eps)}, {round(x3, eps)}).")
            print(f"Maximum value of the objective function: {round(z, eps)}.") # z
        

        print("\nBy Simplex method:")

        if not validate_input(C, A, b, e, num_of_decision_var):
            print("The method is not applicable!")
            continue

        # Simplex method
        model = Simplex(C, A, b, e)
        result = model.simplex()
        
        x1, x2, x3, ans = 0,0,0,0
        
        if result:
            for j in range(len(result)):
                if result[j][0] == 'x1':
                    x1 = result[j][1]
                elif result[j][0] == 'x2':
                    x2 = result[j][1]
                elif result[j][0] == 'x3':
                    x3 = result[j][1]
                elif result[j][0] == 'ans':
                    ans = result[j][1]

            print(f"A vector of decision variables - ({round(x1, eps)}, {round(x2, eps)}, {round(x3, eps)}).")  # excluding slack variables
            print(f"Maximum value of the objective function: {round(ans, eps)}.") # z

        else:
            print("The method is not applicable!")
        
if __name__ == '__main__':
    test_cases()  # Uncomment this line for running test cases
