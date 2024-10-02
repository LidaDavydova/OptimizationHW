

# Test cases
def test_cases():
    test_data = [
        ([3, 5], [[1, 0], [0, 2], [3, 2]], [4, 12, 18], 0.0001),
        ([2, 3, 4], [[1, 1, 2], [2, 2, 3], [1, 0, 1]], [8, 15, 5], 0.0001),
        ([5, 4], [[6, 4], [1, 2], [-1, 1]], [24, 6, 1], 0.0001),
        ([6, 8, 5], [[1, 2, 1], [3, 2, 4], [1, 1, 2]], [20, 42, 15], 0.0001),
        ([10, 20, 15], [[2, 1, 3], [1, 3, 2], [4, 2, 1]], [30, 40, 50], 0.0001)
    ]

    for i, (C, A, b, e) in enumerate(test_data):
        print(f"\nTest Case {i + 1}:")
        model = Simplex(C, A, b, e)
        result = model.simplex()
        if result:
            print("Decision variables (x*):", result[:-len(A)])  # excluding slack variables
            print("Maximum value of the objective function: ", -result[-1])  # negate to get the max value
        else:
            print("The method is not applicable!")

if __name__ == '__main__':
    test_cases()  # Uncomment this line for running test cases
