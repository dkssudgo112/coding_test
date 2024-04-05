


n = int(input())
li = []

dp = [-1]*n

for i in range(n):
    li.append(int(input()))


def solve(n,idx):
    if n <= idx:
        return 0
    
    if dp[idx] != -1:
        return dp[idx]

    if idx+1 < n:
        result = max(solve(n, idx+2)+li[idx], solve(n, idx+1), solve(n, idx+3)+li[idx] + li[idx+1])
        dp[idx] = result
        return result
    else:
        result = max(solve(n, idx+2)+li[idx], solve(n, idx+1))
        dp[idx] = result
        return result
    
print(solve(n,0))