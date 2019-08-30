def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ", sep="  ");
        print()
                       
def subset_sum(n_set, w):
    n = len(n_set)
    sum_table = [['x'] * (w+1) for _ in range(n+1)]

    for _ in range(w+1):
        sum_table[0][_] = 0
    for _ in range(n+1):
        sum_table[_][0] = 0

    for j in range(1, n+1):
        for w_j in range(1, w+1):
            print("Processing j=", j, "set[j]= ", n_set[j-1], "for w_j=", w_j)
            if n_set[j-1] > w_j:
                sum_table[j][w_j] = sum_table[j-1][w_j]
            else:
                sum_table[j][w_j] = max(sum_table[j-1][w_j], w_j + sum_table[j-1][w-w_j])
        print_matrix(sum_table)
    return sum_table[n][w]

print("Subset_sum -> ", subset_sum([3, 34, 4, 12, 5, 2], 9))
    
