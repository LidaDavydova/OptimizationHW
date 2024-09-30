from SimplexMethod import Simplex

def main():
    C = [9, 10, 16]
    A = [[18, 15, 12], [6, 4, 8], [5, 3, 3]]
    b = [360, 192, 180]
    e = 0.0001
    model = Simplex(C, A, b, e)
    C = model.simplex()
    print(C)


if __name__ == '__main__':
    main()
    # print(round(0.0001, ndigits=3)) # 0.0