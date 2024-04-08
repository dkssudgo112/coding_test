T = int(input())

for i in range(T):
    m, n = map(int, input().split())

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
        dp[i][1] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    print(dp[n][m])