from transp_prob import *

def test_cases():
    test_data = [
        ([140,180,160], [[2,3,4,2,4], [8,4,1,4,1], [9,7,3,7,2]], [60,70,120,130,100]),
        ([160,140,170], [[7,8,1,2], [4,5,9,8], [9,2,3,6]], [120,50,190,110]),

    ]

    for i, (S, C, D) in enumerate(test_data):
        print(f"\nTest Case {i + 1}:")
        print_problem(S, C, D)

        print('By North West method:', north_west(S, C, D))

        print('By Vogel aproximation:', vogels_approximation(S, C, D))

        # print(russell_approximation(S, C, D))


if __name__ == '__main__':
    test_cases() 