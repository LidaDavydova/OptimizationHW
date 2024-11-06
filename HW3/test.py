from transp_prob import *

def test_cases():
    test_data = [
    ([140, 180, 160], [[2, 3, 4, 2, 4], [8, 4, 1, 4, 1], [9, 7, 3, 7, 2]], [60, 70, 120, 130, 100]),
    ([160, 140, 170], [[7, 8, 1, 2], [4, 5, 9, 8], [9, 2, 3, 6]], [120, 50, 190, 110]),
    ([100, 150, 200], [[5, 9, 2, 6], [4, 8, 7, 3], [6, 7, 5, 4]], [80, 120, 140, 110]),
    ([150, 200, 250], [[3, 4, 1, 7], [8, 6, 2, 5], [7, 4, 9, 3]], [100, 150, 200, 150]),
    ([180, 220, 170], [[4, 5, 2, 3], [7, 9, 6, 4], [3, 2, 7, 8]], [130, 140, 170, 130]),
]


    for i, (S, C, D) in enumerate(test_data):
        print(f"\nTest Case {i + 1}:")
        print_problem(S, C, D)

        print('By North West method:\n', north_west(S, C, D))

        print('By Vogel aproximation:\n=', vogels_approximation(S, C, D))

        # print(russell_approximation(S, C, D))


if __name__ == '__main__':
    test_cases() 