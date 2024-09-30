from SimplexMethod import Simplex

def main():
    C = [2, -2, 6]
    A = [[2, 1, -2], [1, 2, 4], [1, -1, 2]]
    b = [24,23,10]
    e = 0.0001
    model = Simplex(C, A, b, e)
    C = model.simplex()
    print(C)
    print("Max value of function: ", C[-1])


if __name__ == '__main__':
    main()
    # print(round(0.0001, ndigits=3)) # 0.0