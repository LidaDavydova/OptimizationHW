from Simplex_Method import *
from HW2.inter_point import primal_dual_interior_point

def main():
    # Input data
    print("Enter the coefficients of the objective function (number of variables is 3):")
    C = list(map(float, input().split()))

    m, n = 3, 3

    print("Enter the coefficients of the constraint matrix row-wise (number of constrains is 3):")
    A_elements = []
    for _ in range(m):
        row = list(map(float, input().split()))
        if len(row) != n:
            print("The method is not applicable!")
            return
        A_elements.append(row)
    A = A_elements

    print("Enter the right-hand side vector (b):")
    b = list(map(float, input().split()))

    if len(b) != m:
        print("The method is not applicable!")
        return

    print("Enter the initial starting point (x0) and slack variables:")
    x0 = list(map(float, input().split()))

    if len(x0) != n*2:
        print("The method is not applicable!")
        return

    print("Enter the approximation accuracy (e):")
    e = float(input())
    e = len(str(e).split(".")[1])

    # Run for alpha = 0.5
    alpha = 0.5
    x, z = primal_dual_interior_point(C, A, b, x0, e, alpha)
    if x is not None:
        x1, x2, x3 = x[0], x[1], x[2]
        print("By Interior-Point method:")
        print("Alpha = ", alpha )
        print(f"A vector of decision variables - ({round(x1, e)}, {round(x2, e)}, {round(x3, e)}).")
        print(f"Maximum value of the objective function: {round(z, e)}.") # z

    # Run for alpha = 0.9
    alpha = 0.9
    x, z = primal_dual_interior_point(C, A, b, x0, e, alpha)
    if x is not None:
        x1, x2, x3 = x[0], x[1], x[2]
        print("Alpha = ", alpha )
        print(f"A vector of decision variables - ({round(x1, e)}, {round(x2, e)}, {round(x3, e)}).")
        print(f"Maximum value of the objective function: {round(z, e)}.") # z
    
    
    print("By Simplex method:")  

    if not validate_input(C, A, b, e, 3):
        print("The method is not applicable!")
    
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

        print(f"A vector of decision variables - ({round(x1, e)}, {round(x2, e)}, {round(x3, e)}).")  # excluding slack variables
        print(f"Maximum value of the objective function: {round(ans, e)}.") # z

    else:
        print("The method is not applicable!")
    
    
if __name__ == '__main__':
    main()

   
    
