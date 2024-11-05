import numpy as np

def fill_gap_spaces(a, b) -> str:
    return ' ' * (len(a) - len(b))

def print_problem(S, C2, D):
    C = [[str(C2[i][j]) for j in range(len(C2[0]))] for i in range(len(C2))]
    for j in range(len(C[0])):
        mx = max([C[i][j] for i in range(len(C))]+[D[j]], key=lambda x: len(str(x)))
        for i in range(len(C)):
            C[i][j] = str(C[i][j]) + fill_gap_spaces(str(mx), str(C[i][j]))

    for i in range(len(C)):
        row = ' '.join(map(str, C[i]))
        row += ' | ' + str(S[i])
        print(row)

    print('-'*len(row))
    print(' '.join(map(str, D)))


def north_west(S2, C2, D2):
    C = [[C2[i][j] for j in range(len(C2[0]))] for i in range(len(C2))] 
    D = [D2[j] for j in range(len(D2))]
    S = [S2[i] for i in range(len(S2))]
    m, n = len(C), len(C[0])
    i, j = 0, 0
    cost = np.zeros((m, n))
    while i < m and j < n:
        if S[i] == 0:
            i += 1
        elif D[j] == 0:
            j += 1
        else:
            x = min(S[i], D[j])
            cost[i][j] = x
            S[i] -= x
            D[j] -= x

    return cost

def vogels_approximation(S2, C2, D2):
    C = [[C2[i][j] for j in range(len(C2[0]))] for i in range(len(C2))] 
    D = [D2[j] for j in range(len(D2))]
    S = [S2[i] for i in range(len(S2))]
    m, n = len(C), len(C[0])
    cost = np.zeros((m, n))
    
    while sum(S) > 0 and sum(D) > 0:
        penalties = []

        for j in range(n):
            col = sorted([C[i][j] for i in range(m) if D[j] > 0])
            if len(col) > 1:
                penalties.append((col[1] - col[0], 'col', j))
            elif len(col) == 1:
                penalties.append((col[0], 'col', j))

        for i in range(m):
            row = sorted([C[i][j] for j in range(n) if S[i] > 0])
            if len(row) > 1:
                penalties.append((row[1] - row[0], 'row', i))
            elif len(row) == 1:
                penalties.append((row[0], 'row', i))

        penalty = max(penalties)
        
        if penalty[1] == 'row':
            i = penalty[2]
            j = min((j for j in range(n) if D[j] > 0), key=lambda j: C[i][j])
        else:
            j = penalty[2]
            i = min((i for i in range(m) if S[i] > 0), key=lambda i: C[i][j])

        if S[i] < D[j] and S[i] != 0:
            x = S[i]
        else:
            x = D[j]
        cost[i][j] = x
        S[i] -= x
        D[j] -= x

    return cost

# print(vogels_approximation([140,180,160], [[2,3,4,2,4], [8,4,1,4,1], [9,7,3,7,2]], [60,70,120,130,100]))

def russell_approximation(S, C, D):
    m = len(S)
    n = len(D)
    total_supply = sum(S)
    total_demand = sum(D)

    if total_supply != total_demand:
        raise ValueError("Total supply must equal total demand")

    # Initialize allocation matrix
    allocation = [[0] * n for _ in range(m)]

    # Calculate penalties
    penalties = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            row_min = min(C[i][k] for k in range(n) if k != j)
            col_min = min(C[k][j] for k in range(m) if k != i)
            penalties[i][j] = C[i][j] - row_min - col_min

    while sum(S) > 0 and sum(D) > 0:
        # Find the cell with the highest penalty
        max_penalty = -1
        max_i = -1
        max_j = -1
        for i in range(m):
            for j in range(n):
                if S[i] > 0 and D[j] > 0 and penalties[i][j] > max_penalty:
                    max_penalty = penalties[i][j]
                    max_i = i
                    max_j = j

        # Allocate as much as possible to the cell with the highest penalty
        allocation_amount = min(S[max_i], D[max_j])
        allocation[max_i][max_j] = allocation_amount
        S[max_i] -= allocation_amount
        D[max_j] -= allocation_amount

        # Recalculate penalties
        for i in range(m):
            for j in range(n):
                if S[i] > 0 and D[j] > 0:
                    row_min = min(C[i][k] for k in range(n) if k != j)
                    col_min = min(C[k][j] for k in range(m) if k != i)
                    penalties[i][j] = C[i][j] - row_min - col_min

    return allocation

# print(russell_approximation([140, 180, 160], [[2, 3, 4, 2, 4], [8, 4, 1, 4, 1], [9, 7, 3, 7, 2]], [60, 70, 120, 130, 100]))