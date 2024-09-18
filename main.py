from SimplexMethod import Simplex

def main():
    C = [1, 2, 3]
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [1, 2, 3]
    e = 0.0001
    model = Simplex(C, A, b, e)

if __name__ == '__main__':
    main()