from SimplexMethod import Simplex
from validation import validate_input

def main():
    num_of_decision_var = 2
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
    
    if not validate_input(C, A, b, e, num_of_decision_var):
        print("The method is not applicable!")

    # Create the Simplex model and solve the linear program
    model = Simplex(C, A, b, e)
    result = model.simplex()
    
    # Print results
    if result:
        print("Decision variables (x*):", result[:-len(A)])  # excluding slack variables
        print("Maximum value of the objective function: ", -result[-1])  # negate to get the max value
    else:
        print("The method is not applicable!")


if __name__ == '__main__':
    main()
    # print(round(0.0001, ndigits=3)) # 0.0
