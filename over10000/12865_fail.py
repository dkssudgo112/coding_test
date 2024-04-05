n, k = map(int, input().split())

w_li = []
v_li = []

for i in range(n):
    w,v = map(int, input().split())
    w_li.append(w)
    v_li.append(v)


dp = [[0] * 100000 for i in range(n)]


def solve(n, v_sum, w_sum, idx):
    if n <= idx:
        return v_sum
    if dp[idx][w_sum] != 0:
        return dp[idx][w_sum]

    global k
    if w_sum + w_li[idx] <= k:
        result =  max(solve(n, v_sum + v_li[idx], w_sum + w_li[idx], idx+1), solve(n, v_sum, w_sum, idx+1))
        dp[idx][w_sum] = result
        return result
    return solve(n, v_sum, w_sum, idx+1)
    
print(solve(n, 0, 0, 0))

