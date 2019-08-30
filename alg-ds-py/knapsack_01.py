def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ", sep="    ");
        print()
                       
def knapsack_01(val, wt, W):
    n = len(val)
    K = [[0] * (W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],
                              K[i-1][w])
    return K[n][w]

print("Knapsack_01 -> ", knapsack_01([ 60, 100, 120],[10, 20, 30], 50))
    
