

# Test cases
from SimplexMethod import Simplex

def test_cases():
    test_data = [
        ([3, 5], [[1, 0], [0, 2], [3, 2]], [4, 12, 18], 0.0001),
        ([2, 3, 4], [[1, 1, 2], [2, 2, 3], [1, 0, 1]], [8, 15, 5], 0.0001),
        ([5, 4], [[6, 4], [1, 2], [-1, 1]], [24, 6, 1], 4),
        ([6, 8, 5], [[1, 2, 1], [3, 2, 4], [1, 1, 2]], [20, 42, 15], 0.0001),
        ([10, 20, 15], [[2, 1, 3], [1, 3, 2], [4, 2, 1]], [30, 40, 50], 0.0001)
    ]

    for i, (C, A, b, e) in enumerate(test_data):
        print(f"\nTest Case {i + 1}:")
        model = Simplex(C, A, b, e)
        result = model.simplex()
        # correct_result = ...
        # if result:
        #     print("Decision variables (x*):", result[:-len(A)])  # excluding slack variables
        #     print("Maximum value of the objective function: ", result[-1]) # z

        #     if correct_result[i] == result:
        #         print("Test passed!")
        #     else:
        #         print("Test failed!")
        #         print(f"Expected: {correct_result[i]}")
        # else:
        #     print("The method is not applicable!")
        # print(result)
        x1,x2,ans = 0,0,0
        if result != None:
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
    test_cases()  # Uncomment this line for running test cases
