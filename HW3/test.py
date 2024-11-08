from transp_prob import *

def test_cases():
    test_data = [
        ([140, 180, 160], [[2, 3, 4, 2, 4], [8, 4, 1, 4, 1], [9, 7, 3, 7, 2]], [60, 70, 120, 130, 100]),
        ([160, 140, 170], [[7, 8, 1, 2], [4, 5, 9, 8], [9, 2, 3, 6]], [120, 50, 190, 110]),
        ([100, 150, 200], [[5, 9, 2, 6], [4, 8, 7, 3], [6, 7, 5, 4]], [80, 120, 140, 110]),
    ]

    for i, (S, C, D) in enumerate(test_data):
        try:
            print(f"\nTest Case {i + 1}:")

            if len(S) != 3:
                raise ValueError("The method is not applicable!")

            if any(len(row) != 4 for row in C):
                raise ValueError("The method is not applicable!")

            if len(D) != 4:
                raise ValueError("The method is not applicable!")

            if sum(S) != sum(D):
                raise ValueError("The problem is not balanced!")

            print_problem(S, C, D)

            nw_solution = north_west(S, C, D)
            print("North-West Corner Solution:")
            print(nw_solution)

            vogel_solution = vogels_approximation(S, C, D)
            print("Vogel's Approximation Solution:")
            print(vogel_solution)

            russell_solution = russell_approximation(S, C, D)
            print("Russell's Approximation Solution:")
            print(russell_solution)

        except ValueError as e:
            print(f"{e}")

if __name__ == "__main__":
    test_cases()
