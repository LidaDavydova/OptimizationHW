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
    
    if not validate_input(C, A, b, e, num_of_decision_var):
        print("The method is not applicable!")

    # Create the Simplex model and solve the linear program
    model = Simplex(C, A, b, e)
    result = model.simplex()
    
    # Print results
    x1,x2,ans = 0,0,0
    if result:
        for j in range(len(result)):
            if result[j][0] == 'x1':
                x1 = result[j][1]
            elif result[j][0] == 'x2':
                x2 = result[j][1]
            elif result[j][0] == 'ans':
                ans = result[j][1]
        
        print('x1: ' + str(round(x1, 4)) + '\n' +
                'x2: ' + str(round(x2, 4)) + '\n' +
                'solution: '+ str(round(ans, 4))
                )
    else:
        print("an error occured")


if __name__ == '__main__':
    main()
    # print(round(0.0001, ndigits=3)) # 0.0
