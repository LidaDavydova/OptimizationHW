from SimplexMethod import Simplex
from validation import validate_input

def main():
    num_of_decision_var = 3
    # User input for the linear program
    print("Enter coefficients of the objective function (C) separated by space:")
    C = list(map(float, input().strip().split()))
   
    print("Enter coefficients of the constraint functions (A) as rows, separated by spaces (end with an empty line):")
    A = []
    while True:
        line = input().strip()
        if line == "":
            break
        A.append(list(map(float, line.split())))
        
    print("Enter the right-hand side vector (b) separated by space:")
    b = list(map(float, input().strip().split()))
    
    print("Enter the approximation accuracy (e.g., 0.0001):")
    e = float(input().strip())

    # Print problem
    print(f"Max z = {C[0]} * x1 + {C[1]} * x2 + {C[2]} * x3")
    print("Subject to the constraints:")
    print(f"{A[0][0]} * x1 + {A[0][1]} * x2 + {A[0][2]} * x3 <= {b[0]}")
    print(f"{A[1][0]} * x1 + {A[1][1]} * x2 + {A[1][2]} * x3 <= {b[1]}")
    print(f"{A[2][0]} * x1 + {A[2][1]} * x2 + {A[2][2]} * x3 <= {b[2]}")
    
    if not validate_input(C, A, b, e, num_of_decision_var):
        print("The method is not applicable!")

    # Create the Simplex model and solve the linear program
    model = Simplex(C, A, b, e)
    result = model.simplex()
    
    # Print results
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
       
        print(f"A vector of decision variables - ({round(x1, e)}, {round(x2, e)}, {round(x3, e)}).")  # excluding slack variables
        print(f"Maximum value of the objective function: {round(ans, e)}.") # z

    else:
        print("The method is not applicable!")


if __name__ == '__main__':
    main()
