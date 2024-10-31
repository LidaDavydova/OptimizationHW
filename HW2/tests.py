import sys
sys.path.append('../')
from ..HW1.SimplexMethod import Simplex
from ..HW1.validation import validate_input
from inter_point import primal_dual_interior_point

def test_cases():
    num_of_decision_var = 3

    test_data = [
        ([3, 5], [[1, 0], [0, 2], [3, 2]], [4, 12, 18], [2, 6], 0.0001),
        ([10, 20, 15], [[2, 1, 3], [1, 3, 2], [4, 2, 1]], [30, 40, 50], [7.2, 9.6, 2], 0.0001),
        ([2, 3, -1], [[2, -1, -2], [3, 2, -3], [-1, 3, 4]], [16, 18, 24], [404/21, -12/7, 254/21], 0.0001),
        ([9, 10, 16], [[18, 15, 12], [6, 4, 8], [5, 3, 3]], [360, 192, 180], [384/5, -344/5, 4/5], 0.0001),
        ([2, -2, 6], [[2, 1, -2], [1, 2, 4], [1, -1, 2]], [24, 23, 10], [34/3, 43/12, 9/8], 0.0001),

    ]

    for i, (C, A, b, x0, e) in enumerate(test_data):
        print(f"\nTest Case {i + 1}:")
        if not validate_input(C, A, b, e, num_of_decision_var):
            print("The method is not applicable!")
            continue

        # Iterior point method
        alpha = 0.5
        x, z = primal_dual_interior_point(C, A, b, x0, e, alpha)
        # print(f"A vector of decision variables - ({round(x1, e)}, {round(x2, e)}, {round(x3, e)}).")  # excluding slack variables
        print(f"A vector of decision variables - ({x}).")
        print(f"Maximum value of the objective function: {round(z, e)}.") # z

        alpha = 0.9
        x, z = primal_dual_interior_point(C, A, b, x0, e, alpha)
        print(f"A vector of decision variables - ({x}).")
        print(f"Maximum value of the objective function: {round(z, e)}.") # z
        
        # Simplex method
        model = Simplex(C, A, b, e)
        result = model.simplex()
        
        x1, x2, x3, ans = 0,0,0,0
        e = len(str(e).split(".")[1])
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
            
            print("By Simplex method:")
            print(f"A vector of decision variables - ({round(x1, e)}, {round(x2, e)}, {round(x3, e)}).")  # excluding slack variables
            print(f"Maximum value of the objective function: {round(ans, e)}.") # z

        else:
            print("The method is not applicable!")
        
if __name__ == '__main__':
    test_cases()  # Uncomment this line for running test cases
