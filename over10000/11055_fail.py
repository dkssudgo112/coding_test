n = int(input())
li = list(map(int, input().split()))

# Initialize the memoization table with -1
dp = [[-1]*n for _ in range(n)]

def solve(n, p_idx, idx):
    if n <= idx:
        return 0
    
    # If the result is already computed, return it
    if dp[p_idx][idx] != -1:
        return dp[p_idx][idx]
    
    if li[p_idx] < li[idx]:
        dp[p_idx][idx] = max(solve(n,p_idx,idx+1), li[idx] + solve(n, idx,idx+1))
    else:
        dp[p_idx][idx] = solve(n, p_idx, idx+1)
    
    return dp[p_idx][idx]

sol_li = []
for i in range(len(li)):
       sol_li.append(li[i]+solve(n, i, i))

print(max(sol_li))