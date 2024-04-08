N = int(input())

"""
1 = 1

2 = 2

3 = 3

4 = 1

5 = 2

6 = 3

7 = 4

8 = 2

9 = 1

10 = 2

11 = 3

12 = 3


dp[N] = dp[N-int_N] +1

"""

import math


dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1



i = N
for i in range(2,N+1):
    int_i = math.floor(math.sqrt(i))
    for j in range(1,int_i+1):
        if dp[i] > dp[i-j*j]+1 and dp[i] !=0:
            dp[i] = dp[i-j*j]+1
        elif dp[i] ==0:
            dp[i] = dp[i-j*j]+1
        else:
            continue

print(dp[N])
