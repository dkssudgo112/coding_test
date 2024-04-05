from copy import deepcopy
n = int(input())
data = list(map(int, input().split()))
dp = deepcopy(data)

for i in range(1,n):
    for j in range(i):
        # 현재 인덱스보다 이전에 작은 값을 만나면
        # 이전 작은 값까지의 증가 합 더하기 현재 위치 값이 가장 큰 값을 구한다.
        if data[j] < data[i]:
            dp[i] = max(dp[j]+data[i], dp[i])
print(max(dp))