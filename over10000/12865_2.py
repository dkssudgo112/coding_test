n, k = map(int, input().split())

w_li = []
v_li = []

for i in range(n):
    w,v = map(int, input().split())
    w_li.append(w)
    v_li.append(v)


dp = [[0]*(k+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= w_li[i-1]:  
            dp[i][j] = max(v_li[i-1]+dp[i-1][j-w_li[i-1]],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k]) 