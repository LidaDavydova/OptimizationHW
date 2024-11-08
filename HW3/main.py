from transp_prob import *

def get_input():
    supply = list(map(int, input("Enter 3 supply values separated by spaces: ").split()))
    if len(supply) != 3:
        raise ValueError("The method is not applicable!")

    print("Enter cost matrix of dimensions 3x4 (row by row):")
    cost_matrix = []
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1} values separated by spaces: ").split()))
        if len(row) != 4:
            raise ValueError("The method is not applicable!")
        cost_matrix.append(row)

    demand = list(map(int, input("Enter 4 demand values separated by spaces: ").split()))
    if len(demand) != 4:
        raise ValueError("The method is not applicable!")

    if sum(supply) != sum(demand):
        raise ValueError("The problem is not balanced!")

    return supply, cost_matrix, demand

def main():
    try:
        supply, cost_matrix, demand = get_input()

        print("Transportation problem:")
        print_problem(supply, cost_matrix, demand)

        nw_solution = north_west(supply, cost_matrix, demand)
        print("North-West Corner Solution:")
        print(nw_solution)


        vogel_solution = vogels_approximation(supply, cost_matrix, demand)
        print("Vogel's Approximation Solution:")
        print(vogel_solution)

        russell_solution = russell_approximation(supply, cost_matrix, demand)
        print("Russell's Approximation Solution:")
        print(russell_solution)

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
