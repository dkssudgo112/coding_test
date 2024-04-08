T = int(input())


for i in range(T):
    k = int(input())
    n = int(input())
    dp = [[0]*(n+1) for i in range(k+1)]

    for i in range(1,n+1):
        dp[0][i] = i
    

    for a in range(1,k+1):
        for b in range(1,n+1):
            for c in range(1,b+1):
                dp[a][b] += dp[a-1][c]

    print(dp[k][n])
